from datetime import datetime as dt
import os
import threading

def log(what, message):
    t = threading.Thread(target=WriteLogFile, args=(what, message,))
    t.start()

def WriteLogFile(what, message):
# функция для записи лога
    dir_log = "log"
    if not os.path.exists(dir_log):
        os.mkdir(dir_log)
    with open(f'{dir_log}/{dt.now():%d.%m.%Y}.log', 'a', encoding='utf-8') as f_obj:
        string = what + ':' + str(dt.now())[0:19] + ': ' + message + '\n'
        f_obj.write(string)