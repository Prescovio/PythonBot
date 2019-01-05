import sys
import traceback
import discord
from Logger import Logger

from discord.ext import commands
from discord.ext.commands import Bot


class MyClient(Bot):
    # general events
    def __init__(self, prefix, description, formatter, pm_help, log_path):
        super().__init__(prefix, formatter, description, pm_help)
        self.add_command(self.test)
        self.logger = Logger(__name__, log_path)

    @commands.command()
    async def test(self, ctx, *args):
        print(ctx)
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

    async def on_connect(self):
        event_name = 'on_connect'
        message = event_name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_ready(self):
        print("on_ready")
        print("Discord version ", discord.version_info)
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------------')
        print('All channels')
        for channel in self.get_all_channels():
            print(channel)

        print('All private channels')
        for private_channel in self.private_channels:
            print(private_channel)

        print('All Members')
        for member in self.get_all_members():
            print(member)

        print('All Users')
        for user in self.users:
            print(user)

        print('All Guilds')
        for guild in self.guilds:
            print(guild)

        print('All Emojis')
        for emoji in self.emojis:
            print(emoji)

        print('All voice clients')
        for voice_client in self.voice_clients:
            print(voice_client)

        print('Activity')
        print(self.activity)
        print('Latency')
        print(self.latency)

        event_name = 'on_ready'
        message = event_name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_resumed(self):
        event_name = 'on_resumed'
        message = event_name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_shard_ready(self, shard_id):
        event_name = 'on_shard_ready'
        message = 'Shard id: ' + shard_id
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_error(self, event, *args, **kwargs):
        print("on_error")
        print(event)
        for arg in args:
            print(arg)

        for kwarg in kwargs:
            print(kwarg, kwargs[kwarg])

        print('Ignoring exception in {}'.format(event), file=sys.stderr)
        traceback.print_exc()

        event_name = 'on_error'
        message = 'Error: ' + str(traceback.print_exc())
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # guild events
    async def on_guild_join(self, guild):
        event_name = 'on_guild_join'
        message = 'Guild: ' + guild.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_remove(self, guild):
        event_name = 'on_guild_remove'
        message = 'Guild: ' + guild.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_update(self, before, after):
        event_name = 'on_guild_update'
        message = 'Before: ' + before.name + ', After: ' + after.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_available(self, guild):
        event_name = 'on_guild_available'
        message = 'Guild: ' + guild.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_unavailable(self, guild):
        event_name = 'on_guild_unavailable'
        message = 'Guild: ' + guild.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_emojis_update(self, guild, before, after):
        event_name = 'on_guild_emojis_update'
        message = 'Guild: ' + guild.name + ', Before: ' + before.name + ', After: ' +  after.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # role events
    async def on_guild_role_create(self, role):
        event_name = 'on_guild_role_create'
        message = 'Role: ' + role.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_role_delete(self, role):
        event_name = 'on_guild_role_delete'
        message = 'Role: ' + role.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_role_update(self, before, after):
        event_name = 'on_guild_role_update'
        message = 'Before: ' + before.name + ' After: ' + after.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # message events
    async def on_message(self, message):
        await super().process_commands(message)
        event_name = 'on_message'
        message = 'Message: ' + message.content + ', Author: ' + message.author.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_message_edit(self, before, after):
        event_name = 'on_message_edit'
        message = ('Before message: ' + before.content + ', After message: ' + after.content +
                   ', Author: ' + before.author)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_message_delete(self, message):
        event_name = 'on_message'
        message = 'Message: ' + message.content + ', Author: ' + message.author
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # raw message events
    async def on_raw_message_edit(self, payload):
        event_name = 'on_raw_message_edit'
        message = 'Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_raw_message_delete(self, payload):
        event_name = 'on_raw_message_delete'
        message = 'Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_raw_bulk_message_delete(self, payload):
        event_name = 'on_raw_bulk_message_delete'
        message = 'Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # reaction events
    async def on_reaction_add(self, reaction, user):
        event_name = 'on_reaction_add'
        message = 'Reaction: ' + reaction + ', User: ' + user
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_reaction_remove(self, reaction, user):
        event_name = 'on_reaction_remove'
        message = 'Reaction: ' + reaction + ', User: ' + user
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_reaction_clear(self, message, reactions):
        event_name = 'on_reactions_clear'
        message = ('Message: ' + message.content + ', Author: ' + message.author + ' - ' +
                   ','.join(reactions))

        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # raw reaction events
    async def on_raw_reaction_add(self, payload):
        event_name = 'on_raw_reaction_add'
        message = 'Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_raw_reaction_remove(self, payload):
        event_name = 'on_raw_reaction_remove'
        message = 'Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_raw_reaction_clear(self, message, reactions):
        event_name = 'on_raw_reaction_clear'
        message = ('Message: ' + message.content + ', Author: ' + message.author + ' - ' +
                   ','.join(reactions))

        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # guild channel events
    async def on_guild_channel_create(self, channel):
        event_name = 'on_private_channel_create'
        message = 'Channel: ' + channel.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_channel_delete(self, channel):
        event_name = 'on_private_channel_delete'
        message = 'Channel: ' + channel.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_channel_update(self, before, after):
        event_name = 'on_guild_channel_update'
        message = 'Before channel: ' + before.name + ', After channel: ' + after.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_guild_channel_pins_update(self, channel, last_pin):
        event_name = 'on_guild_channel_pins_update'
        message = 'Channel: ' + channel.name + ', Last pin: ' + last_pin
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # private channel events
    async def on_private_channel_create(self, channel):
        event_name = 'on_private_channel_create'
        message = 'Channel: ' + channel.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_private_channel_delete(self, channel):
        event_name = 'on_private_channel_delete'
        message = 'Channel: ' + channel.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_private_channel_update(self, before, after):
        event_name = 'on_private_channel_update'
        message = 'Before channel: ' + before.name + ', After channel: ' + after.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_private_channel_pins_update(self, channel, last_pin):
        event_name = 'on_private_channel_pins_update'
        message = 'Channel: ' + channel.name + ', Last pin: ' + last_pin
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # member events
    async def on_member_join(self, member):
        event_name = 'on_member_join'
        message = 'Member: ' + member.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_member_remove(self, member):
        event_name = 'on_member_remove'
        message = 'Member: ' + member.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_member_update(self, before, after):
        event_name = 'on_member_update'
        message = 'Member before: ' + before.name + ', Member after: ' + after.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_voice_state_update(self, member, before, after):
        event_name = 'on_voice_state_update'
        message = 'Member: ' + member + ', Before: ' + before + ', After: ' + after
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_member_ban(self, guild, user):
        event_name = 'on_member_ban'
        message = 'Guild: ' + guild.name + ', User: ' + user.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_member_unban(self, guild, user):
        event_name = 'on_member_unban'
        message = 'Guild: ' + guild.name + ', User: ' + user.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_typing(self, channel, user, when):
        event_name = 'on_typing'
        message = 'Channel: ' + channel.name + ', User: ' + user.name + ', at: ' + str(when)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_group_join(self, channel, user):
        event_name = 'on_group_join'
        message = 'Channel: ' + channel.name + ', User: ' + user.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_group_remove(self, channel, user):
        event_name = 'on_group_remove'
        message = 'Channel: ' + channel.name + ', User: ' + user.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # relationship events
    async def on_relationship_add(self, relationship):
        event_name = 'on_relationship_add'
        message = ('Relationship type: ' + relationship.type +
                   ', Relationship user: ' + relationship.user)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_relationship_remove(self, relationship):
        event_name = 'on_relationship_remove'
        message = ('Relationship type: ' + relationship.type +
                   ', Relationship user: ' + relationship.user)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_relationship_update(self, before, after):
        event_name = 'on_relationship_update'
        message = ('Before type: ' + before.type + ', Before user: ' + before.user +
                   ', After type: ' + after.type + ', After user: ' + after.user)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # socket events
    async def on_socket_raw_receive(self, payload):
        event_name = 'on_socket_raw_receive'
        message = event_name + ' fired - Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_socket_raw_send(self, payload):
        event_name = 'on_socket_raw_send'
        message = event_name + ' fired - Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # webhook events
    async def on_webhooks_update(self, channel):
        event_name = 'on_webhooks_update'
        message = event_name + ' fired - Channel: ' + channel.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)
