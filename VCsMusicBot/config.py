import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("config.py"):
    load_dotenv("config.py")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = "5837427920:AAEHQ8DYhGiTusz2rpz6s_T6BlD9lJKQZ4M"
BOT_NAME = "𝑫𝑬𝑵𝑨𝑹"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tgbotproject")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = "29699592"
API_HASH = "36c5d87a0d72b145a014b89def282cbd"
BOT_USERNAME = "D3NARBOT"
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = "https://github.com/vxl3/VCsMusicBot"
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
