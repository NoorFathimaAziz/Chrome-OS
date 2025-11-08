from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class GroupDelete:
    def __init__(self):   
        pass
    def handle(self, groupKey):
        service = GoogleService([ChromeScopes.GROUP]).build_service()
        response = service.groups().delete(
                groupKey=groupKey 
            ).execute()
        return response