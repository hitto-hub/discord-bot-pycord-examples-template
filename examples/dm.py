# discord.pyの大事な部分をimport
import dotenv
import os
import discord

# デプロイ先の環境変数にトークンをおいてね
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
    print("Hello!")  # コマンドラインにHello!と出力

#送信者にDMを返す
@bot.command()
async def dm(ctx: discord.ApplicationContext):
    await ctx.author.send("Direct Message!!")

# 起動
bot.run(token)