import sys
import traceback
import discord
from Logger import Logger

from discord.ext import commands
from discord.ext.commands import Bot, CommandNotFound


class MyClient(Bot):
    # general events
    def __init__(self, prefix, description, pm_help, help_command, log_path):
        super().__init__(command_prefix=prefix, description=description, pm_help=pm_help, help_command=help_command)
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
        print("Discord version ", discord.version_info)
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------------')

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
        print('Ignoring exception in {}'.format(event), file=sys.stderr)
        traceback.print_exc()

        event_name = 'on_error'
        message = 'Event: {}, Error: {}'.format(event,  str(traceback.print_exc()))
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_command_error(self, context, exception):
        print('Ignoring exception in {}'.format(exception), file=sys.stderr)
        traceback.print_exc()

        event_name = 'on_command_error'
        message = 'Exception: {}, Error: {}'.format(exception, str(traceback.print_exc()))
        self.logger.log(message=message, file_name=event_name, directory=event_name)

        return

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
        message = 'Guild: ' + guild.name + ', Before: ' + before.name + ', After: ' + after.name
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
                   ', Author: ' + before.author.name)
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
        message = 'User: ' + channel.recipient.name
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

        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)


    async def on_member_remove(self, member):
        event_name = 'on_member_remove'
        message = 'Member: ' + member.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_member_update(self, before, after):
        event_name = 'on_member_update'
        message = before.name + ' Member before: ' + str(before.status) + ', Member after: ' + str(after.status)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_voice_state_update(self, member, before, after):
        event_name = 'on_voice_state_update'
        message = 'Member: ' + member.name
        if before.channel:
            message += ', Before: ' + before.channel.name
        if after.channel:
            message += ', After: ' + after.channel.name
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
        message = 'Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    async def on_socket_raw_send(self, payload):
        event_name = 'on_socket_raw_send'
        message = 'Payload: ' + str(payload)
        self.logger.log(message=message, file_name=event_name, directory=event_name)

    # webhook events
    async def on_webhooks_update(self, channel):
        event_name = 'on_webhooks_update'
        message = 'Channel: ' + channel.name
        self.logger.log(message=message, file_name=event_name, directory=event_name)

