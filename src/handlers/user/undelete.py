from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class UserUndelete:
    def __init__(self):  
        pass
    def handle(self, body):
        undelete_body = {
            "orgUnitPath": body.get('orgUnitPath', '/'),  
        }
        service = GoogleService([ChromeScopes.USER]).build_service()
        response = service.users().undelete(
                userKey=body['userKey'],
                body=undelete_body
            ).execute()
            
            
        
        
            



