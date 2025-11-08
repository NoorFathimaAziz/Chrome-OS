from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class MakeAdmin:
    def __init__(self):  
        pass
    def handle(self, body):
        service = GoogleService([ChromeScopes.USER]).build_service()
        response = service.users().makeAdmin(
                userKey=body['userKey'],
                body= body
            ).execute() 
            
            