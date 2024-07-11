from infra.services import Services

class RockScissorPaperConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Rock-scissor-paper",
            path="./functions/rock_scissor_paper",
            description="rock scissor paper",
            
        )

        services.api_gateway.create_endpoint("GET", "/rock-scissor-paper", function, public=True)

            