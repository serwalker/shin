#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved


import sys

from pyrogram import Client
from CtrlUB.config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    BOTLOG_CHATID,
    STRING_SESSION as string1,
    STRING_SESSION2 as string2,
    STRING_SESSION3 as string3,
    STRING_SESSION4 as string4,
    STRING_SESSION5 as string5,
)
from pyrogram.enums import ParseMode
from CtrlUB.version import __version__
from CtrlUB.logging import LOGGER

MSG_ON = """
➠ **Client** `{}` **actived!**
➠ **CtrlUB** `v{}`
**Your userbot is ready to use!**
"""

clients = []
client_id = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="ctrl1",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=str(string1),
            plugins=dict(root="shin/plugins"),
            in_memory=True
        )
        self.two = Client(
            name="ctrl2",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=str(string2),
            plugins=dict(root="shin/plugins"),
            in_memory=True
        )
        self.three = Client(
            name="ctrl3",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=str(string3),
            plugins=dict(root="shin/plugins"),
            in_memory=True
        )
        self.four = Client(
            name="string4",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=str(string4),
            plugins=dict(root="shin/plugins"),
            in_memory=True
        )
        self.five = Client(
            name="ctrl5",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=str(string5),
            plugins=dict(root="shin/plugins"),
            in_memory=True
        )

    async def start(self):
        LOGGER("Starting").info(f"shin Clients")
        if string1:
            await self.one.start()
            clients.append(1)
            await self.one.join_chat("gcaika")
            await self.one.send_message(
                BOTLOG_CHATID,
                MSG_ON.format("1", __version__),
            )
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            client_id.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER("Client 1").info(
                f"Logged as {self.one.name} [{self.one.id}]"
            )
        if string2:
            await self.two.start()
            await self.two.join_chat("gcaika")
            clients.append(2)
            await self.two.send_message(
                "me",
                MSG_ON.format("2", __version__),
            )
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            client_id.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            LOGGER("Client 2").info(
                f"Logged as {self.two.name} [{self.two.id}]"
            )
        if string3:
            await self.three.start()
            await self.three.join_chat("gcaika")
            clients.append(3)
            await self.three.send_message(
                "me",
                MSG_ON.format("3", __version__),
            )
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            client_id.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            LOGGER("Client 3").info(
                f"Logged as {self.three.name} [{self.three.id}]"
            )
        if string4:
            await self.four.start()
            await self.four.join_chat("gcaika")
            clients.append(4)
            await self.four.send_message(
                "me",
                MSG_ON.format("4", __version__),
            )
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            client_id.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            LOGGER("Client 4").info(
                f"Logged as {self.four.name} [{self.four.id}]"
            )
        if string5:
            await self.five.start()
            await self.five.join_chat("gcaika")
            clients.append(5)
            await self.five.send_message(
                "me",
                MSG_ON.format("5", __version__),
            )
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            client_id.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            LOGGER("Client 5").info(
                f"Logged as {self.five.name} [{self.five.id}]"
            )


class Bot(Client):
    def __init__(self):
        LOGGER("Assistant").info(f"Bot Starting")
        super().__init__(
            name="CtrlUBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=ParseMode.DEFAULT
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER("Assistant").info(f"Bot started {self.name} [{self.id}]")
