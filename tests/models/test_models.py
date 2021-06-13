import uuid
from datetime import datetime

from messageboard.models.models import ObjectKey, ObjectType, User, Board, Message
from messageboard.utils.common import to_isoformat


def test_user_init():
    obj_key = ObjectKey.USER
    obj_id = f"user#{uuid.uuid4()}"
    dt = to_isoformat()
    user = User(obj_key, obj_id, "john", dt, dt, "john.doe@email.com", [], ObjectType.USER)

    assert user.obj_key == obj_key
    assert user.obj_id == obj_id
    assert user.name == "john"
    assert user.created_at == dt
    assert user.updated_at == dt
    assert user.board_ids == []
    assert user.obj_type == ObjectType.USER


def test_user_to_dict():
    obj_id = f"user#{uuid.uuid4()}"
    dt = to_isoformat()
    init_dict = {
        "obj_key": ObjectKey.USER,
        "obj_id": obj_id,
        "name": "john",
        "created_at": dt,
        "updated_at": dt,
        "email": "john.doe@email.com",
        "board_ids": [],
        "obj_type": ObjectType.USER,
    }

    user = User.from_dict(init_dict)

    assert user.to_dict() == init_dict


def test_user_model_comparison():
    obj_id = f"user#{uuid.uuid4()}"
    dt = to_isoformat()
    init_dict = {
        "obj_key": ObjectKey.USER,
        "obj_id": obj_id,
        "name": "john",
        "created_at": dt,
        "updated_at": dt,
        "email": "john.doe@email.com",
        "board_ids": [],
        "obj_type": ObjectType.USER,
    }

    user1 = User.from_dict(init_dict)
    user2 = User.from_dict(init_dict)

    assert user1 == user2


def test_board_init():
    obj_key = ObjectKey.BOARD
    obj_id = f"board#{uuid.uuid4()}"
    dt = to_isoformat()
    board = Board(obj_key, obj_id, "the board", dt, dt, ObjectType.BOARD)

    assert board.obj_key == obj_key
    assert board.obj_id == obj_id
    assert board.name == "the board"
    assert board.created_at == dt
    assert board.updated_at == dt
    assert board.obj_type == ObjectType.BOARD


def test_message_init():
    obj_key = ObjectKey.BOARD
    obj_id = f"msg#{uuid.uuid4()}"
    dt = to_isoformat()
    message = Message(obj_key, obj_id, "the message", obj_id, obj_id, dt, dt, ObjectType.MESSAGE)

    assert message.obj_key == obj_key
    assert message.obj_id == obj_id
    assert message.message == "the message"
    assert message.user_id == obj_id
    assert message.board_id == obj_id
    assert message.created_at == dt
    assert message.updated_at == dt
    assert message.obj_type == ObjectType.MESSAGE
