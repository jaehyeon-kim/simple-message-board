from messageboard.models.models import User
from messageboard.utils.common import get_table


def create_user(user: User):
    items_table = get_table()
    items_table.put_item(Item=user.to_dict())
    return user.to_dict()
