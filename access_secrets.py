import os
import json
from google.cloud import secretmanager

def access_secret():

    client = secretmanager.SecretManagerServiceClient()
    secret_name = os.getenv("SECRET_NAME", "")
    project_id =  os.getenv("PROJECT_ID", "")
    request = {"name": f"projects/{project_id}/secrets/{secret_name}/versions/latest"}
    response = client.access_secret_version(request)
    secret_string = response.payload.data.decode("UTF-8")
    return json.loads(secret_string)