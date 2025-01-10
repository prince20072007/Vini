from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("23648032"))
API_HASH = getenv("a7bfbe0052c9582b9c396eb13218b968")

BOT_TOKEN = getenv("8158321796:AAF_TRqWIJFEcDGwKI8Wfi-WkHQ-wHzSLPI", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7553806137"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tbcbotschat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tbc_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2107459523").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
