import os
from boto3.dynamodb.conditions import Key
from aws_lambda_powertools import Tracer

from messageboard.models.models import User
from messageboard.utils.common import get_table

tracer = Tracer()


@tracer.capture_method
def create_user(user: User):
    items_table = get_table()
    items_table.put_item(Item=user.to_dict())
    return user


@tracer.capture_method
def get_user(email: str):
    items_table = get_table()
    resp = items_table.query(
        IndexName=os.environ["QUERY_USER_INDEX"], KeyConditionExpression=Key("email").eq(email)
    )
    return User.from_dict(resp["Items"][0])
