#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7754829341:AAGCplAKGutDjUShS0bvKydAX-38")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24213496"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "460587b3c127073be75378abec90ff56")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-10020358639"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@sukasukasuki")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "60037733"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://madara:madara@cluster0.qifw6tx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-100193806"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002058501"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[2073762128]
    for x in (os.environ.get("ADMINS", "6003783733 6893079708").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴀɴᴅᴀ ʜᴀʀᴜꜱ ʙᴇʀɢᴀʙᴜɴɢ ᴄʜᴀɴɴᴇʟ ᴅᴀʜᴜʟᴜ ᴀɢᴀʀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ‼️.\n\nꜱɪʟᴀʜᴋᴀɴ ʙᴇʀɢᴀʙᴜɴɢ ʟᴀʟᴜ ᴍᴜʟᴀɪ ᴜʟᴀɴɢ ʙᴏᴛ💋.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>subscribe channel agar dapat update media setiap hari!!</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ᴀɴᴅᴀ ʜᴀʀᴜꜱ ʙᴇʀɢᴀʙᴜɴɢ ᴄʜᴀɴɴᴇʟ ᴅᴀʜᴜʟᴜ ᴀɢᴀʀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ!!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
