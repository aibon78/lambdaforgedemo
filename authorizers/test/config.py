from infra.services import Services

class TestAuthorizerConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="TestAuthorizer",
            path="./authorizers/test",
            description="qlq"
        )

        services.api_gateway.create_authorizer(function, name="test", default=False)
