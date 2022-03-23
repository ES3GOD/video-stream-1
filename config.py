from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME", "session")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ES3GOD/video-stream-1")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)  # Remember to give value in Seconds

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
