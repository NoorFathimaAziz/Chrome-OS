from google.oauth2 import service_account
from googleapiclient.discovery import build
from src.config import ChromeConfig

class GoogleService:

    def __init__(self, scope:list[str]=[]):
        self.scope = scope
        
    def get_credentials(self):

        """Get credentials from service account JSON file."""

        credentials = service_account.Credentials.from_service_account_file(
            ChromeConfig.SERVICE_ACCOUNT_FILE,
            scopes=self.scope,
            subject=ChromeConfig.ADMIN_MAIL
        )
    
        return credentials

    def build_service(self):
        """Build and return the Admin SDK Directory API service."""
  
        credentials = self.get_credentials()
        service = build('admin', 'directory_v1', credentials=credentials)
        return service 

    def chrome_policy_service(self):

        credentials = self.get_credentials()
        service = build('chromepolicy', 'v1', credentials=credentials)
        return service
    