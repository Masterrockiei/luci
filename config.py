import os

class Config(object):
  GROUP_ID = int(os.environ.get("GROUP_ID", "-1001565165506"))
  ADMINS = [id for id in os.environ.get("ADMINS").split(" ")]
  SESSION_NAME = os.environ.get("RiyaMusicBot", "session")
  API_HASH = os.environ.get("API_HASH")
  API_ID =  int(os.environ.get("API_ID", ""))
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  
