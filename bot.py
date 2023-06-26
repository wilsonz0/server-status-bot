import discord
import responses
from discord.ext import tasks
from config import TOKEN 

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        # send_update.start()


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        # send_update.stop()
        
        username = str(message.author)
        user_message = str(message.content)

        print(f'{username} said "{user_message}"')

        if user_message == '!startLoop':
            send_update.start()
        elif user_message == '!endLoop':
            send_update.stop()
        elif user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @tasks.loop(minutes=30)
    async def send_update():
        response = responses.get_response("!getstatus")
        print(response)


    client.run(TOKEN)

