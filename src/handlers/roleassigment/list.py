from src.config import ChromeScopes,ChromeConfig
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError

class RoleAssList:
    @staticmethod
    def list_roleass(**kwargs): 
            service = GoogleService([ChromeScopes.ROLE]).build_service()
            response = service.roleAssignments().list(customer = ChromeConfig.CUSTOMER_ID,**kwargs).execute()
            return {'success': True, 'data': response}