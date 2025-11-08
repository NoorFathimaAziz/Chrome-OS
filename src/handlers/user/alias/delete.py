from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class AliasDelete:
    def __init__(self):
        pass

    def handle(self, body):
        # Validate input parameters
        if not body or 'userKey' not in body or 'alias' not in body:
            return {"error": "Both userKey and alias are required in the request body"}, 400

        try:
            # Extract userKey and alias from body
            user_key = body['userKey']
            alias = body['alias']

            # Build Google service
            service = GoogleService([ChromeScopes.USER]).build_service()
            
            # Execute alias deletion
            response = service.users().aliases().delete(
                userKey=user_key,
                alias=alias
            ).execute()
            
            return {"message": "Alias deleted successfully", "response": response}, 200
        
        except Exception as e:
            return {"error": str(e)}, 500 