import dataclasses
from typing import List


class ObjectKey:
    USER = "user"
    BOARD = "board"


class ObjectType:
    USER = "user"
    BOARD = "board"
    MESSAGE = "message"


class DictMixin:
    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class User(DictMixin):
    obj_key: str
    obj_id: str
    name: str
    created_at: str
    updated_at: str
    email: str
    board_ids: List[str] = dataclasses.field(default_factory=list)
    obj_type: str = ObjectType.USER


@dataclasses.dataclass
class Board(DictMixin):
    obj_key: str
    obj_id: str
    name: str
    created_at: str
    updated_at: str
    obj_type: str = ObjectType.BOARD


@dataclasses.dataclass
class Message(DictMixin):
    obj_key: str
    obj_id: str
    message: str
    user_id: str
    board_id: str
    created_at: str
    updated_at: str
    obj_type: str = ObjectType.MESSAGE
