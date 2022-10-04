from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

class EnvLoader():
    def __init__(self):
        self.token = getenv("TOKEN")
        self.guild_id = getenv("GUILD_ID")
        self.pexels_api_key = getenv("PEXELS_API_KEY")