from src.config import ChromeScopes,ChromeConfig
from src.credentials.google_auth import GoogleService

class SchemaDelete:
    def __init__(self):   
        pass
    def handle(self, schemaKey):
        service = GoogleService([ChromeScopes.SCHEMAS]).build_service()
        response = service.schemas().delete(
               customerId=ChromeConfig.CUSTOMER_ID, 
               schemaKey = schemaKey 
            ).execute()
        return response 