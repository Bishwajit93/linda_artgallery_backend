# artgallery/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video
import cloudinary.api, os

BASE = os.getenv("CLOUDINARY_BASE_FOLDER", "linda_artgallery").strip("/")

@receiver(post_save, sender=Video)
def fill_video_duration(sender, instance: Video, created, **kwargs):
    if not instance.video or instance.duration_seconds:
        return

    pid = instance.video.public_id
    candidates = [pid]
    if not pid.startswith(BASE + "/"):
        candidates.append(f"{BASE}/{pid}")

    for cid in candidates:
        try:
            info = cloudinary.api.resource(cid, resource_type="video")
            dur = info.get("duration")
            if dur:
                instance.duration_seconds = int(round(dur))
                instance.save(update_fields=["duration_seconds"])
                break
        except Exception:
            continue
