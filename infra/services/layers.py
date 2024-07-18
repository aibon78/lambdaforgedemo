from aws_cdk import aws_lambda as _lambda
from lambda_forge.path import Path


class Layers:
    def __init__(self, scope) -> None:

        # self.layer = _lambda.LayerVersion.from_layer_version_arn(
        #     scope,
        #     id="Layer",
        #     layer_version_arn="",
        # )
        pass

        self.qlq_layer = _lambda.LayerVersion(
            scope,
            id='QlqLayer',
            code=_lambda.Code.from_asset(Path.layer('layers/qlq')),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
            description='',
         )
