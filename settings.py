import os
from os.path import join, dirname
from dotenv import load_dotenv

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

IRC_TOKEN = os.environ.get("IRC_TOKEN")
CLIENT_ID = os.environ.get("CLIENT_ID")
NICK = os.environ.get("NICK")
PREFIX = os.environ.get("PREFIX")
INITIAL_CHANNELS = os.environ.get("INITIAL_CHANNELS")
