import json
import traceback

from MyClient import MyClient
from MyHelpCommand import MyHelpCommand

with open('config.json', 'r') as f:
    config = json.load(f)

prefix = config['GENERAL']['PREFIX']
description = config['GENERAL']['DESCRIPTION']
pm_help = config['GENERAL']['PM_HELP']
log_path = config['GENERAL']['LOG_PATH']

help_command = MyHelpCommand()
bot = MyClient(prefix, description, pm_help, help_command, log_path)

try:
    bot.run('NTI3OTk3MDQ3MjgzMTIyMjI2.DwfTyA.Nmjz-2oGd4bxmTsZ3lSj3EMUhyk')
except Exception as error:
    exception = type(error)
    message = 'Unexpected exception, traceback: {}'.format(str(traceback.print_exc()))
    bot.logger.log(message=message, file_name=exception, directory=exception)
