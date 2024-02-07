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

# メッセージ編集時に発動(編集前(before)と後(after)のメッセージを送信)
@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    txt = f"{before.author} がメッセージを編集しました！\nbefore:```{before.content}```\nafter:```{after.content}```"
    # リアクションをつける
    await after.add_reaction("✅")
    await before.channel.send(txt)

# メッセージ削除時に発動(削除されたメッセージを送信)
@bot.event
async def on_message_delete(message: discord.Message):
    txt = f"{message.channel}:{message.author} がメッセージを削除しました！\n```{message.content}```"
    # DMに送信
    await message.author.send(txt)
    # チャンネルに送信
    await message.channel.send(txt)

# 誰かがメッセージ入力中に発動(XXが入力中です……のとき)
@bot.event
async def on_typing(channel: discord.TextChannel, user,when):
    txt=f"{user} がメッセージを入力しています！"
    await channel.send(txt)


# 起動
bot.run(token)