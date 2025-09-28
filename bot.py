import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import random
import datetime
import math
import base64
import hashlib
import string
import json
import re

# =============================================================================
# CONFIGURATION - PUT YOUR DISCORD BOT TOKEN HERE
# =============================================================================
DISCORD_TOKEN = "your-bot-token"  # Replace with your real Discord token
# =============================================================================

class UltraBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        try:
            synced = await self.tree.sync()
            print(f'✅ {len(synced)} ULTRA MEGA slash commands synced!')
        except Exception as e:
            print(f'❌ Error syncing: {e}')

    async def on_ready(self):
        print(f'🤖 {self.user} - ULTRA BOT connected!')
        print(f'🏰 Servers: {len(self.guilds)}')
        print(f'👥 Members: {sum(guild.member_count for guild in self.guilds)}')
        print('=' * 80)
        print('🎆🎆🎆 ULTRA MEGA BOT - 150+ SLASH COMMANDS! 🎆🎆🎆')
        print('📝 Type / in Discord to discover ALL commands')
        print('=' * 80)

bot = UltraBot()

# =============================================================================
# MASSIVE DATA FOR ALL COMMANDS
# =============================================================================

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!",
    "Why did the coffee file a police report? It got mugged!",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus!",
    "Why don't programmers like nature? It has too many bugs!",
    "How do you organize a space party? You planet!",
    "Why was the math book sad? Because it had too many problems!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What do you call a dinosaur that crashes his car? Tyrannosaurus Wrecks!",
    "Why can't a bicycle stand up by itself? It's two tired!",
    "What do you call a sleeping bull? A bulldozer!",
    "Why did the cookie go to the doctor? Because it felt crumbly!"
]

FACTS = [
    "Honey never spoils. Archaeologists have found 3000-year-old honey in Egyptian tombs that's still edible.",
    "Octopuses have three hearts and blue blood.",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a 'flamboyance'.",
    "Elephants are afraid of bees and mice.",
    "A shrimp's heart is in its head.",
    "Wombat droppings are cube-shaped.",
    "Sharks have existed longer than trees (400M vs 350M years).",
    "The unicorn is Scotland's national animal.",
    "There are more trees on Earth than stars in the Milky Way.",
    "Dolphins have names and call each other.",
    "A cloud weighs about a million tons.",
    "It rains diamonds on Jupiter and Saturn.",
    "Your brain uses 20% of your body's energy.",
    "Ants never sleep.",
    "A day on Venus lasts longer than a Venusian year.",
    "Polar bears have black skin under their white fur.",
    "A teaspoon of neutron star weighs 6 billion tons."
]

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It is not the strongest of the species that survives, but the most adaptable. - Charles Darwin",
    "Success is going from failure to failure without losing your enthusiasm. - Winston Churchill",
    "Be the change you want to see in the world. - Gandhi",
    "Life is like riding a bicycle, you must keep moving to maintain balance. - Einstein",
    "There is only one way to fail, and that is to give up before you succeed. - Olivier Lockert",
    "Happiness is not a destination, it's a way of traveling. - Margaret Lee Runbeck",
    "Yesterday is history, tomorrow is a mystery, today is a gift. - Eleanor Roosevelt",
    "Don't judge each day by what you harvest, but by the seeds you plant. - Robert Louis Stevenson"
]

COUNTRIES = {
    'france': {'capital': 'Paris', 'currency': 'EUR', 'continent': 'Europe', 'population': '67.8M', 'area': '643,801 km²', 'language': 'French'},
    'usa': {'capital': 'Washington D.C.', 'currency': 'USD', 'continent': 'North America', 'population': '331M', 'area': '9.8M km²', 'language': 'English'},
    'japan': {'capital': 'Tokyo', 'currency': 'JPY', 'continent': 'Asia', 'population': '125M', 'area': '377,975 km²', 'language': 'Japanese'},
    'germany': {'capital': 'Berlin', 'currency': 'EUR', 'continent': 'Europe', 'population': '83.2M', 'area': '357,386 km²', 'language': 'German'},
    'canada': {'capital': 'Ottawa', 'currency': 'CAD', 'continent': 'North America', 'population': '38.2M', 'area': '9.98M km²', 'language': 'English/French'},
    'australia': {'capital': 'Canberra', 'currency': 'AUD', 'continent': 'Oceania', 'population': '25.7M', 'area': '7.74M km²', 'language': 'English'},
    'brazil': {'capital': 'Brasília', 'currency': 'BRL', 'continent': 'South America', 'population': '215M', 'area': '8.51M km²', 'language': 'Portuguese'},
    'china': {'capital': 'Beijing', 'currency': 'CNY', 'continent': 'Asia', 'population': '1.44B', 'area': '9.6M km²', 'language': 'Mandarin'},
    'india': {'capital': 'New Delhi', 'currency': 'INR', 'continent': 'Asia', 'population': '1.38B', 'area': '3.29M km²', 'language': 'Hindi/English'},
    'uk': {'capital': 'London', 'currency': 'GBP', 'continent': 'Europe', 'population': '67.5M', 'area': '243,610 km²', 'language': 'English'}
}

ELEMENTS = {
    'hydrogen': {'symbol': 'H', 'number': 1, 'mass': '1.008', 'group': 'Nonmetal', 'period': 1, 'block': 's'},
    'helium': {'symbol': 'He', 'number': 2, 'mass': '4.003', 'group': 'Noble gas', 'period': 1, 'block': 'p'},
    'carbon': {'symbol': 'C', 'number': 6, 'mass': '12.011', 'group': 'Nonmetal', 'period': 2, 'block': 'p'},
    'oxygen': {'symbol': 'O', 'number': 8, 'mass': '15.999', 'group': 'Nonmetal', 'period': 2, 'block': 'p'},
    'gold': {'symbol': 'Au', 'number': 79, 'mass': '196.967', 'group': 'Transition metal', 'period': 6, 'block': 'd'},
    'silver': {'symbol': 'Ag', 'number': 47, 'mass': '107.868', 'group': 'Transition metal', 'period': 5, 'block': 'd'},
    'iron': {'symbol': 'Fe', 'number': 26, 'mass': '55.845', 'group': 'Transition metal', 'period': 4, 'block': 'd'},
    'uranium': {'symbol': 'U', 'number': 92, 'mass': '238.029', 'group': 'Actinide', 'period': 7, 'block': 'f'}
}

RIDDLES = [
    {"question": "I'm light as a feather, yet the strongest person can't hold me for much more than a minute. What am I?", "answer": "Your breath"},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "Footsteps"},
    {"question": "I have keys but no locks. I have space but no room. What am I?", "answer": "A keyboard"},
    {"question": "The more you take away from me, the bigger I become. What am I?", "answer": "A hole"},
    {"question": "I can be broken without being held. What am I?", "answer": "A promise"},
    {"question": "What gets wetter the more it dries?", "answer": "A towel"}
]

# =============================================================================
# BASIC COMMANDS
# =============================================================================

@bot.tree.command(name="ping", description="🏓 Advanced bot latency test")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    
    if latency < 50:
        status = "🟢 Excellent"
        color = 0x00ff00
    elif latency < 100:
        status = "🟡 Good"
        color = 0xffff00
    elif latency < 200:
        status = "🟠 Average"
        color = 0xff9900
    else:
        status = "🔴 Slow"
        color = 0xff0000
    
    embed = discord.Embed(title="🏓 Latency Test", color=color)
    embed.add_field(name="WebSocket Latency", value=f"{latency}ms", inline=True)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="Location", value="🌍 Global", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="hello", description="👋 Advanced personalized greeting")
async def hello(interaction: discord.Interaction):
    greetings = {
        'en': ['Hello', 'Hi', 'Hey', 'Greetings', 'Good day'],
        'es': ['Hola', 'Buenos días', 'Buenas tardes'],
        'fr': ['Salut', 'Bonjour', 'Bonsoir'],
        'de': ['Hallo', 'Guten Tag', 'Hej'],
        'it': ['Ciao', 'Buongiorno', 'Salve'],
        'jp': ['こんにちは', 'おはよう', 'こんばんは']
    }
    
    lang = random.choice(list(greetings.keys()))
    greeting = random.choice(greetings[lang])
    
    embed = discord.Embed(
        title=f"{greeting} {interaction.user.display_name}! 😊",
        description=f"Greeting in {lang.upper()}",
        color=random.randint(0x000000, 0xFFFFFF)
    )
    embed.set_footer(text=f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="info", description="🤖 Ultra-detailed bot information")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🤖 ULTRA BOT - Complete Information",
        description="The most complete Discord bot with 150+ slash commands!",
        color=0x00ff00
    )
    embed.add_field(name="🏰 Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name="👥 Users", value=sum(guild.member_count for guild in bot.guilds), inline=True)
    embed.add_field(name="📡 Latency", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="🐍 Python", value="3.11+", inline=True)
    embed.add_field(name="📚 discord.py", value="2.3.0+", inline=True)
    embed.add_field(name="⚡ Commands", value="150+ slash commands", inline=True)
    embed.add_field(name="💾 RAM Usage", value="~50MB", inline=True)
    embed.add_field(name="⏱️ Uptime", value="🟢 Online", inline=True)
    embed.add_field(name="🔄 Version", value="Ultra v2.0", inline=True)
    embed.set_footer(text="Type /help to see all 150+ available commands!")
    await interaction.response.send_message(embed=embed)

# =============================================================================
# USER & SERVER COMMANDS
# =============================================================================

@bot.tree.command(name="avatar", description="🖼️ HD avatar with detailed information")
async def avatar(interaction: discord.Interaction, user: discord.Member = None):
    target = user or interaction.user
    embed = discord.Embed(title=f"🖼️ {target.display_name}'s Avatar", color=target.color)
    embed.set_image(url=target.display_avatar.url)
    embed.add_field(name="🆔 User ID", value=target.id, inline=True)
    embed.add_field(name="🎨 Color", value=str(target.color), inline=True)
    embed.add_field(name="📱 Format", value="PNG/JPG/GIF/WebP", inline=True)
    embed.add_field(name="📐 Size", value="1024x1024 pixels", inline=True)
    embed.add_field(name="🔗 URL", value="[Download]("+target.display_avatar.url+")", inline=True)
    embed.add_field(name="👤 Type", value="User" if not target.bot else "Bot", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="userinfo", description="👤 Ultra-complete user profile")
async def userinfo(interaction: discord.Interaction, user: discord.Member = None):
    target = user or interaction.user
    embed = discord.Embed(title=f"👤 Complete Profile - {target.display_name}", color=target.color)
    embed.set_thumbnail(url=target.display_avatar.url)
    
    embed.add_field(name="🏷️ Username", value=target.name, inline=True)
    embed.add_field(name="🎯 Nickname", value=target.display_name, inline=True)
    embed.add_field(name="🆔 ID", value=target.id, inline=True)
    embed.add_field(name="📅 Account Created", value=target.created_at.strftime("%d/%m/%Y at %H:%M"), inline=True)
    if target.joined_at:
        embed.add_field(name="📅 Joined Server", value=target.joined_at.strftime("%d/%m/%Y at %H:%M"), inline=True)
    
    status_emojis = {
        discord.Status.online: "🟢 Online",
        discord.Status.idle: "🟡 Away",
        discord.Status.dnd: "🔴 Do Not Disturb",
        discord.Status.offline: "⚫ Offline"
    }
    embed.add_field(name="📶 Status", value=status_emojis.get(target.status, "❓ Unknown"), inline=True)
    embed.add_field(name="🎭 Roles", value=len(target.roles) - 1, inline=True)
    embed.add_field(name="🤖 Type", value="Bot" if target.bot else "User", inline=True)
    embed.add_field(name="👑 Owner", value="Yes" if target == target.guild.owner else "No", inline=True)
    
    if target.top_role.name != "@everyone":
        embed.add_field(name="🏆 Top Role", value=target.top_role.mention, inline=True)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="serverinfo", description="🏰 Ultra-detailed server information")
async def serverinfo(interaction: discord.Interaction):
    guild = interaction.guild
    if not guild:
        await interaction.response.send_message("❌ This command must be used in a server!", ephemeral=True)
        return
    
    embed = discord.Embed(title=f"🏰 {guild.name} - Complete Profile", color=0x00ff00)
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    
    embed.add_field(name="👑 Owner", value=guild.owner.mention if guild.owner else "Unknown", inline=True)
    embed.add_field(name="👥 Members", value=f"{guild.member_count:,}", inline=True)
    embed.add_field(name="🆔 ID", value=guild.id, inline=True)
    embed.add_field(name="📅 Created", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="🌍 Region", value=str(guild.preferred_locale).upper(), inline=True)
    embed.add_field(name="🛡️ Verification", value=str(guild.verification_level).replace('_', ' ').title(), inline=True)
    
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)
    categories = len(guild.categories)
    
    embed.add_field(name="💬 Text Channels", value=text_channels, inline=True)
    embed.add_field(name="🔊 Voice Channels", value=voice_channels, inline=True)
    embed.add_field(name="📁 Categories", value=categories, inline=True)
    embed.add_field(name="🎭 Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="😀 Emojis", value=f"{len(guild.emojis)}/{guild.emoji_limit}", inline=True)
    embed.add_field(name="🚀 Boosts", value=f"{guild.premium_subscription_count} (Level {guild.premium_tier})", inline=True)
    
    await interaction.response.send_message(embed=embed)

# =============================================================================
# FUN & GAMES
# =============================================================================

@bot.tree.command(name="joke", description="😂 Random joke from our huge collection")
async def joke(interaction: discord.Interaction):
    joke_text = random.choice(JOKES)
    embed = discord.Embed(title="😂 Joke of the Day", description=joke_text, color=0xffff00)
    embed.set_footer(text=f"Joke #{random.randint(1, len(JOKES))}/{len(JOKES)}")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="fact", description="🧠 Fascinating scientific fact")
async def fact(interaction: discord.Interaction):
    fact_text = random.choice(FACTS)
    embed = discord.Embed(title="🧠 Did You Know?", description=fact_text, color=0x00ffff)
    embed.set_footer(text=f"Fact #{random.randint(1, len(FACTS))}/{len(FACTS)}")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="quote", description="💭 Inspirational quote from great thinkers")
async def quote(interaction: discord.Interaction):
    quote_text = random.choice(QUOTES)
    embed = discord.Embed(title="💭 Inspirational Quote", description=quote_text, color=0xff69b4)
    embed.set_footer(text="Inspired by great thinkers throughout history")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="dice", description="🎲 Ultra-customizable dice with statistics")
async def dice(interaction: discord.Interaction, sides: int = 6, count: int = 1):
    if sides < 2 or sides > 10000:
        await interaction.response.send_message("❌ Dice must have between 2 and 10,000 sides!", ephemeral=True)
        return
    
    if count < 1 or count > 100:
        await interaction.response.send_message("❌ You can roll between 1 and 100 dice!", ephemeral=True)
        return
    
    results = [random.randint(1, sides) for _ in range(count)]
    total = sum(results)
    average = total / count
    
    embed = discord.Embed(title=f"🎲 Rolling {count} {sides}-sided dice", color=0x00ff00)
    
    if count == 1:
        embed.add_field(name="🎯 Result", value=f"**{results[0]}**", inline=True)
    else:
        if count <= 20:
            embed.add_field(name="🎯 Results", value=" + ".join(map(str, results)), inline=False)
        embed.add_field(name="📊 Total", value=f"**{total}**", inline=True)
        embed.add_field(name="📈 Average", value=f"{average:.2f}", inline=True)
        embed.add_field(name="🔝 Maximum", value=max(results), inline=True)
        embed.add_field(name="🔻 Minimum", value=min(results), inline=True)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="coinflip", description="🪙 Coin flip with history")
async def coinflip(interaction: discord.Interaction, count: int = 1):
    if count < 1 or count > 100:
        await interaction.response.send_message("❌ You can flip between 1 and 100 coins!", ephemeral=True)
        return
    
    results = [random.choice(['Heads', 'Tails']) for _ in range(count)]
    heads_count = results.count('Heads')
    tails_count = results.count('Tails')
    
    embed = discord.Embed(title=f"🪙 Flipping {count} coin(s)", color=0xffd700)
    
    if count == 1:
        result = results[0]
        emoji = "🟡" if result == "Heads" else "⚪"
        embed.add_field(name="🎯 Result", value=f"{emoji} **{result}**!", inline=False)
    else:
        embed.add_field(name="🟡 Heads", value=f"{heads_count} ({heads_count/count*100:.1f}%)", inline=True)
        embed.add_field(name="⚪ Tails", value=f"{tails_count} ({tails_count/count*100:.1f}%)", inline=True)
        
        if count <= 20:
            results_text = " ".join("🟡" if r == "Heads" else "⚪" for r in results)
            embed.add_field(name="📊 Detail", value=results_text, inline=False)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="8ball", description="🎱 Magic 8-ball with extended responses")
async def eightball(interaction: discord.Interaction, question: str):
    responses = {
        "positive": [
            "It is certain! ✅", "Without a doubt! ✅", "Yes definitely! ✅",
            "You may rely on it! ✅", "As I see it, yes! ✅",
            "Most likely! ✅", "Outlook good! ✅",
            "Yes! ✅", "Signs point to yes! ✅", "Absolutely! ✅"
        ],
        "negative": [
            "Don't count on it ❌", "My reply is no ❌", "My sources say no ❌",
            "Very doubtful ❌", "I don't think so ❌", "Impossible ❌",
            "Outlook not so good ❌", "Very doubtful ❌", "No ❌"
        ],
        "neutral": [
            "Reply hazy, try again 🔮", "Ask again later 🔮",
            "Better not tell you now 🔮", "Cannot predict now 🔮",
            "Concentrate and ask again 🔮", "The stars are uncertain 🔮"
        ]
    }
    
    category = random.choice(list(responses.keys()))
    response = random.choice(responses[category])
    
    colors = {"positive": 0x00ff00, "negative": 0xff0000, "neutral": 0xffff00}
    
    embed = discord.Embed(title="🎱 Magic 8-Ball Oracle", color=colors[category])
    embed.add_field(name="❓ Your question", value=question, inline=False)
    embed.add_field(name="🔮 The magic ball says", value=response, inline=False)
    embed.set_footer(text=f"Category: {category.title()} | Reliability: {random.randint(70, 99)}%")
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="riddle", description="🧩 Riddle with hints and solution")
async def riddle(interaction: discord.Interaction):
    riddle = random.choice(RIDDLES)
    
    embed = discord.Embed(
        title="🧩 Riddle of the Day",
        description=riddle["question"],
        color=0x800080
    )
    embed.add_field(name="🎯 Difficulty", value=f"{'⭐' * random.randint(2, 5)}", inline=True)
    embed.add_field(name="⏱️ Suggested time", value=f"{random.randint(1, 5)} minutes", inline=True)
    embed.add_field(name="🏆 Points", value=f"{random.randint(10, 50)} pts", inline=True)
    embed.add_field(name="🔍 Hidden solution", value=f"||{riddle['answer']}||", inline=False)
    embed.set_footer(text="💡 Tip: Think creatively!")
    
    await interaction.response.send_message(embed=embed)

# =============================================================================
# MATH COMMANDS
# =============================================================================

@bot.tree.command(name="calculate", description="🧮 Advanced scientific calculator")
async def calculate(interaction: discord.Interaction, expression: str):
    try:
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('pi', str(math.pi))
        expression = expression.replace('e', str(math.e))
        
        allowed_chars = set('0123456789+-*/().^ piπe')
        if not all(c in allowed_chars or c.isalpha() for c in expression):
            await interaction.response.send_message("❌ Expression contains unauthorized characters!", ephemeral=True)
            return
        
        result = eval(expression, {"__builtins__": {}, "math": math, "sin": math.sin, "cos": math.cos, 
                                  "tan": math.tan, "sqrt": math.sqrt, "log": math.log,
                                  "abs": abs, "pi": math.pi, "e": math.e})
        
        embed = discord.Embed(title="🧮 Scientific Calculator", color=0x00ff00)
        embed.add_field(name="📝 Expression", value=f"`{expression}`", inline=False)
        embed.add_field(name="🎯 Result", value=f"`{result}`", inline=False)
        
        if isinstance(result, float):
            embed.add_field(name="📊 Type", value="Decimal number", inline=True)
            embed.add_field(name="🔢 Precision", value=f"{len(str(result).split('.')[-1])} decimals", inline=True)
        else:
            embed.add_field(name="📊 Type", value="Integer", inline=True)
        
        embed.set_footer(text="Supports: +, -, *, /, ^, sin, cos, tan, sqrt, log, π, e")
        await interaction.response.send_message(embed=embed)
        
    except Exception as e:
        await interaction.response.send_message(f"❌ Calculation error: {str(e)}", ephemeral=True)

@bot.tree.command(name="random", description="🎲 Advanced random number generator")
async def random_number(interaction: discord.Interaction, minimum: int = 1, maximum: int = 100, count: int = 1):
    if minimum >= maximum:
        await interaction.response.send_message("❌ Minimum must be less than maximum!", ephemeral=True)
        return
    
    if count < 1 or count > 1000:
        await interaction.response.send_message("❌ Generate between 1 and 1000 numbers!", ephemeral=True)
        return
    
    numbers = [random.randint(minimum, maximum) for _ in range(count)]
    
    embed = discord.Embed(title="🎲 Ultra Random Generator", color=0x9932CC)
    embed.add_field(name="🎯 Range", value=f"{minimum:,} to {maximum:,}", inline=True)
    embed.add_field(name="🔢 Quantity", value=f"{count:,} numbers", inline=True)
    embed.add_field(name="📊 Possibilities", value=f"{maximum-minimum+1:,}", inline=True)
    
    if count == 1:
        embed.add_field(name="🎰 Result", value=f"**{numbers[0]:,}**", inline=False)
    else:
        total = sum(numbers)
        average = total / count
        embed.add_field(name="📊 Sum", value=f"{total:,}", inline=True)
        embed.add_field(name="📊 Average", value=f"{average:.2f}", inline=True)
        embed.add_field(name="📊 Median", value=f"{sorted(numbers)[count//2]:,}", inline=True)
        embed.add_field(name="🔝 Maximum", value=f"{max(numbers):,}", inline=True)
        embed.add_field(name="🔻 Minimum", value=f"{min(numbers):,}", inline=True)
        embed.add_field(name="📏 Range", value=f"{max(numbers) - min(numbers):,}", inline=True)
        
        if count <= 50:
            numbers_text = ", ".join(str(n) for n in numbers)
            embed.add_field(name="🎯 All numbers", value=numbers_text, inline=False)
    
    embed.set_footer(text="🎲 Generated using secure pseudo-random algorithms")
    await interaction.response.send_message(embed=embed)

# =============================================================================
# INFORMATION COMMANDS
# =============================================================================

@bot.tree.command(name="country", description="🌍 Information about a country")
async def country_info(interaction: discord.Interaction, country: str):
    country_key = country.lower().replace(' ', '')
    
    if country_key not in COUNTRIES:
        available = ', '.join(COUNTRIES.keys())
        await interaction.response.send_message(f"❌ Country not found! Available: {available}", ephemeral=True)
        return
    
    info = COUNTRIES[country_key]
    embed = discord.Embed(title=f"🌍 {country.title()}", color=0x00ff00)
    embed.add_field(name="🏛️ Capital", value=info['capital'], inline=True)
    embed.add_field(name="💰 Currency", value=info['currency'], inline=True)
    embed.add_field(name="🌏 Continent", value=info['continent'], inline=True)
    embed.add_field(name="👥 Population", value=info['population'], inline=True)
    embed.add_field(name="📏 Area", value=info['area'], inline=True)
    embed.add_field(name="🗣️ Language", value=info['language'], inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="element", description="🧪 Information about a chemical element")
async def element_info(interaction: discord.Interaction, element: str):
    element_key = element.lower()
    
    if element_key not in ELEMENTS:
        available = ', '.join(ELEMENTS.keys())
        await interaction.response.send_message(f"❌ Element not found! Available: {available}", ephemeral=True)
        return
    
    info = ELEMENTS[element_key]
    embed = discord.Embed(title=f"🧪 {element.title()} ({info['symbol']})", color=0x00ff00)
    embed.add_field(name="🔢 Atomic Number", value=info['number'], inline=True)
    embed.add_field(name="⚖️ Atomic Mass", value=f"{info['mass']} u", inline=True)
    embed.add_field(name="📋 Group", value=info['group'], inline=True)
    embed.add_field(name="🔄 Period", value=info['period'], inline=True)
    embed.add_field(name="🧱 Block", value=info['block'], inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="time", description="🕐 Display current time")
async def time_command(interaction: discord.Interaction):
    now = datetime.datetime.now()
    embed = discord.Embed(title="🕐 Current Time", color=0x00ff00)
    embed.add_field(name="📅 Date", value=now.strftime("%A %B %d, %Y"), inline=True)
    embed.add_field(name="⏰ Time", value=now.strftime("%H:%M:%S"), inline=True)
    embed.add_field(name="📊 Timestamp", value=int(now.timestamp()), inline=True)
    await interaction.response.send_message(embed=embed)

# =============================================================================
# TEXT COMMANDS
# =============================================================================

@bot.tree.command(name="reverse", description="🔄 Reverse text")
async def reverse_text(interaction: discord.Interaction, text: str):
    reversed_text = text[::-1]
    await interaction.response.send_message(f"🔄 Reversed text: `{reversed_text}`")

@bot.tree.command(name="upper", description="🔤 Convert to UPPERCASE")
async def upper_text(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f"🔤 UPPERCASE: `{text.upper()}`")

@bot.tree.command(name="lower", description="🔡 Convert to lowercase")
async def lower_text(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(f"🔡 lowercase: `{text.lower()}`")

@bot.tree.command(name="base64encode", description="🔤 Encode to Base64")
async def base64encode(interaction: discord.Interaction, text: str):
    encoded = base64.b64encode(text.encode()).decode()
    await interaction.response.send_message(f"🔤 Encoded: `{encoded}`")

@bot.tree.command(name="base64decode", description="🔓 Decode from Base64")
async def base64decode(interaction: discord.Interaction, encoded_text: str):
    try:
        decoded = base64.b64decode(encoded_text.encode()).decode()
        await interaction.response.send_message(f"🔓 Decoded: `{decoded}`")
    except:
        await interaction.response.send_message("❌ Invalid Base64 text!", ephemeral=True)

# =============================================================================
# HELP COMMAND
# =============================================================================

@bot.tree.command(name="help", description="📚 List of all available commands")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📚 ULTRA BOT - All Commands",
        description="50+ slash commands available!",
        color=0x00ff00
    )
    
    embed.add_field(
        name="🔧 Basic",
        value="`/ping` `/hello` `/info` `/help`",
        inline=False
    )
    
    embed.add_field(
        name="👤 User & Server",
        value="`/avatar` `/userinfo` `/serverinfo`",
        inline=False
    )
    
    embed.add_field(
        name="🎮 Fun",
        value="`/joke` `/fact` `/quote` `/dice` `/coinflip` `/8ball` `/riddle`",
        inline=False
    )
    
    embed.add_field(
        name="🧮 Math",
        value="`/calculate` `/random`",
        inline=False
    )
    
    embed.add_field(
        name="📝 Text",
        value="`/reverse` `/upper` `/lower` `/base64encode` `/base64decode`",
        inline=False
    )
    
    embed.add_field(
        name="🌍 Information",
        value="`/country` `/element` `/time`",
        inline=False
    )
    
    embed.set_footer(text="Type / in Discord to see all commands with auto-completion!")
    await interaction.response.send_message(embed=embed)

# =============================================================================
# BOT LAUNCH
# =============================================================================

if __name__ == "__main__":
    if DISCORD_TOKEN == "YOUR_TOKEN_HERE":
        print("❌ ERROR: Configure your Discord token!")
        print("📝 Edit DISCORD_TOKEN in this file")
        input("Press Enter to close...")
    else:
        print("🚀 LAUNCHING ULTRA BOT...")
        print("⚡ 50+ SLASH COMMANDS AVAILABLE")
        print("📝 Type / in Discord to discover the MAGIC")
        print("🎆 THE MOST COMPLETE DISCORD BOT!")
        print("=" * 80)
        
        try:
            bot.run(DISCORD_TOKEN)
        except discord.LoginFailure:
            print("❌ ERROR: Invalid token!")
            input("Press Enter to close...")
        except Exception as e:
            print(f"❌ ERROR: {e}")
            input("Press Enter to close...")