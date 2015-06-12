from .slack import SlackAPI
from whatstrending import settings

api = SlackAPI(settings.SLACK_ACCESS_TOKEN)

__all__ = [
    "api"
]
