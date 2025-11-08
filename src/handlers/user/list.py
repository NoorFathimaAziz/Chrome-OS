from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError

class UserListHandler:
    @staticmethod
    def list_users(**kwargs): 
            service = GoogleService([ChromeScopes.USER]).build_service()
            response = service.users().list(**kwargs).execute()
            return {'success': True, 'data': response}
        
        