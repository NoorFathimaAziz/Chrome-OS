from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class RoleUpdate:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.ROLE]).build_service()
        reponse = service.roles().update(
            customer=ChromeConfig.CUSTOMER_ID, 
            roleId=body['roleId'], 
            body=body['update']
        ).execute()
        return reponse
    
