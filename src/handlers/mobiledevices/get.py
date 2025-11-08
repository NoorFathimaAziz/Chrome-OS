from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService
from googleapiclient.errors import HttpError



class GetMobdevices:
    
    def __init__(self) ->None:
        pass

    def get(self,resourceId):
        service =GoogleService([ChromeScopes.MOBILE_DEVICES]).build_service()
        response = service.mobiledevices().get(
            customerId = ChromeConfig.CUSTOMER_ID,
            resourceId = resourceId
        ).execute()
        return response
    
    # def get(self, resourceId):
    #     service = GoogleService([ChromeScopes.CHROMEOS_READ_ONLY]).build_service()
    #     response = service.mobiledevices().get(
    #         customerId=ChromeConfig.CUSTOMER_ID, 
    #         resourceId=resourceId
    #     ).execute()
    #     return response 