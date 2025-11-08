from src.config import ChromeConfig
from src.config  import ChromeScopes
from src.credentials.google_auth import GoogleService


class ActionMobDevices:

    def __init__(self)-> None:
        pass

    def action(self,resourceId):
        service = GoogleService([ChromeScopes.MOBILE_DEVICES_ACTION]).build_service()
        response =  service.mobiledevices().action(customerId = ChromeConfig.CUSTOMER_ID, resourceId = resourceId).execute()
        return response