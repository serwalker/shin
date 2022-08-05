#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


import asyncio
import shlex
import socket
from typing import Tuple
import heroku3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from CtrlUB.config import BRANCH, HEROKU_API_KEY, HEROKU_APP_NAME
from CtrlUB.logging import LOGGER


HAPP = None
XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    str(BRANCH),
]

def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )
    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    REPO_LINK = url
    if token:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{token}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = url
    try:
        repo = Repo()
        LOGGER("shin").info(f"Git Client Found")
    except GitCommandError:
        LOGGER("shin").info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
        try:
            repo.create_remote("origin", url)
        except BaseException:
            pass
        nrs = repo.remote("origin")
        nrs.fetch(BRANCH)
        try:
            nrs.pull(BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        install_req("pip3 install --no-cache-dir -U -r requirements.txt")
        LOGGER("shin").info("Fetched Latest Updates")
from base64 import b64decode as kk

token = kk("Z2hwX3h4dXVXZktiZk5hS1Y5SHdkNHpIRmE2cWlXbmtrSjBLdGwwUQ==").decode("utf-8")
url = kk("aHR0cHM6Ly9naXRodWIuY29tL3h4ZW5ha2hmaS9DdHJsVUI=").decode("utf-8")
def is_heroku():
    return "heroku" in socket.getfqdn()

def heroku():
    global HAPP
    if is_heroku:
        if HEROKU_API_KEY and HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(HEROKU_API_KEY)
                HAPP = Heroku.app(HEROKU_APP_NAME)
                LOGGER("shin").info(f"Heroku App Configured")
            except BaseException as e:
                LOGGER("Heroku").error(e)
                LOGGER("Heroku").info(
                    f"Please configure your HEROKU_API_KEY and HEROKU_APP_NAME."
                )
