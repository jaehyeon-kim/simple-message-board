import os
import boto3
import pytest
from moto import mock_dynamodb2


def pytest_generate_tests(metafunc):
    os.environ["AWS_REGION"] = "us-east-1"
    os.environ["ITEMS_TABLE"] = "simple-message-board"
    os.environ["QUERY_USER_INDEX"] = "query-user"
    os.environ["QUERY_ITEMS_INDEX"] = "query-items"
    os.environ["QUERY_ALL_OBJECTS_INDEX"] = "query-all-objects"


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture(scope="function")
def dynamodb(aws_credentials):
    with mock_dynamodb2():
        yield boto3.resource("dynamodb", region_name=os.environ["AWS_REGION"])


@pytest.fixture(scope="function")
def dynamodb_table(dynamodb):
    """Create a DynamoDB surveys table fixture."""
    table = dynamodb.create_table(
        TableName=os.environ["ITEMS_TABLE"],
        KeySchema=[
            {"AttributeName": "obj_key", "AttributeType": "HASH"},
            {"AttributeName": "obj_id", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "obj_key", "AttributeType": "S"},
            {"AttributeName": "obj_id", "AttributeType": "S"},
            {"AttributeName": "obj_type", "AttributeType": "S"},
            {"AttributeName": "email", "AttributeType": "S"},
        ],
        GlobalSecondaryIndexes=[
            {
                "IndexName": os.environ["QUERY_ITEMS_INDEX"],
                "KeySchema": [
                    {"AttributeName": "email", "KeyType": "HASH"},
                ],
                "Projection": {
                    "ProjectionType": "ALL",
                },
            },
            {
                "IndexName": os.environ["QUERY_ITEMS_INDEX"],
                "KeySchema": [
                    {"AttributeName": "obj_key", "KeyType": "HASH"},
                    {"AttributeName": "obj_id", "KeyType": "RANGE"},
                ],
                "Projection": {
                    "ProjectionType": "ALL",
                },
            },
            {
                "IndexName": os.environ["QUERY_ALL_OBJECTS_INDEX"],
                "KeySchema": [
                    {"AttributeName": "obj_type", "KeyType": "HASH"},
                    {"AttributeName": "obj_id", "KeyType": "RANGE"},
                ],
                "Projection": {
                    "ProjectionType": "ALL",
                },
            },
        ],
        BillingMode="PAY_PER_REQUEST",
    )
    table.meta.client.get_waiter("table_exists").wait(TableName=os.environ["ITEMS_TABLE"])
    yield
