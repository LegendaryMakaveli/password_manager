from datetime import datetime
from bson import ObjectId


class PasswordEntry:
    def __init__(self, url, encrypted_password, user_id, folder_id=None, title=None, notes=None, created_at=None, updated_at=None, _id=None):
        self._id = _id or ObjectId()
        self.title = title
        self.url = url
        self.encrypted_password = encrypted_password
        self.notes = notes
        self.user_id = user_id
        self.folder_id = folder_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self):
        return {
            "_id": self._id,
            "title": self.title,
            "url": self.url,
            "encrypted_password": self.encrypted_password,
            "notes": self.notes,
            "user_id": self.user_id,
            "folder_id": self.folder_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(data):
        return PasswordEntry(
            title=data.get("title"),
            url=data.get("url"),
            encrypted_password=data.get("encrypted_password"),
            notes=data.get("notes"),
            user_id=data.get("user_id"),
            folder_id=data.get("folder_id"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            _id=data.get("_id")
        )