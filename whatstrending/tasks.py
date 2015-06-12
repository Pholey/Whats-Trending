from celery import Celery
from slack import api
app = Celery("tasks", broker="redis://localhost")

@app.task
def runSlack():
    while True:
        # Print our recieved messages
        print(api.receive())
