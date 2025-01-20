from datetime import datetime
from time import sleep
import orchestrator

last_execute = None

while True:
    if last_execute is None or (datetime.now() - last_execute).seconds >= 3600:
        last_execute = datetime.now()
        orchestrator.execute_routine()
    sleep(60)
    pass