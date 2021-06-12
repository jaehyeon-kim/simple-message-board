import os
import boto3
import pytest
from moto import mock_s3, mock_dynamodb2


def pytest_generate_tests(metafunc):
    os.environ["AWS_REGION"] = "us-east-1"
    os.environ["ITEMS_TABLE"] = "simple-message-board"
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
            {"AttributeName": "objId", "KeyType": "HASH"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "objId", "AttributeType": "S"},
            {"AttributeName": "objType", "AttributeType": "S"},
        ],
        GlobalSecondaryIndexes=[
            {
                "IndexName": os.environ["QUERY_ALL_OBJECTS_INDEX"],
                "KeySchema": [
                    {"AttributeName": "objType", "KeyType": "HASH"},
                    {"AttributeName": "objId", "KeyType": "RANGE"},
                ],
                "Projection": {
                    "ProjectionType": "ALL",
                },
            }
        ],
        BillingMode="PAY_PER_REQUEST",
    )
    table.meta.client.get_waiter("table_exists").wait(TableName=os.environ["ITEMS_TABLE"])
    yield
