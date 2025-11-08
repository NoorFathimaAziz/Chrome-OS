from src.config import ChromeScopes
from src.config import ChromeConfig
from src.credentials.google_auth import GoogleService

class Updatenotifi:
    def __init__(self):
        pass
    def update(self, body):
        service = GoogleService([ChromeScopes.NOTIFICATION]).build_service()
        response = service.users().update(
                customer=body['customer'],
                notificationId =body['notificationId'],
                body=body['update']
            ).execute()
        return response
        
       