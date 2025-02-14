import aws_cdk as cdk
from constructs import Construct


class PDPInsightStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # S3 Bucket for dataset and PDP storage
        bucket = cdk.aws_s3.Bucket(self, "PDPInsightBucket")


app = cdk.App()
PDPInsightStack(app, "PDPInsightStack")
app.synth()
