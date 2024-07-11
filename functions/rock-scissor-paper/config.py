from infra.services import Services

class Rock-scissor-paperConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Rock-scissor-paper",
            path="./functions/rock-scissor-paper",
            description="rock scissor paper",
            
        )

        services.api_gateway.create_endpoint("GET", "/rock-scissor-paper", function)

            