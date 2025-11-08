from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class PhotoDelete:
    def __init__(self):   
        pass
    def handle(self, userKey):
        service = GoogleService([ChromeScopes.USER]).build_service()
        response = service.users().photos().delete(
                userKey=userKey
            ).execute()
        return response