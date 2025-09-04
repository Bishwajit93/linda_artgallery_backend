import os
import requests
from django.core.files.storage import Storage
from django.conf import settings

class BunnyStorage(Storage):
    """
    Custom Django storage backend for BunnyCDN
    - Handles saving and deleting files
    - Provides exists() so Django admin stops complaining
    """

    def _save(self, name, content):
        # Build upload URL
        upload_url = f"{settings.BUNNY_ENDPOINT}/{settings.BUNNY_STORAGE_NAME}/{name}"

        # Upload the file using Bunny API
        response = requests.put(
            upload_url,
            data=content.read(),
            headers={"AccessKey": settings.BUNNY_STORAGE_KEY},
        )

        if response.status_code not in [201, 202]:
            raise Exception(f"❌ Bunny upload failed: {response.text}")

        return name

    def exists(self, name):
        """
        Check if a file already exists in Bunny Storage
        """
        check_url = f"{settings.BUNNY_ENDPOINT}/{settings.BUNNY_STORAGE_NAME}/{name}"
        response = requests.head(check_url, headers={"AccessKey": settings.BUNNY_STORAGE_KEY})
        return response.status_code == 200

    def url(self, name):
        """
        Return public CDN URL for a file
        """
        return f"{settings.BUNNY_CDN_URL}{name}"

    def delete(self, name):
        """
        Delete a file from Bunny Storage
        """
        delete_url = f"{settings.BUNNY_ENDPOINT}/{settings.BUNNY_STORAGE_NAME}/{name}"
        response = requests.delete(delete_url, headers={"AccessKey": settings.BUNNY_STORAGE_KEY})
        if response.status_code not in [200, 204]:
            raise Exception(f"❌ Bunny delete failed: {response.text}")
