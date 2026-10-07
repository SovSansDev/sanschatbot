import discord
from discord.ext import commands
import google.generativeai as genai

# Konfigurasi API Gemini
genai.configure(api_key="AQ.Ab8RN6LXKHuw82grbLxaNRECXPDJe32Duxzwc78SJ_O1YpagJg")
model = genai.GenerativeModel('gemini-1.5-flash')

# Setup Bot Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Login berhasil sebagai {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Kalau bot di-mention, balas pakai Gemini
    if bot.user.mentioned_in(message):
        user_message = message.content.replace(f'<@{bot.user.id}>', '').strip()
        
        if user_message:
            async with message.channel.typing():
                try:
                    response = model.generate_content(user_message)
                    await message.reply(response.text)
                except Exception as e:
                    await message.reply(f"Duh, error bro: {e}")

# Jalankan Bot menggunakan Token Discord
bot.run("MTU1NzMyOTc5NjY3NjE5NDM0NA.GcqOVN.AFxZAiRV43zAC5Bo1UToipMRarSTrDxZ7h
apH8")
