from twitter import api

from twitter.interface import get_user_tweets
from AI import brain
from tasks import runSlack

# Init our worker
runSlack.delay()

brain.train(["foo"])

print(brain.get_response("bar"))
