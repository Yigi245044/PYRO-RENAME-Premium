import os 
import logging 
from pyrogram import Client, __version__
from user import User, LOGGER
# import pyromod.listen

logging.getLogger().setLevel(logging.INFO)
 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6617104403:AAGVM-N4J3l-CMHO98Sp6-U3_26m2ZBsTjw")

API_ID = int(os.environ.get("API_ID", "21037450"))

API_HASH = os.environ.get("API_HASH", "05ac9eb7c523b83c51d89d1f2f91d58b")

class Bot(Client):  
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
        self.LOGGER = LOGGER
  
    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")








