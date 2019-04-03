import json
import traceback

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

try:
    bot.run('NTI3OTk3MDQ3MjgzMTIyMjI2.DwfTyA.Nmjz-2oGd4bxmTsZ3lSj3EMUhyk')
except Exception as error:
    exception = type(error)
    message = 'Unexpected exception, traceback: {}'.format(str(traceback.print_exc()))
    bot.logger.log(message=message, file_name=exception, directory=exception)
