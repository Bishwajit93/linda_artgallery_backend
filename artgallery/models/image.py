from django.conf import settings
from django.db import models
from pathlib import Path
from PIL import Image as PilImage, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from io import BytesIO
import os
from cloudinary.models import CloudinaryField

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = CloudinaryField("image", folder="images/artworks")  # Store in Cloudinary
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["order", "-created_at"]

    def save(self, *args, **kwargs):
        """
        Keep your watermarking logic, but now works for local files before upload to Cloudinary.
        Note: Cloudinary processes after save, so watermarking happens on the file before sending.
        """
        # If image is uploaded from local, watermark it
        if hasattr(self.image, "path") and os.path.exists(self.image.path):
            img_path = self.image.path
            img = PilImage.open(img_path).convert("RGBA")

            script_font_path = Path(settings.BASE_DIR) / "assets" / "fonts" / "GreatVibes-Regular.ttf"
            default_font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

            font_size = max(16, int(min(img.size) / 20))
            try:
                font = ImageFont.truetype(str(script_font_path), font_size)
            except Exception:
                font = ImageFont.truetype(default_font_path, font_size)

            draw = ImageDraw.Draw(img)
            text = "Linda Güzel"

            try:
                bbox = draw.textbbox((0, 0), text, font=font)
                text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            except Exception:
                text_w, text_h = draw.textsize(text, font=font)

            padding = max(10, font_size // 4)
            x = img.width - text_w - padding
            y = img.height - text_h - padding

            patch_w = min(200, img.width // 5)
            patch_h = min(100, img.height // 8)
            patch_box = (img.width - patch_w, img.height - patch_h, img.width, img.height)

            try:
                patch = img.crop(patch_box).convert("L")
                avg_brightness = sum(patch.getdata()) / (patch_w * patch_h)
            except Exception:
                avg_brightness = 128

            if avg_brightness < 128:
                fg = (255, 255, 255, 170)
                shadow = (0, 0, 0, 110)
            else:
                fg = (0, 0, 0, 170)
                shadow = (255, 255, 255, 110)

            shadow_offset = max(1, font_size // 20)
            draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow)
            draw.text((x, y), text, font=font, fill=fg)

            buffer = BytesIO()
            img.convert("RGB").save(buffer, format="JPEG", quality=90)
            file_content = ContentFile(buffer.getvalue())
            self.image.save(os.path.basename(self.image.name), file_content, save=False)
            buffer.close()

        super().save(*args, **kwargs)
