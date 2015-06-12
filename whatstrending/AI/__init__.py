from whatstrending import settings
from chatterbot import ChatBot
# from chatterbot.adapters.storage import MongoDatabaseAdapter

# TODO(pholey): Get MongoDatabaseAdapter up and running
# brain = ChatBot(settings.BOT_NAME, storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter")
brain = ChatBot(settings.BOT_NAME)


__all__ = [
    'brain'
]
