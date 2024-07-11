from functions.rock_scissor_paper.config import RockScissorPaperConfig
from functions.hello_andre.config import HelloAndreConfig

from functions.hello_world.config import HelloWorldConfig
from docs.config import DocsConfig
from aws_cdk import Stack
from constructs import Construct
from infra.services import Services


class LambdaStack(Stack):
    def __init__(self, scope: Construct, context, **kwargs) -> None:

        super().__init__(scope, f"{context.name}-Lambda-Stack", **kwargs)

        self.services = Services(self, context)

        # Docs
        DocsConfig(self.services)

        # HelloWorld
        HelloWorldConfig(self.services)

       
       

        # HelloAndre
        HelloAndreConfig(self.services)

        # Rock-scissor-paper
        RockScissorPaperConfig(self.services)
