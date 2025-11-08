from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class GroupUpdate:
    def __init__(self):
        pass
    def handle(self, body):
        service = GoogleService([ChromeScopes.GROUP]).build_service()
        response = service.groups().update(
                groupKey=body['groupKey'],
                body=body['update']
            ).execute()
        return response 