from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class DomainAdd:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.DOMAIN]).build_service()
        reponse = service.domains().insert(customer=ChromeConfig.CUSTOMER_ID, body=body).execute()
        return reponse