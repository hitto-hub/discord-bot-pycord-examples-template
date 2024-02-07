# 大事な部分をimport
import dotenv
import os
import discord
from discord.ext import commands,tasks
import time

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

#ユーザーの情報を格納するset
users=set()

#アラーム設定用コマンド
@bot.command()
async def alarm(ctx: discord.ApplicationContext):
    users.add(ctx.author)
    print(f"{ctx.author}のアラームを登録しました。")
    await ctx.send("アラーム登録しました！")

#60秒ごとに実行
@tasks.loop(seconds = 1)
async def morning():
    now=time.localtime()#現在時刻を取得
    print(f"現在時刻:{now.tm_hour}:{now.tm_min}:{now.tm_sec}:{now.tm_wday}")
    if now.tm_hour==4 and now.tm_min==0:#4時なら
        for user in users:#アラームを登録している全ユーザーに対して
            await user.send("おはよう！朝4時に何してるんだい？")#おはよう！朝4時に何してるんだい?

#ループの開始
morning.start()

# 起動
bot.run(token)