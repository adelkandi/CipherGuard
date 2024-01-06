import os

from dotenv import load_dotenv
from CipherGuard import CipherBot

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

CipherBot.run(DISCORD_TOKEN)
