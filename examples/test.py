import os
import random
import json
# Pycordを読み込む
import discord
import dotenv

# アクセストークンを設定
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "〇〇をプレイ中"の"〇〇"を設定,
)

# 起動時に自動的に動くメソッド
@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("Hello!")

# pingコマンドを実装
@bot.command(name="ping", description="pingを返します")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"pong to {ctx.author.mention}")

# 2つ前に送信された自分のメッセージを編集する
@bot.command(name="edit", description="1つ前の自分のメッセージを編集します")
async def edit(ctx: discord.ApplicationContext):
    async for message in ctx.channel.history(limit=2):
        if message.author == bot.user:
            await message.edit(content=f"{message.content}編集しました")

# Botを起動
bot.run(token)
