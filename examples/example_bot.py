# このボットは、Discordのチャットで「$hello」と入力すると
# 「Hello!」と返すだけのボットです。

# import
import os
import dotenv
import discord
# 環境変数を設定
dotenv.load_dotenv()
# アクセストークンを設定
token = str(os.getenv("TOKEN"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)
