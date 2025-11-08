from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class RoleAssGet:

    def __init__(self) -> None:
        pass

    def handle(self, roleAssignmentId):
        service = GoogleService([ChromeScopes.ROLE_READ_ONLY]).build_service()
        reponse = service.roleAssignments().get(customer = ChromeConfig.CUSTOMER_ID,roleAssignmentId = roleAssignmentId).execute()  
        return reponse 