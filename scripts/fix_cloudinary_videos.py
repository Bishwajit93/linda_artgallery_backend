# scripts/fix_cloudinary_videos.py
import os, django, cloudinary.uploader

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from artgallery.models import Video

BASE = os.getenv("CLOUDINARY_BASE_FOLDER", "linda_artgallery").strip("/")

moved = 0
for v in Video.objects.all():
    if not v.video:
        continue
    old_pid = v.video.public_id
    if old_pid.startswith(BASE + "/"):
        continue  # already normalized

    new_pid = f"{BASE}/{old_pid}"
    try:
        cloudinary.uploader.rename(
            old_pid, new_pid,
            resource_type="video",
            overwrite=True
        )
        v.video = new_pid
        v.save(update_fields=["video"])
        moved += 1
        print(f"✅ Moved {old_pid} -> {new_pid}")
    except Exception as e:
        print(f"❌ Failed {old_pid}: {e}")

print("Done. Total moved:", moved)
