from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

CHANNEL = int(os.getenv("CHANNEL"))
GREETINGS = int(os.getenv("GREETINGS"))
TEST =  int(os.getenv("TEST"))
CARD = int(os.getenv("CARD"))
PUBLIC_MSG = int(os.getenv("PUBLIC_MSG"))
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
ONE_TIME_TXT = os.getenv("ONE_TIME_TXT")
QUICK_TXT = os.getenv("QUICK_TXT")