from datetime import datetime
from threading import Thread
from time import sleep
import obtaining_data
import autocommits
import common

last_execute = None
last_quote = None

def execute_routine():
    global last_quote, last_execute
    current_quote = obtaining_data.get_dollar_quote()
    common.log_register(f'The current dollar exchange rate: R$ {current_quote:.2f}')
    if last_quote is None or current_quote != last_quote:
        last_quote = current_quote
        repository_path = "C:\\Projetos\\git_duplo\\anabele"
        commit_message = "Log update"
        autocommits.git_commit(repository_path, commit_message)

def execute_routine_thread():
    global last_quote, last_execute
    while True:
        if last_execute is None or (datetime.now() - last_execute).seconds >= 3600:
            last_execute = datetime.now()
            execute_routine()
        sleep(60)

Thread(target=execute_routine_thread).start()
