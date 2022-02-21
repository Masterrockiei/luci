import os

class Config(object):
  GROUP_ID = int(os.environ.get("GROUP_ID", "-1001565165506"))
  ADMINS = [id for id in os.environ.get("ADMINS").split(" ")]
  SESSION_NAME = os.environ.get("RiyaMusicBot", "session")
  API_HASH = os.environ.get("api_hash")
  API_ID =  int(os.environ.get("api_id"))
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  
