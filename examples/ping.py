# このボットは、pingコマンドを実装したサンプルコードです。
# このコードを実行すると、pingコマンドが使えるBotが起動します。
# pingコマンドを実行すると、Botが「pong to @ユーザー名」とreplyを返します。

import os
import dotenv
import discord
# アクセストークンを設定
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
    intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
    activity=discord.Game("ping"),  # Botのステータスメッセージを設定
)

# 起動時に自動的に動くメソッド
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# pingコマンドを実装
@bot.slash_command(name="ping", description="pingを返します")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"pong to {ctx.author.mention}")

# Botを起動
bot.run(token)
