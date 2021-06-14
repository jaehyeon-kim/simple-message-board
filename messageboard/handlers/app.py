import json
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler.api_gateway import (
    ApiGatewayResolver,
    ProxyEventType,
    Response,
)

from messageboard.models.models import User
from messageboard.usecases.user import create_user, get_user

tracer = Tracer()
logger = Logger()
app = ApiGatewayResolver(proxy_type=ProxyEventType.APIGatewayProxyEvent)


@app.post("/user", cors=True)
@tracer.capture_method
def _create_user():
    user = User.from_request(app.current_event.json_body)
    create_user(user)
    return Response(
        status_code=200, content_type="application/json", body=json.dumps(user.to_dict())
    )


@app.get("/user", cors=True)
@tracer.capture_method
def _get_user():
    email = app.current_event.get_query_string_value("email")
    try:
        user = get_user(email)
        return Response(200, content_type="application/json", body=json.dumps(user.to_dict()))
    except IndexError:
        return Response(
            404,
            content_type="application/json",
            body=json.dumps({"message": f"user with email {email} is not found"}),
        )


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
