from discord.ext.commands import DefaultHelpCommand


class MyHelpCommand(DefaultHelpCommand):
    def __init__(self):
        super().__init__()
