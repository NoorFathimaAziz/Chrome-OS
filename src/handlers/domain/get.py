from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class DomainGet:

    def __init__(self) -> None:
        pass

    def handle(self, domainName):
        service = GoogleService([ChromeScopes.DOMAIN_READ_ONLY]).build_service()
        reponse = service.domains().get(customer=ChromeConfig.CUSTOMER_ID, domainName = domainName).execute()
        return reponse
    
