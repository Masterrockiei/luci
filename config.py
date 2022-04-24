import os
from os import getenv

GROUP_ID = int(getenv("GROUP_ID", "--1001592740366"))
ADMINS = [id for id in getenv("ADMINS").split(" ")]
SESSION_NAME = getenv("SophieMusicBot", "session")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
  
