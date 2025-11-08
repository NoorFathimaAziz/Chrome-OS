from src.config import ChromeScopes,ChromeConfig
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError
 
class ListMobDevices:
    @staticmethod
    def list_mobile(**kwargs):
            service = GoogleService([ChromeScopes.MOBILE_DEVICES]).build_service()
            response = service.mobiledevices().list(customerId = ChromeConfig.CUSTOMER_ID ,**kwargs).execute()
            return {'success': True, 'data': response}