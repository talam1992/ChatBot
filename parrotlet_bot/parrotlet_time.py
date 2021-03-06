__author__ = 'Timothy Lam'

import datetime
import time
import trans_
import config


def parrotlet_time():
    _time = str(datetime.datetime.now()).split()[1].split('.')[0]
    reply = f'The Time is {_time}'
    if config.lang_code != 'en':
        reply = trans_.translate_sentence_code(reply, config.lang_code)
        config.lang_code = 'en'
    return reply


def parrotlet_date():
    return time.ctime()
