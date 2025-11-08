from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class Listpriv:

    def __init__(self) -> None:
        pass
    
    def list(self):
        service = GoogleService([ChromeScopes.PRIVILEGES]).build_service()
        response = service.roles().list(customer=ChromeConfig.CUSTOMER_ID).execute()
        return response 