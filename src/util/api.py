import aiohttp
from util import env_loader

class api():
    def __init__(self):
        self.url = "https://api.pexels.com/v1/search"
        self.token = env_loader.EnvLoader().token
        self.headers = {
            'Authorization': self.token,
        }
    
    async def get(self, params: str):
        if params is None:
            return None
        self.params = {
            'query': params,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=self.headers, params=self.params) as response:
                return await response.json()