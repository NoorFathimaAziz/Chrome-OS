from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService 



class MoveChromeOS:

    def __init__(self) ->None:
        pass

    def move(self,body):
        service = GoogleService([ChromeScopes.CHROMEOS]).build_service()

        org_unit_path = '/cruxchromeapi Testing OU/team sanjeev'
        
        response = service.chromeosdevices().moveDevicesToOu(
            customerId = ChromeConfig.CUSTOMER_ID,
            orgUnitPath = org_unit_path,
            body=body
        ).execute()

        return response


