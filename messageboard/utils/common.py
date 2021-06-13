import os
import boto3
from datetime import datetime


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION", "us-east-1"))
    table = dynamodb.Table(os.environ["ITEMS_TABLE"])
    return table


def to_isoformat(dt: datetime = None):
    if not dt:
        dt = datetime.utcnow()
    return f"{dt.isoformat(sep='T', timespec='milliseconds')}Z"
