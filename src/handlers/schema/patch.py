from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class SchemaPatch:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.SCHEMAS]).build_service()
        reponse = service.schemas().patch( 
            customerId=ChromeConfig.CUSTOMER_ID,
            schemaKey = body['schemaKey'],
            body=body['update']
        ).execute()
        return reponse