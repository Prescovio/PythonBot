import json

from MyClient import MyClient
from MyHelpFormatter import MyHelpFormatter

with open('config.json', 'r') as f:
    config = json.load(f)

prefix = config['GENERAL']['PREFIX']
description = config['GENERAL']['DESCRIPTION']
pm_help = config['GENERAL']['PM_HELP']
log_path = config['GENERAL']['LOG_PATH']

help_formatter = MyHelpFormatter()
bot = MyClient(prefix, description, help_formatter, pm_help, log_path)

bot.run('NTI3OTk3MDQ3MjgzMTIyMjI2.DwfTyA.Nmjz-2oGd4bxmTsZ3lSj3EMUhyk')
