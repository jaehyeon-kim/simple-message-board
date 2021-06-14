import json
from messageboard.models.models import User
import messageboard.handlers.app as app


def test_create_user(lambda_context, items_table):
    event = {
        "path": "/user",
        "httpMethod": "POST",
        "body": '{ "name": "john", "email": "john.doe@email.com" }',
        "requestContext": {"requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef"},
    }

    result = app.lambda_handler(event, lambda_context)
    body = json.loads(result["body"])

    assert result["statusCode"] == 200
    assert body["name"] == "john"
    assert body["email"] == "john.doe@email.com"


def test_get_user_susccess(lambda_context, items_table):
    from messageboard.usecases.user import create_user

    user = User.from_request({"name": "john", "email": "john.doe@email.com"})
    create_user(user)

    event = {
        "path": "/user",
        "httpMethod": "GET",
        "queryStringParameters": {"email": "john.doe@email.com"},
        "requestContext": {"requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef"},
    }

    result = app.lambda_handler(event, lambda_context)
    body = json.loads(result["body"])

    assert result["statusCode"] == 200
    assert body["name"] == "john"
    assert body["email"] == "john.doe@email.com"


def test_get_user_failure(lambda_context, items_table):
    event = {
        "path": "/user",
        "httpMethod": "GET",
        "queryStringParameters": {"email": "john.doe@email.com"},
        "requestContext": {"requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef"},
    }

    result = app.lambda_handler(event, lambda_context)
    body = json.loads(result["body"])

    assert result["statusCode"] == 404
    assert body["message"] == "user with email john.doe@email.com is not found"
