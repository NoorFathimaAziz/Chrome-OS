from src.config import ChromeScopes,ChromeConfig
from src.credentials.google_auth import GoogleService

class SchemaUpdate:
    def __init__(self):
        pass
    def handle(self, body):
        service = GoogleService([ChromeScopes.SCHEMAS]).build_service()
        response = service.schemas().update(
                customerId=ChromeConfig.CUSTOMER_ID,
                schemaKey = body['schemaKey'],
                body=body['update']
            ).execute()
        return response 