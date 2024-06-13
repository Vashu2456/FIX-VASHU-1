import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25581940"))
    API_HASH = os.environ.get("API_HASH", "1e80acd755ceab02b3e2a22d49b25c18")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7148375527:AAGn7ctUxdL-hM_YJUiTmFrc18zGEnpYAIA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQHAwxwAgsWyJTtsFXYr-RjZOA_pg-xtVwioD8s1lDs1d4W1gKTxToMQyeWBrsDmW1sr7TWj5aXGOFdhn9VwiYlMKGsfr9JuWZwy6sz_KkI2Vk6hS5u2Vnnowpy-_XHqqi7PCMZSBb0IEj03VJdpoKnKNqYa3rKbT_3sdmjHzNUTQyL-haralF2P8GfA4JLscfHNxgv9u2erNr8o6_LUOqf0F9lyUkmMsIL9oWNQC7oh4pXIwsdETNmgvGmZs6f6-RfZkdox6d3CgEEo3EbF2LFVfM1AmGc2riTnXPn7ZGqnLwtie2w5Lg0jMJf4lyMu8jrTxnGOqPblTpQC9oLbnoZ6gIk_KAAAAAGVW2_yAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@FIXER_X_BOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
