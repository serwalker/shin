# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB-Userbot/blob/main/LICENSE/>.
#


from distutils.util import strtobool
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
ALIVE_LOGO = getenv("ALIVE_LOGO", None)
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = []
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BRANCH = getenv("BRANCH", "main")
DB_URL = getenv("DATABASE_URL", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
STRING_SESSION = getenv("STRING_SESSION", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
