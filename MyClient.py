import sys
import traceback
import discord

from discord.ext import commands
from discord.ext.commands import Bot


class MyClient(Bot):
    # general events
    def __init__(self, prefix, description, formatter, pm_help):
        super(MyClient, self).__init__(prefix, formatter, description, pm_help)
        self.add_command(self.test)

    @commands.command()
    async def test(self, ctx, *args):
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

    async def on_connect(self):
        print("on_connect")

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

    async def on_resumed(self):
        print('on_resumed')

    async def on_shard_ready(self, shard_id):
        print("on_shard_ready")

    async def on_error(self, event, *args, **kwargs):
        print("on_error")
        print(event)
        for arg in args:
            print(arg)

        for kwarg in kwargs:
            print(kwarg, kwargs[kwarg])

        print('Ignoring exception in {}'.format(event), file=sys.stderr)
        traceback.print_exc()

    # guild events
    async def on_guild_join(self, guild):
        print("on_guild_join")

    async def on_guild_remove(self, guild):
        print("on_guild_remove")

    async def on_guild_update(self, before, after):
        print("on_guild_update")

    async def on_guild_available(self, guild):
        print("on_guild_available")

    async def on_guild_unavailable(self, guild):
        print("on_guild_unavailable")

    async def on_guild_emojis_update(self, guild, before, after):
        print("on_guild_emojis_update")

    # role events
    async def on_guild_role_create(self, role):
        print("on_guild_role_create")

    async def on_guild_role_delete(self, role):
        print("on_guild_role_delete")

    async def on_guild_role_update(self, before, after):
        print("on_guild_role_update")

    # message events
    async def on_message(self, message):
        await super().process_commands(message)
        print("on_message")

    async def on_message_edit(self, before, after):
        print("on_message_edit")

    async def on_message_delete(self, message):
        print("on_message_delete")

    # raw message events
    async def on_raw_message_edit(self, payload):
        print("on_raw_message_edit")

    async def on_raw_message_delete(self, payload):
        print("on_raw_message_delete")

    async def on_raw_bulk_message_delete(self, payload):
        print("on_raw_bulk_message_delete")

    # reaction events
    async def on_reaction_add(self, reaction, user):
        print("on_reaction_add")

    async def on_reaction_remove(self, reaction, user):
        print("on_reaction_remove")

    async def on_reaction_clear(self, message, reactions):
        print("on_reaction_clear")

    # raw reaction events
    async def on_raw_reaction_add(self, payload):
        print("on_raw_reaction_add")

    async def on_raw_reaction_remove(self, padload):
        print("on_raw_reaction_remove")

    async def on_raw_reaction_clear(self, message, reactions):
        print("on_raw_reaction_clear")

    # guild channel events
    async def on_guild_channel_create(self, channel):
        print("on_guild_channel_create")

    async def on_guild_channel_delete(self, channel):
        print("on_guild_channel_delete")

    async def on_guild_channel_update(self, before, after):
        print("on_guild_channel_update")

    async def on_guild_channel_pins_update(self, channel, last_pin):
        print("on_guild_channel_pins_update")

    # private channel events
    async def on_private_channel_create(self, channel):
        print("on_private_channel_create")

    async def on_private_channel_delete(self, channel):
        print("on_private_channel_celete")

    async def on_private_channel_update(self, before, after):
        print("on_private_channel_update")

    async def on_private_channel_pins_update(self, channel, last_pin):
        print("on_private_channel_pins_update")

    # member events
    async def on_member_join(self, member):
        print("on_member_join")

    async def on_member_remove(self, member):
        print("on_member_remove")

    async def on_member_update(self, before, after):
        print("on_member_update")

    async def on_voice_state_update(self, member, before, after):
        print("on_voice_state_updated")

    async def on_member_ban(self, guild, user):
        print("on_member_join")

    async def on_member_unban(self, guild, user):
        print("on_member_unban")

    async def on_typing(self, channel, user, when):
        print("on_typing")

    async def on_group_join(self, channel, user):
        print("on_group_join")

    async def on_group_remove(self, channel, user):
        print("on_group_remove")

    # relationship events
    async def on_relationship_add(self, relationship):
        print("on_relationship_add")

    async def on_relationship_remove(self, relationship):
        print("on_relationship_remove")

    async def on_relationship_update(self, before, after):
        print("on_relationship_update")

    # socket events
    async def on_socket_raw_receive(self, message):
        print("on_socket_raw_receive")

    async def on_socket_raw_send(self, payload):
        print("on_socket_raw_send")

    # webhook events
    async def on_webhooks_update(self, channel):
        print("on_webhooks_update")
