import discord
from discord.ext import commands
from discord import SlashCommandGroup, Option, SlashCommandOptionType

# main.pyで読み込ませるためのCogを継承したクラスを作成します。
class SubCog(commands.Cog):
    def __init__(self, bot):
        print("start sub init")
        self.bot = bot

    # comというコマンドグループを定義します
    com = SlashCommandGroup("com", "comコマンドのグループ")

    # comというコマンドグループにhelloコマンドを定義します
    @com.command(name="hello", description="挨拶するだけのコマンド")
    async def hello(
        self,
        ctx: discord.ApplicationContext,
        # name引数を受け取る様に設定します。
        name: Option(
            str,
            description="引数の説明",
        )
    ):
        # 引数の段階だと型がstr型かわかりにくいので注釈をつけてます
        name: str = name
        # 名前にさんづけしてこんにちはするだけの処理
        await ctx.response.send_message(f"{name}さん、こんにちは！")

# main.pyのload_extensionsのが実行する実際の関数を定義します
def setup(bot):
    bot.add_cog(SubCog(bot)) #add_cog関数にSubCogのインスタンスを渡します
