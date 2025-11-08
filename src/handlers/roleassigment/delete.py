from src.config import ChromeScopes,ChromeConfig
from src.credentials.google_auth import GoogleService

class RoleAssDelete:
    def __init__(self):   
        pass
    def handle(self, roleAssignmentId):
        service = GoogleService([ChromeScopes.ROLE]).build_service()
        response = service.roleAssignments().delete(
                customer = ChromeConfig.CUSTOMER_ID,
               roleAssignmentId = roleAssignmentId
            ).execute()
        return response