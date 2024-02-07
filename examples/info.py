# 参考: discord.pyスターターキット
# https://qiita.com/Chroma7p/private/ff1402746803f6e0aa06

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
    print("Hello!")  # コマンドラインにHello!と出力

#ctx.authorでコマンド送信者の情報が取れる
@bot.command()
async def info(ctx: discord.ApplicationContext):
    info=f"this guild:{ctx.guild}\n"
    info+=f"this channel:{ctx.channel}\n"
    info+=f"your user id:{ctx.author.id}\n"
    info+=f"your user name:{ctx.author}"
    await ctx.send(info)

# 起動
bot.run(token)