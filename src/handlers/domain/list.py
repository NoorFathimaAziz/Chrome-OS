from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class DomainList:

    def __init__(self) -> None:
        pass
    
    def handle(self):
        service = GoogleService([ChromeScopes.DOMAIN_READ_ONLY]).build_service()
        reponse = service.domains().list(customer=ChromeConfig.CUSTOMER_ID).execute()
        return reponse 
