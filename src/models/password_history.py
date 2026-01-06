from datetime import datetime
from bson import ObjectId


class PasswordHistory:
    def __init__(self, password_entry_id, encrypted_old_password, changed_at=None, _id=None):
        self._id = _id or ObjectId()
        self.password_entry_id = password_entry_id
        self.encrypted_old_password = encrypted_old_password
        self.changed_at = changed_at or datetime.utcnow()

    def to_dict(self):
        return {
            "_id": self._id,
            "password_entry_id": self.password_entry_id,
            "encrypted_old_password": self.encrypted_old_password,
            "changed_at": self.changed_at
        }

    @staticmethod
    def from_dict(data):
        return PasswordHistory(
            password_entry_id=data.get("password_entry_id"),
            encrypted_old_password=data.get("encrypted_old_password"),
            changed_at=data.get("changed_at"),
            _id=data.get("_id")
        )