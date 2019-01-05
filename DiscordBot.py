import json

from MyClient import MyClient
from MyHelpFormatter import MyHelpFormatter

with open('config.json', 'r') as f:
    config = json.load(f)

prefix = config['DEFAULT']['PREFIX']
description = config['DEFAULT']['DESCRIPTION']
pm_help = config['DEFAULT']['PM_HELP']
log_path = config['DEFAULT']['LOG_PATH']

help_formatter = MyHelpFormatter()
bot = MyClient(prefix, description, help_formatter, pm_help, log_path)

bot.run('NTI3OTk3MDQ3MjgzMTIyMjI2.DwfTyA.Nmjz-2oGd4bxmTsZ3lSj3EMUhyk')
