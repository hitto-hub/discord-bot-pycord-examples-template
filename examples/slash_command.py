# このボットは、Discordのスラッシュコマンドを使って、
# 「/hello」と入力すると「Hello!」と返すだけのボットです。
# guild_ids=[1164754195535102112]は、このスラッシュコマンドを使えるサーバーを指定しています。
# また、example_bot.pyで使用されているdiscord.Client()と違い、discord.Bot()を使用して、Bot のインスタンスを作成します。
# これは Client とは異なり、Client のすべての機能を継承しながら、スラッシュ コマンドの作成やその他の機能をサポートします。

import os
import dotenv
import discord
# アクセストークンを設定
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
guild_id = str(os.getenv("GUILD_ID"))

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[guild_id])
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello!")

bot.run(token)
