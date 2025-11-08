from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class RoleDelete:

    def __init__(self) -> None:
        pass

    def handle(self, roleId):
        service = GoogleService([ChromeScopes.ROLE]).build_service()
        reponse = service.roles().delete(customer=ChromeConfig.CUSTOMER_ID, roleId= roleId).execute()
        return reponse 