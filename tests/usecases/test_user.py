import uuid
from datetime import datetime

from messageboard.models.models import ObjectKey, ObjectType, User


def _to_isoformat(dt: datetime = None):
    if not dt:
        dt = datetime.utcnow()
    return f"{dt.isoformat(sep='T', timespec='milliseconds')}Z"


user_dict = {
    "obj_key": ObjectKey.USER,
    "obj_id": f"user#{uuid.uuid4()}",
    "name": "john",
    "created_at": _to_isoformat(),
    "updated_at": _to_isoformat(),
    "email": "john.doe@email.com",
    "board_ids": [],
    "obj_type": ObjectType.USER,
}


def test_create_user(items_table):
    from messageboard.usecases.user import create_user

    user = User.from_dict(user_dict)
    assert create_user(user) == user_dict
