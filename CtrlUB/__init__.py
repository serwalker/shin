# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB/blob/main/LICENSE/>.
#


import asyncio
import sys
import time
from datetime import datetime
from typing import Any, Dict
from aiohttp import ClientSession
from gpytranslate import Translator
from pyrogram import Client
from pyrogram.types import *
from CtrlUB.config import API_ID, API_HASH, STRING_SESSION, DB_URL, BOTLOG_CHATID
from CtrlUB.logging import LOGGER
from CtrlUB.startup.client import Userbot, Bot


LOOP = asyncio.get_event_loop_policy().get_event_loop()
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
StartTime = time.time()
START_TIME = datetime.now()
TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}


API_ID = API_ID
API_HASH = API_HASH
DB_URL = DB_URL

if not STRING_SESSION:
    LOGGER(__name__).error("No String Session Found! Exiting!")
    sys.exit()

if not API_ID:
    LOGGER(__name__).error("No API_ID Found! Exiting!")
    sys.exit()

if not API_HASH:
    LOGGER(__name__).error("No API_HASH Found! Exiting!")
    sys.exit()

if BOTLOG_CHATID:
    BOTLOG_CHATID = BOTLOG_CHATID
else:
    BOTLOG_CHATID = "me"

bot = Userbot()
app = Bot()
