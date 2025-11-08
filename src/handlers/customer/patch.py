from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class CustomerPatch:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.CUSTOMER]).build_service()
        reponse = service.customers().patch(
            customerKey=ChromeConfig.CUSTOMER_ID, 
            body = body
        ).execute()
        return reponse