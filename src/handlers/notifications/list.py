from src.config import ChromeScopes
from src.config import ChromeConfig
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError

class ListNotifi:
    @staticmethod
    def list(customer,**kwargs): 
            service = GoogleService([ChromeScopes.NOTIFICATION]).build_service()
            response = service.notifications().list(customer = customer,**kwargs).execute()
            return {'success': True, 'data': response}
        
        