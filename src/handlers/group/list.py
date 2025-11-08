from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError

class GroupList:
    @staticmethod
    def list_group(**kwargs): 
            service = GoogleService([ChromeScopes.GROUP]).build_service()
            response = service.groups().list(**kwargs).execute()
            return {'success': True, 'data': response}