import os

class Config(object):
  GROUP_ID = int(os.environ.get("GROUP_ID", "-1001565165506"))
  ADMINS = [id for id in os.environ.get("ADMINS").split(" ")]
