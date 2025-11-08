from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class List_Next_Role:

    def __init__(self) -> None:
        pass
    
    def handle(self):
        service = GoogleService([ChromeScopes.ROLE_READ_ONLY]).build_service()
        reponse = service.roles().list(customer=ChromeConfig.CUSTOMER_ID).execute()
        return reponse 