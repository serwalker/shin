# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB/blob/main/LICENSE/>.
#


import sys
import importlib
from pyrogram import idle
from uvloop import install
from CtrlUB.config import BOT_TOKEN

from CtrlUB.version import __version__
from CtrlUB import app, bot, BOTLOG_CHATID, LOOP, aiosession
from CtrlUB.helpers.misc import heroku, git
from CtrlUB.logging import LOGGER


async def main():
    if BOT_TOKEN:
            await app.start()
    await bot.start()
    LOGGER("CtrlUB").info(f"Bot v{__version__} is actived! 🔥")
    await idle()
    await aiosession.close()

if __name__ == "__main__":
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
