from datetime import datetime
from bson import ObjectId


class User:
    def __init__(self, email, password_hash, created_at=None, updated_at=None, _id=None):
        self._id = _id or ObjectId()
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(data):
        return User(
            email=data.get("email"),
            password_hash=data.get("password_hash"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            _id=data.get("_id")
        )
