import pytest
import uuid

from messageboard.models.models import ObjectKey, ObjectType, User
from messageboard.utils.common import to_isoformat

user_dict = {
    "obj_key": ObjectKey.USER,
    "obj_id": f"user#{uuid.uuid4()}",
    "name": "john",
    "created_at": to_isoformat(),
    "updated_at": to_isoformat(),
    "email": "john.doe@email.com",
    "board_ids": [],
    "obj_type": ObjectType.USER,
}


def test_create_user(items_table):
    from messageboard.usecases.user import create_user

    user = User.from_dict(user_dict)
    assert create_user(user) == user


def test_get_user_success(items_table):
    from messageboard.usecases.user import create_user, get_user

    user = User.from_dict(user_dict)
    create_user(user)

    assert get_user("john.doe@email.com") == user


def test_get_user_failure(items_table):
    from messageboard.usecases.user import create_user, get_user

    user = User.from_dict(user_dict)
    create_user(user)

    with pytest.raises(IndexError):
        get_user("jane.doe@email.com")
