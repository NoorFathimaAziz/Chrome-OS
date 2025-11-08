from src.config import ChromeScopes,ChromeConfig
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError

class CalList:
    @staticmethod
    def list(**kwargs): 
            service = GoogleService([ChromeScopes.CALENDAR]).build_service()
            response = service.resources().calendars().list(customer = ChromeConfig.CUSTOMER_ID,**kwargs).execute()
            return {'success': True, 'data': response}
        
        