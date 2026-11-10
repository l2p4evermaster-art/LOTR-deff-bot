
____________
Nanic wrote:

import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot je online: {bot.user}")

@bot.tree.command(name="defcall", description="Napravi novi DEF CALL")
@app_commands.describe(
    selo="Ime sela i koordinate",
    vrijeme="Vrijeme udara",
    potreba="Koliko defa je potrebno"
)
async def defcall(
    interaction: discord.Interaction,
    selo: str,
    vrijeme: str,
    potreba: str
):
    embed = discord.Embed(
        title="🛡️ TRAVIAN DEF CALL",
        color=discord.Color.red()
    )
    embed.add_field(name="🏰 Selo", value=selo)
    embed.add_field(name="⏰ Vrijeme udara", value=vrijeme)
    embed.add_field(name="⚔️ Potreban DEF", value=potreba)
    embed.set_footer(text="Travian Alliance DEF System")

    await interaction.response.send_message(embed=embed)

bot.run("OVDJE_IDE_TVOJ_TOKEN")