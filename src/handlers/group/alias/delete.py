from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class AliasDeleteGroup:
    def __init__(self):
        pass

    def handle(self, body):
        # Validate input parameters
        if not body or 'groupKey' not in body or 'alias' not in body:
            return {"error": "Both grouprKey and alias are required in the request body"}, 400

        try:
            # Extract userKey and alias from body
            group_key = body['groupKey']
            alias = body['alias']

            # Build Google service
            service = GoogleService([ChromeScopes.GROUP]).build_service()
            
            # Execute alias deletion
            response = service.groups().aliases().delete(
                groupKey=group_key,
                alias=alias
            ).execute()
            
            return {"message": "Alias deleted successfully", "response": response}, 200
        
        except Exception as e:
            return {"error": str(e)}, 500 