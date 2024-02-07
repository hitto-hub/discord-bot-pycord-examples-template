# on_readyでbotが起動したときにHello!と出力するコード。
# /helloコマンドでHello!とメッセージを送信する。
# /editコマンドでHello!というメッセージを送信しWorld"を追記編集する。

# 大事な部分をimport
import dotenv
import os
import discord

# アクセストークンを設定
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

# オブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "〇〇をプレイ中"の"〇〇"を設定,
)

# イベントを検知
@bot.event
# botの起動が完了したとき
async def on_ready():
    print("Hello!")

# /helloコマンドでHello!とメッセージを送信する。
@bot.command()
async def hello(ctx: discord.ApplicationContext):
    await ctx.send("Hello!")

# /editコマンドでHello!というメッセージをWorldに編集する。
@bot.command()
async def edit(ctx: discord.ApplicationContext):
    msg = await ctx.send("Hello!")
    await msg.edit(content=f"{msg.content} World!")

# 2つ前に送信された自分のメッセージを編集する
@bot.command(name="edit2", description="1つ前の自分のメッセージを編集します")
async def edit2(ctx: discord.ApplicationContext):
    async for message in ctx.channel.history(limit=2):
        if message.author == bot.user:
            await message.edit(content=f"{message.content}編集しました")

# 起動
bot.run(token)