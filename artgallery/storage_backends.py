# artgallery/storage_backends.py
from django.core.files.storage import Storage
from django.conf import settings
import requests

class BunnyStorage(Storage):
    def _save(self, name, content):
        content.seek(0)  # reset file pointer
        upload_url = f"{settings.BUNNY_ENDPOINT}/{settings.BUNNY_STORAGE_NAME}/{name}"

        response = requests.put(
            upload_url,
            data=content,
            headers={"AccessKey": settings.BUNNY_STORAGE_KEY},
        )

        if response.status_code not in [201, 202]:
            raise Exception(f"❌ Bunny upload failed: {response.status_code} {response.text}")

        return name

    def exists(self, name):
        return False  # always overwrite

    def url(self, name):
        base = settings.BUNNY_CDN_URL.rstrip("/")
        return f"{base}/{name.lstrip('/')}"

    def delete(self, name):
        delete_url = f"{settings.BUNNY_ENDPOINT}/{settings.BUNNY_STORAGE_NAME}/{name}"
        response = requests.delete(delete_url, headers={"AccessKey": settings.BUNNY_STORAGE_KEY})
        if response.status_code not in [200, 204]:
            raise Exception(f"❌ Bunny delete failed: {response.status_code} {response.text}")

    def deconstruct(self):
        return ("artgallery.storage_backends.BunnyStorage", [], {})
