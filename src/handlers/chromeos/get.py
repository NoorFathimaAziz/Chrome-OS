from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class ChromeOSget:
    def __init__(self) -> None:
        pass

    def chromehandle(self, deviceId):
        service = GoogleService([ChromeScopes.CHROMEOS_READ_ONLY]).build_service()
        response = service.chromeosdevices().get(
            customerId=ChromeConfig.CUSTOMER_ID, 
            deviceId=deviceId
        ).execute()
        return response 