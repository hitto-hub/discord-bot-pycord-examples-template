import os
# Pycordを読み込む
import discord
import dotenv
from discord.ext import commands,tasks
import time

# アクセストークンを設定
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

# gasurl
gasurl = str(os.getenv("GASURL"))
url = gasurl

# channelid
channelid = str(os.getenv("CHANNELID"))

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
    for channel in bot.get_all_channels():
        if int(channel.id) == int(channelid):
            now = time.localtime()
            mes = "```" + time.strftime("%Y/%m/%d %H:%M:%S", now) + ":起動しました\n```"
            await channel.send(mes)

# pingコマンドを実装
@bot.command(name="ping", description="pingを返します")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"pong to {ctx.author.mention}")

# 1つ前に送信された自分のメッセージを編集する
@bot.command(name="edit", description="1つ前の自分のメッセージを編集します")
async def edit(ctx: discord.ApplicationContext):
    async for message in ctx.channel.history(limit=2):
        if message.author == bot.user:
            await message.edit(content="編集しました")

# 10秒ごとにchannelidにメッセージを送信
@tasks.loop(seconds=1)
async def log_get():
    # 完全に起動するまで待つ
    await bot.wait_until_ready()
    # channel指定 要改善
    for channel in bot.get_all_channels():
        if int(channel.id) == int(channelid):
            # メッセージ指定 要改善
            async for message in channel.history(limit=1):
                # 自分のメッセージのみを編集
                if message.author == bot.user:
                    mes = message.content[:-3]
                    now = time.localtime()
                    mes = mes + time.strftime("%Y/%m/%d %H:%M:%S", now) + "\n```"
                    await message.edit(content=f"{mes}")

log_get.start()

# Botを起動
bot.run(token)
