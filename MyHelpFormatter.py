from discord.ext.commands import HelpFormatter


class MyHelpFormatter(HelpFormatter):
    def __init__(self):
        super().__init__(True, True, 80)
