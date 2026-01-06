from datetime import datetime
from bson import ObjectId


class Folder:
    def __init__(self, name, user_id, created_at=None, updated_at=None, _id=None):
        self._id = _id or ObjectId()
        self.name = name
        self.user_id = user_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(data):
        return Folder(
            name=data.get("name"),
            user_id=data.get("user_id"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            _id=data.get("_id")
        )