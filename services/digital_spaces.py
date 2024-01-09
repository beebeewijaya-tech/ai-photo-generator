import boto3
from decouple import config


class DigitalOceanSpaceService:
    session = boto3.session.Session()
    client = None
    bucket_name = None

    def __init__(self):
        self.bucket_name = config("SPACES_BUCKET_NAME")
        self.client = self.session.client('s3',
                                          endpoint_url=config("SPACES_BUCKET_URL"),
                                          region_name=config("SPACES_REGION"),
                                          aws_access_key_id=config("SPACES_ACCESS"),
                                          aws_secret_access_key=config("SPACES_SECRET"))

    def upload(self, file, filename):
        return self.client.put_object(Bucket=self.bucket_name,
                                      Key=filename,
                                      Body=file,  # The object's contents.
                                      ACL='public-read',
                                      )
