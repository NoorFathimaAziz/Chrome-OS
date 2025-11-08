from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class CustomerGet:

    def __init__(self) -> None:
        pass
    
    def handle(self):
        service = GoogleService([ChromeScopes.CUSTOMER_READ_ONLY]).build_service()
        reponse = service.customers().get(customerKey=ChromeConfig.CUSTOMER_ID).execute()
        return reponse
