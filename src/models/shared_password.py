from datetime import datetime
from bson import ObjectId


class SharedPassword:
    def __init__(self, password_entry_id, owner_id, shared_with_user_id, permission="read", created_at=None, _id=None):
        self._id = _id or ObjectId()
        self.password_entry_id = password_entry_id
        self.owner_id = owner_id
        self.shared_with_user_id = shared_with_user_id
        self.permission = permission
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            "_id": self._id,
            "password_entry_id": self.password_entry_id,
            "owner_id": self.owner_id,
            "shared_with_user_id": self.shared_with_user_id,
            "permission": self.permission,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return SharedPassword(
            password_entry_id=data.get("password_entry_id"),
            owner_id=data.get("owner_id"),
            shared_with_user_id=data.get("shared_with_user_id"),
            permission=data.get("permission", "read"),
            created_at=data.get("created_at"),
            _id=data.get("_id")
        )