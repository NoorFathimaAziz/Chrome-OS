from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class RoleAssAdd:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.ROLE]).build_service()
        reponse = service.roleAssignments().insert(customer = ChromeConfig.CUSTOMER_ID,body=body).execute()
        return reponse