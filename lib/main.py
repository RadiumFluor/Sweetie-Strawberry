import discord

class Main(discord.Client):
    async def on_ready(self):
        print('Conexão estabelecida como {0}!' .format(self.user))

client = Main()