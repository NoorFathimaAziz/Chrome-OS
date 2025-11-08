from src.config import ChromeScopes
from src.config import ChromeConfig
from src.credentials.google_auth import GoogleService


class DelMobdevices:
    def __init__(self):   
        pass
    def handle(self, resourceId):
        service = GoogleService([ChromeScopes.MOBILE_DEVICES]).build_service()
        response = service.mobiledevices().delete(
                customerId = ChromeConfig.CUSTOMER_ID,
                resourceId = resourceId
            ).execute()
        
           
        
        




        
       