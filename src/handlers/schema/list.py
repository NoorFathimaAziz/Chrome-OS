from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class SchemaList:

    def __init__(self) -> None:
        pass
    
    def handle(self):
        service = GoogleService([ChromeScopes.SCHEMAS_READ_ONLY]).build_service()
        reponse = service.schemas().list(customerId=ChromeConfig.CUSTOMER_ID).execute()
        return reponse 