from src.config import ChromeScopes,ChromeConfig
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError
 
class ChromeList:
    @staticmethod
    def list_chrome(**kwargs):
            service = GoogleService([ChromeScopes.CHROMEOS]).build_service()
            response = service.chromeosdevices().list(customerId = ChromeConfig.CUSTOMER_ID,**kwargs).execute()
            return {'success': True, 'data': response}

        
        