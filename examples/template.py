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


# 起動
bot.run(token)