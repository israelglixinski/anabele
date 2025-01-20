from datetime import datetime
import os

current_directory = os.path.dirname(os.path.abspath(__file__))    

def log_register(text=''):
    yyyymmdd = datetime.now().strftime('%Y%m%d')
    datetimestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(f'{current_directory}\\logs\\autocommits\\{yyyymmdd}', 'a') as file:
        file.write(f'{datetimestamp} - {text}\n')
    pass
