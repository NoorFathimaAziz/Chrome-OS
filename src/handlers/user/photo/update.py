from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class PhotoUpdate:
    def __init__(self):
        pass
    def handle(self, body):
        service = GoogleService([ChromeScopes.USER]).build_service()
        response = service.users().photos().update(
                userKey=body['userKey'],
                body=body['update']
            ).execute()
        return response