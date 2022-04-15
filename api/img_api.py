from dotenv import load_dotenv
load_dotenv()
import os
import json

def appID():
    return json.load(os.environ.get("WOLFRAM_API_APPID"))