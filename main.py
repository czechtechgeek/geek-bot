#geekbot

from twitchio.ext import commands
import settings as CR

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=CR.IRC_TOKEN, 
                         client_id=CR.CLIENT_ID, 
                         nick=CR.NICK, 
                         prefix=CR.PREFIX,
                         initial_channels=[CR.INITIAL_CHANNELS])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()