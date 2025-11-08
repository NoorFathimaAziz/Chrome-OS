from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class PolicySchemaList:

    def __init__(self) -> None:
        pass
    
    def handle(self, page_size, next_token):
        service = GoogleService([ChromeScopes.POLICY_READ_ONLY]).chrome_policy_service()
        response = service.customers().policySchemas().list(parent=f'customers/{ChromeConfig.CUSTOMER_ID}', pageSize = page_size, pageToken=next_token ).execute()
        return response