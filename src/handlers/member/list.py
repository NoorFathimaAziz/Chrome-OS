from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError

class MemberList:
    @staticmethod
    def list_member(**kwargs): 
            service = GoogleService([ChromeScopes.GROUP_MEMBER]).build_service()
            response = service.members().list(**kwargs).execute()
            return {'success': True, 'data': response}