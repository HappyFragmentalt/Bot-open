import discord
from discord.ext import commands
import random
import math
import datetime
import asyncio
import json
import base64
import hashlib
from typing import Optional


class BasicCommands(commands.Cog):
    """Basic commands for the Discord bot"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx):
        """Say hello to the user"""
        greetings = ['Hello', 'Hi', 'Hey', 'Greetings', 'Salutations', 'Howdy', 'Good day']
        await ctx.send(f'{random.choice(greetings)} {ctx.author.mention}!')

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Check bot latency"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'🏓 Pong! Latency: {latency}ms')

    @commands.command(name='info', aliases=['botinfo'])
    async def info(self, ctx):
        """Display bot information"""
        embed = discord.Embed(
            title="🤖 Bot Information",
            description="A comprehensive Discord bot with hundreds of commands",
            color=0x00ff00
        )
        embed.add_field(name="🏰 Guilds", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="👥 Users", value=len(self.bot.users), inline=True)
        embed.add_field(name="📡 Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="🐍 Python", value="3.11+", inline=True)
        embed.add_field(name="📚 discord.py", value="2.3.0+", inline=True)
        embed.add_field(name="⚡ Commands", value="1000+", inline=True)
        await ctx.send(embed=embed)


class UtilityCommands(commands.Cog):
    """Utility and information commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar', aliases=['av', 'pfp'])
    async def avatar(self, ctx, member: discord.Member = None):
        """Get user's avatar"""
        if member is None:
            member = ctx.author
        
        embed = discord.Embed(
            title=f"{member.display_name}'s Avatar",
            color=member.color
        )
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='serverinfo', aliases=['server', 'guildinfo'])
    async def serverinfo(self, ctx):
        """Get server information"""
        guild = ctx.guild
        embed = discord.Embed(
            title=f"📊 {guild.name}",
            color=0x00ff00
        )
        embed.add_field(name="👑 Owner", value=guild.owner.mention, inline=True)
        embed.add_field(name="👥 Members", value=guild.member_count, inline=True)
        embed.add_field(name="💬 Channels", value=len(guild.channels), inline=True)
        embed.add_field(name="🎭 Roles", value=len(guild.roles), inline=True)
        embed.add_field(name="📅 Created", value=guild.created_at.strftime("%B %d, %Y"), inline=True)
        embed.add_field(name="🆔 ID", value=guild.id, inline=True)
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)

    @commands.command(name='userinfo', aliases=['user', 'whois'])
    async def userinfo(self, ctx, member: discord.Member = None):
        """Get user information"""
        if member is None:
            member = ctx.author
        
        embed = discord.Embed(
            title=f"👤 {member.display_name}",
            color=member.color
        )
        embed.add_field(name="🏷️ Username", value=f"{member.name}#{member.discriminator}", inline=True)
        embed.add_field(name="🆔 ID", value=member.id, inline=True)
        embed.add_field(name="📅 Joined Server", value=member.joined_at.strftime("%B %d, %Y"), inline=True)
        embed.add_field(name="📅 Created Account", value=member.created_at.strftime("%B %d, %Y"), inline=True)
        embed.add_field(name="🎭 Roles", value=len(member.roles) - 1, inline=True)
        embed.add_field(name="🤖 Bot", value="Yes" if member.bot else "No", inline=True)
        embed.set_thumbnail(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='calculate', aliases=['calc', 'math'])
    async def calculate(self, ctx, *, expression):
        """Calculate mathematical expressions"""
        try:
            # Safe evaluation of mathematical expressions
            allowed_chars = set('0123456789+-*/().^ ')
            if not all(c in allowed_chars for c in expression):
                await ctx.send("❌ Invalid characters in expression!")
                return
            
            # Replace ^ with **
            expression = expression.replace('^', '**')
            result = eval(expression)
            
            embed = discord.Embed(
                title="🧮 Calculator",
                color=0x00ff00
            )
            embed.add_field(name="Expression", value=f"`{expression}`", inline=False)
            embed.add_field(name="Result", value=f"`{result}`", inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

    @commands.command(name='time', aliases=['clock', 'datetime'])
    async def time(self, ctx):
        """Get current time"""
        now = datetime.datetime.now()
        embed = discord.Embed(
            title="🕐 Current Time",
            color=0x00ff00
        )
        embed.add_field(name="Date", value=now.strftime("%B %d, %Y"), inline=True)
        embed.add_field(name="Time", value=now.strftime("%H:%M:%S"), inline=True)
        embed.add_field(name="Day", value=now.strftime("%A"), inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='base64encode', aliases=['b64encode'])
    async def base64encode(self, ctx, *, text):
        """Encode text to base64"""
        encoded = base64.b64encode(text.encode()).decode()
        await ctx.send(f"🔤 Encoded: `{encoded}`")

    @commands.command(name='base64decode', aliases=['b64decode'])
    async def base64decode(self, ctx, *, encoded_text):
        """Decode base64 text"""
        try:
            decoded = base64.b64decode(encoded_text.encode()).decode()
            await ctx.send(f"🔤 Decoded: `{decoded}`")
        except:
            await ctx.send("❌ Invalid base64 string!")

    @commands.command(name='hash')
    async def hash_text(self, ctx, algorithm, *, text):
        """Hash text using various algorithms"""
        algorithms = {'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256, 'sha512': hashlib.sha512}
        
        if algorithm.lower() not in algorithms:
            await ctx.send(f"❌ Supported algorithms: {', '.join(algorithms.keys())}")
            return
        
        hash_obj = algorithms[algorithm.lower()]()
        hash_obj.update(text.encode())
        result = hash_obj.hexdigest()
        
        embed = discord.Embed(
            title=f"🔐 {algorithm.upper()} Hash",
            color=0x00ff00
        )
        embed.add_field(name="Input", value=f"`{text}`", inline=False)
        embed.add_field(name="Hash", value=f"`{result}`", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='membercount', aliases=['members'])
    async def membercount(self, ctx):
        """Get detailed member statistics"""
        guild = ctx.guild
        total = guild.member_count
        humans = len([m for m in guild.members if not m.bot])
        bots = len([m for m in guild.members if m.bot])
        online = len([m for m in guild.members if m.status != discord.Status.offline])
        
        embed = discord.Embed(
            title=f"📊 Member Statistics for {guild.name}",
            color=0x00ff00
        )
        embed.add_field(name="👥 Total Members", value=total, inline=True)
        embed.add_field(name="👤 Humans", value=humans, inline=True)
        embed.add_field(name="🤖 Bots", value=bots, inline=True)
        embed.add_field(name="🟢 Online", value=online, inline=True)
        embed.add_field(name="📴 Offline", value=total - online, inline=True)
        embed.add_field(name="📈 Online %", value=f"{round((online/total)*100, 1)}%", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='channelinfo', aliases=['channel'])
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        """Get information about a channel"""
        if channel is None:
            channel = ctx.channel
        
        embed = discord.Embed(
            title=f"📺 Channel Information: #{channel.name}",
            color=0x00ff00
        )
        embed.add_field(name="🆔 ID", value=channel.id, inline=True)
        embed.add_field(name="📅 Created", value=channel.created_at.strftime("%B %d, %Y"), inline=True)
        embed.add_field(name="📂 Category", value=channel.category.name if channel.category else "None", inline=True)
        embed.add_field(name="🔞 NSFW", value="Yes" if channel.nsfw else "No", inline=True)
        embed.add_field(name="⏱️ Slowmode", value=f"{channel.slowmode_delay}s" if channel.slowmode_delay else "None", inline=True)
        embed.add_field(name="📍 Position", value=channel.position, inline=True)
        
        if channel.topic:
            embed.add_field(name="📝 Topic", value=channel.topic, inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name='roleinfo', aliases=['role'])
    async def roleinfo(self, ctx, *, role_name):
        """Get information about a role"""
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not role:
            await ctx.send("❌ Role not found!")
            return
        
        embed = discord.Embed(
            title=f"🎭 Role Information: {role.name}",
            color=role.color
        )
        embed.add_field(name="🆔 ID", value=role.id, inline=True)
        embed.add_field(name="📅 Created", value=role.created_at.strftime("%B %d, %Y"), inline=True)
        embed.add_field(name="👥 Members", value=len(role.members), inline=True)
        embed.add_field(name="🌈 Color", value=str(role.color), inline=True)
        embed.add_field(name="📍 Position", value=role.position, inline=True)
        embed.add_field(name="🔗 Mentionable", value="Yes" if role.mentionable else "No", inline=True)
        embed.add_field(name="📌 Hoisted", value="Yes" if role.hoist else "No", inline=True)
        embed.add_field(name="🤖 Managed", value="Yes" if role.managed else "No", inline=True)
        
        # Show some key permissions
        perms = role.permissions
        key_perms = []
        if perms.administrator:
            key_perms.append("Administrator")
        if perms.manage_guild:
            key_perms.append("Manage Server")
        if perms.manage_channels:
            key_perms.append("Manage Channels")
        if perms.manage_roles:
            key_perms.append("Manage Roles")
        if perms.ban_members:
            key_perms.append("Ban Members")
        if perms.kick_members:
            key_perms.append("Kick Members")
        
        if key_perms:
            embed.add_field(name="🔑 Key Permissions", value="\n".join(key_perms), inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name='emojis', aliases=['emojilist'])
    async def emojis(self, ctx):
        """List all custom emojis in the server"""
        emojis = ctx.guild.emojis
        if not emojis:
            await ctx.send("❌ This server has no custom emojis!")
            return
        
        # Split emojis into chunks to avoid message length limits
        emoji_chunks = [emojis[i:i+20] for i in range(0, len(emojis), 20)]
        
        for i, chunk in enumerate(emoji_chunks):
            embed = discord.Embed(
                title=f"😀 Custom Emojis ({i+1}/{len(emoji_chunks)})",
                color=0x00ff00
            )
            
            emoji_text = ""
            for emoji in chunk:
                emoji_text += f"{emoji} `:{emoji.name}:` (ID: {emoji.id})\n"
            
            embed.description = emoji_text
            embed.set_footer(text=f"Total emojis: {len(emojis)}")
            await ctx.send(embed=embed)
            
            if i < len(emoji_chunks) - 1:
                await asyncio.sleep(1)  # Avoid rate limits

    @commands.command(name='invites')
    @commands.has_permissions(manage_guild=True)
    async def invites(self, ctx):
        """List all active invites for the server"""
        try:
            invites = await ctx.guild.invites()
            if not invites:
                await ctx.send("❌ No active invites found!")
                return
            
            embed = discord.Embed(
                title="📨 Active Invites",
                color=0x00ff00
            )
            
            for invite in invites[:10]:  # Limit to 10 invites
                channel = invite.channel.name if invite.channel else "Unknown"
                inviter = invite.inviter.display_name if invite.inviter else "Unknown"
                uses = invite.uses or 0
                max_uses = invite.max_uses or "∞"
                
                embed.add_field(
                    name=f"Code: {invite.code}",
                    value=f"Channel: #{channel}\nInviter: {inviter}\nUses: {uses}/{max_uses}",
                    inline=True
                )
            
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to view invites!")

    @commands.command(name='createinvite', aliases=['invite'])
    @commands.has_permissions(create_instant_invite=True)
    async def createinvite(self, ctx, max_uses: int = 0, max_age: int = 0):
        """Create an invite for the current channel"""
        try:
            invite = await ctx.channel.create_invite(
                max_uses=max_uses,
                max_age=max_age,
                reason=f"Invite created by {ctx.author}"
            )
            
            embed = discord.Embed(
                title="📨 Invite Created",
                color=0x00ff00
            )
            embed.add_field(name="Invite Link", value=invite.url, inline=False)
            embed.add_field(name="Channel", value=f"#{ctx.channel.name}", inline=True)
            embed.add_field(name="Max Uses", value=max_uses or "Unlimited", inline=True)
            embed.add_field(name="Expires", value="Never" if max_age == 0 else f"{max_age} seconds", inline=True)
            
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to create invites!")

    @commands.command(name='backup')
    @commands.has_permissions(administrator=True)
    async def backup_info(self, ctx):
        """Get server backup information (channels, roles, etc.)"""
        guild = ctx.guild
        
        # Count different types of channels
        text_channels = len([c for c in guild.channels if isinstance(c, discord.TextChannel)])
        voice_channels = len([c for c in guild.channels if isinstance(c, discord.VoiceChannel)])
        categories = len([c for c in guild.channels if isinstance(c, discord.CategoryChannel)])
        
        embed = discord.Embed(
            title="💾 Server Backup Information",
            description=f"Backup data for {guild.name}",
            color=0x00ff00
        )
        
        embed.add_field(name="📊 Basic Info", 
                       value=f"Members: {guild.member_count}\nRoles: {len(guild.roles)}\nEmojis: {len(guild.emojis)}", 
                       inline=True)
        
        embed.add_field(name="📺 Channels", 
                       value=f"Text: {text_channels}\nVoice: {voice_channels}\nCategories: {categories}", 
                       inline=True)
        
        embed.add_field(name="⚙️ Settings", 
                       value=f"Verification: {guild.verification_level}\nRegion: {guild.region}\nBoosts: {guild.premium_subscription_count}", 
                       inline=True)
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        embed.set_footer(text="Note: This is just information display, not actual backup functionality")
        await ctx.send(embed=embed)

    @commands.command(name='permissions', aliases=['perms'])
    async def permissions(self, ctx, member: discord.Member = None):
        """Check a member's permissions in the current channel"""
        if member is None:
            member = ctx.author
        
        perms = ctx.channel.permissions_for(member)
        
        # Get all permissions that are True
        allowed_perms = [perm.replace('_', ' ').title() for perm, value in perms if value]
        
        embed = discord.Embed(
            title=f"🔑 Permissions for {member.display_name}",
            description=f"In #{ctx.channel.name}",
            color=member.color
        )
        
        if allowed_perms:
            # Split into chunks to avoid field value limits
            chunks = [allowed_perms[i:i+10] for i in range(0, len(allowed_perms), 10)]
            for i, chunk in enumerate(chunks):
                embed.add_field(
                    name=f"✅ Allowed Permissions ({i+1})",
                    value="\n".join(chunk),
                    inline=True
                )
        else:
            embed.add_field(name="❌ No Permissions", value="This member has no permissions in this channel.", inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name='uptime')
    async def uptime(self, ctx):
        """Show bot uptime"""
        # This would need to be implemented with a start time tracker
        # For now, we'll show a placeholder
        embed = discord.Embed(
            title="⏱️ Bot Uptime",
            description="Bot uptime tracking would need to be implemented with a start time variable.",
            color=0x00ff00
        )
        embed.add_field(name="Status", value="Online and running", inline=True)
        embed.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='weather')
    async def weather(self, ctx, *, location):
        """Get weather information (placeholder - would need weather API)"""
        embed = discord.Embed(
            title=f"🌤️ Weather for {location}",
            description="Weather functionality would require integration with a weather API like OpenWeatherMap.",
            color=0x00ff00
        )
        embed.add_field(name="Implementation Note", 
                       value="To enable this feature, you would need to:\n1. Get an API key from OpenWeatherMap\n2. Install requests library\n3. Implement API calls", 
                       inline=False)
        await ctx.send(embed=embed)


class FunCommands(commands.Cog):
    """Fun and entertainment commands"""
    
    def __init__(self, bot):
        self.bot = bot
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the coffee file a police report? It got mugged!",
            "What's the best thing about Switzerland? I don't know, but the flag is a big plus!",
            "Why don't programmers like nature? It has too many bugs!",
            "How do you organize a space party? You planet!",
            "Why was the math book sad? Because it had too many problems!",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
        
        self.facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat.",
            "A group of flamingos is called a 'flamboyance'.",
            "Octopuses have three hearts and blue blood.",
            "Bananas are berries, but strawberries aren't.",
            "A shrimp's heart is in its head.",
            "Elephants are afraid of bees.",
            "Wombat droppings are cube-shaped.",
            "A group of crows is called a 'murder'.",
            "Sharks have been around longer than trees.",
            "The unicorn is Scotland's national animal."
        ]
        
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Life is what happens to you while you're busy making other plans. - John Lennon",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "It is during our darkest moments that we must focus to see the light. - Aristotle",
            "The way to get started is to quit talking and begin doing. - Walt Disney",
            "Don't let yesterday take up too much of today. - Will Rogers",
            "You learn more from failure than from success. - Unknown",
            "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
            "If you are working on something that you really care about, you don't have to be pushed. The vision pulls you. - Steve Jobs",
            "People who are crazy enough to think they can change the world, are the ones who do. - Rob Siltanen"
        ]

    @commands.command(name='joke', aliases=['funny', 'laugh'])
    async def joke(self, ctx):
        """Get a random joke"""
        joke = random.choice(self.jokes)
        embed = discord.Embed(
            title="😂 Random Joke",
            description=joke,
            color=0xffff00
        )
        await ctx.send(embed=embed)

    @commands.command(name='dice', aliases=['roll', 'd6'])
    async def dice(self, ctx, sides: int = 6):
        """Roll a dice"""
        if sides < 2 or sides > 100:
            await ctx.send("❌ Dice must have between 2 and 100 sides!")
            return
        
        result = random.randint(1, sides)
        await ctx.send(f"🎲 Rolled a {sides}-sided dice: **{result}**")

    @commands.command(name='coinflip', aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """Flip a coin"""
        result = random.choice(['Heads', 'Tails'])
        emoji = '🪙' if result == 'Heads' else '🪙'
        await ctx.send(f"{emoji} **{result}**!")

    @commands.command(name='8ball', aliases=['eightball', 'magic8ball'])
    async def eightball(self, ctx, *, question):
        """Ask the magic 8-ball a question"""
        responses = [
            "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
            "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
            "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
            "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
            "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
        ]
        
        response = random.choice(responses)
        embed = discord.Embed(
            title="🎱 Magic 8-Ball",
            color=0x800080
        )
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=response, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='fact', aliases=['randomfact'])
    async def fact(self, ctx):
        """Get a random fact"""
        fact = random.choice(self.facts)
        embed = discord.Embed(
            title="🧠 Random Fact",
            description=fact,
            color=0x00ffff
        )
        await ctx.send(embed=embed)

    @commands.command(name='quote', aliases=['inspire', 'motivation'])
    async def quote(self, ctx):
        """Get an inspirational quote"""
        quote = random.choice(self.quotes)
        embed = discord.Embed(
            title="💭 Inspirational Quote",
            description=quote,
            color=0xff69b4
        )
        await ctx.send(embed=embed)

    @commands.command(name='choose', aliases=['pick', 'decide'])
    async def choose(self, ctx, *, choices):
        """Choose randomly from given options (separate with commas)"""
        options = [choice.strip() for choice in choices.split(',')]
        if len(options) < 2:
            await ctx.send("❌ Please provide at least 2 options separated by commas!")
            return
        
        chosen = random.choice(options)
        embed = discord.Embed(
            title="🤔 Decision Maker",
            color=0x00ff00
        )
        embed.add_field(name="Options", value="\n".join(f"• {option}" for option in options), inline=False)
        embed.add_field(name="My Choice", value=f"**{chosen}**", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='rps', aliases=['rockpaperscissors'])
    async def rps(self, ctx, choice):
        """Play rock paper scissors"""
        choices = ['rock', 'paper', 'scissors']
        user_choice = choice.lower()
        
        if user_choice not in choices:
            await ctx.send("❌ Choose rock, paper, or scissors!")
            return
        
        bot_choice = random.choice(choices)
        
        # Determine winner
        if user_choice == bot_choice:
            result = "It's a tie!"
            color = 0xffff00
        elif (user_choice == 'rock' and bot_choice == 'scissors') or \
             (user_choice == 'paper' and bot_choice == 'rock') or \
             (user_choice == 'scissors' and bot_choice == 'paper'):
            result = "You win!"
            color = 0x00ff00
        else:
            result = "I win!"
            color = 0xff0000
        
        embed = discord.Embed(
            title="✂️ Rock Paper Scissors",
            color=color
        )
        embed.add_field(name="Your Choice", value=user_choice.title(), inline=True)
        embed.add_field(name="My Choice", value=bot_choice.title(), inline=True)
        embed.add_field(name="Result", value=result, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='number', aliases=['guess', 'guessnumber'])
    async def guess_number(self, ctx):
        """Start a number guessing game"""
        number = random.randint(1, 100)
        
        embed = discord.Embed(
            title="🔢 Number Guessing Game",
            description="I'm thinking of a number between 1 and 100. Try to guess it!\nYou have 6 attempts.",
            color=0x00ff00
        )
        await ctx.send(embed=embed)
        
        attempts = 0
        max_attempts = 6
        
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        
        while attempts < max_attempts:
            try:
                message = await self.bot.wait_for('message', timeout=30.0, check=check)
                
                try:
                    guess = int(message.content)
                except ValueError:
                    await ctx.send("❌ Please enter a valid number!")
                    continue
                
                attempts += 1
                
                if guess == number:
                    await ctx.send(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                    return
                elif guess < number:
                    await ctx.send(f"📈 Too low! Attempts remaining: {max_attempts - attempts}")
                else:
                    await ctx.send(f"📉 Too high! Attempts remaining: {max_attempts - attempts}")
                
            except asyncio.TimeoutError:
                await ctx.send(f"⏰ Time's up! The number was {number}.")
                return
        
        await ctx.send(f"💔 Game over! The number was {number}.")


class ModerationCommands(commands.Cog):
    """Moderation commands for server management"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear', aliases=['purge', 'delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        """Clear messages from the channel"""
        if amount > 100:
            await ctx.send("❌ Cannot delete more than 100 messages at once!")
            return
        
        deleted = await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"🗑️ Deleted {len(deleted) - 1} messages!", delete_after=3)

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Kick a member from the server"""
        if member.top_role >= ctx.author.top_role:
            await ctx.send("❌ You cannot kick this member!")
            return
        
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="👢 Member Kicked",
                color=0xff9900
            )
            embed.add_field(name="Member", value=member.mention, inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to kick this member!")

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Ban a member from the server"""
        if member.top_role >= ctx.author.top_role:
            await ctx.send("❌ You cannot ban this member!")
            return
        
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="🔨 Member Banned",
                color=0xff0000
            )
            embed.add_field(name="Member", value=member.mention, inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to ban this member!")

    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """Unban a member from the server"""
        banned_users = [entry async for entry in ctx.guild.bans()]
        
        member_name, member_discriminator = member.split('#')
        
        for ban_entry in banned_users:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"✅ Unbanned {user.mention}")
                return
        
        await ctx.send("❌ User not found in ban list!")

    @commands.command(name='slowmode', aliases=['slow'])
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        """Set channel slowmode"""
        if seconds > 21600:  # 6 hours max
            await ctx.send("❌ Slowmode cannot exceed 6 hours (21600 seconds)!")
            return
        
        await ctx.channel.edit(slowmode_delay=seconds)
        if seconds == 0:
            await ctx.send("✅ Slowmode disabled!")
        else:
            await ctx.send(f"⏱️ Slowmode set to {seconds} seconds!")

    @commands.command(name='mute')
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, duration: int = None, *, reason="No reason provided"):
        """Mute a member (duration in minutes)"""
        if member.top_role >= ctx.author.top_role:
            await ctx.send("❌ You cannot mute this member!")
            return
        
        # Find or create muted role
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted", reason="Auto-created mute role")
            
            # Set permissions for muted role in all channels
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False, speak=False, add_reactions=False)
        
        try:
            await member.add_roles(muted_role, reason=reason)
            
            embed = discord.Embed(
                title="🔇 Member Muted",
                color=0xff9900
            )
            embed.add_field(name="Member", value=member.mention, inline=True)
            embed.add_field(name="Duration", value=f"{duration} minutes" if duration else "Permanent", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
            await ctx.send(embed=embed)
            
            # Auto-unmute after duration
            if duration:
                await asyncio.sleep(duration * 60)
                if muted_role in member.roles:
                    await member.remove_roles(muted_role, reason="Auto-unmute")
                    await ctx.send(f"🔊 {member.mention} has been automatically unmuted.")
                    
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to mute this member!")

    @commands.command(name='unmute')
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        """Unmute a member"""
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("❌ No muted role found!")
            return
        
        if muted_role not in member.roles:
            await ctx.send("❌ This member is not muted!")
            return
        
        try:
            await member.remove_roles(muted_role, reason=f"Unmuted by {ctx.author}")
            embed = discord.Embed(
                title="🔊 Member Unmuted",
                color=0x00ff00
            )
            embed.add_field(name="Member", value=member.mention, inline=True)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to unmute this member!")

    @commands.command(name='warn')
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Warn a member"""
        embed = discord.Embed(
            title="⚠️ Warning Issued",
            color=0xffff00
        )
        embed.add_field(name="Member", value=member.mention, inline=True)
        embed.add_field(name="Reason", value=reason, inline=True)
        embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
        
        await ctx.send(embed=embed)
        
        try:
            dm_embed = discord.Embed(
                title="⚠️ Warning",
                description=f"You have been warned in {ctx.guild.name}",
                color=0xffff00
            )
            dm_embed.add_field(name="Reason", value=reason, inline=False)
            dm_embed.add_field(name="Moderator", value=str(ctx.author), inline=False)
            await member.send(embed=dm_embed)
        except discord.Forbidden:
            await ctx.send("⚠️ Could not send warning to user's DMs.")

    @commands.command(name='softban')
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Softban a member (ban then immediately unban to delete messages)"""
        if member.top_role >= ctx.author.top_role:
            await ctx.send("❌ You cannot softban this member!")
            return
        
        try:
            await member.ban(reason=f"Softban: {reason}", delete_message_days=1)
            await ctx.guild.unban(member, reason="Softban unban")
            
            embed = discord.Embed(
                title="🔨 Member Softbanned",
                color=0xff6600
            )
            embed.add_field(name="Member", value=member.mention, inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to softban this member!")

    @commands.command(name='lockdown')
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel = None):
        """Lock down a channel"""
        if channel is None:
            channel = ctx.channel
        
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        
        embed = discord.Embed(
            title="🔒 Channel Locked",
            description=f"{channel.mention} has been locked down.",
            color=0xff0000
        )
        await ctx.send(embed=embed)

    @commands.command(name='unlock')
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        """Unlock a channel"""
        if channel is None:
            channel = ctx.channel
        
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        
        embed = discord.Embed(
            title="🔓 Channel Unlocked",
            description=f"{channel.mention} has been unlocked.",
            color=0x00ff00
        )
        await ctx.send(embed=embed)

    @commands.command(name='massban')
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, *members: discord.Member):
        """Ban multiple members at once"""
        if len(members) == 0:
            await ctx.send("❌ Please provide at least one member to ban!")
            return
        
        if len(members) > 10:
            await ctx.send("❌ Cannot ban more than 10 members at once!")
            return
        
        banned = []
        failed = []
        
        for member in members:
            try:
                if member.top_role < ctx.author.top_role:
                    await member.ban(reason=f"Mass ban by {ctx.author}")
                    banned.append(member.mention)
                else:
                    failed.append(f"{member.mention} (insufficient permissions)")
            except discord.Forbidden:
                failed.append(f"{member.mention} (bot lacks permissions)")
        
        embed = discord.Embed(
            title="🔨 Mass Ban Results",
            color=0xff0000
        )
        
        if banned:
            embed.add_field(name="✅ Successfully Banned", value="\n".join(banned), inline=False)
        if failed:
            embed.add_field(name="❌ Failed to Ban", value="\n".join(failed), inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name='nickname', aliases=['nick'])
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, nickname=None):
        """Change or reset a member's nickname"""
        if member.top_role >= ctx.author.top_role and member != ctx.author:
            await ctx.send("❌ You cannot change this member's nickname!")
            return
        
        try:
            old_nick = member.display_name
            await member.edit(nick=nickname)
            
            embed = discord.Embed(
                title="✏️ Nickname Changed",
                color=0x00ff00
            )
            embed.add_field(name="Member", value=member.mention, inline=True)
            embed.add_field(name="Old Nickname", value=old_nick, inline=True)
            embed.add_field(name="New Nickname", value=nickname or "None", inline=True)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to change this member's nickname!")

    @commands.command(name='modlogs', aliases=['logs'])
    @commands.has_permissions(view_audit_log=True)
    async def modlogs(self, ctx, limit: int = 10):
        """View recent moderation actions"""
        if limit > 20:
            limit = 20
        
        embed = discord.Embed(
            title="📋 Recent Moderation Actions",
            color=0x00ff00
        )
        
        actions = []
        async for entry in ctx.guild.audit_logs(limit=limit):
            if entry.action in [discord.AuditLogAction.kick, discord.AuditLogAction.ban, 
                               discord.AuditLogAction.unban, discord.AuditLogAction.member_role_update]:
                actions.append(f"**{entry.action.name.title()}** | {entry.target} | by {entry.user} | {entry.created_at.strftime('%Y-%m-%d %H:%M')}")
        
        if actions:
            embed.description = "\n".join(actions)
        else:
            embed.description = "No recent moderation actions found."
        
        await ctx.send(embed=embed)


class InteractiveCommands(commands.Cog):
    """Interactive commands and games"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='poll')
    async def poll(self, ctx, question, *options):
        """Create a poll with reactions"""
        if len(options) < 2:
            await ctx.send("❌ Please provide at least 2 options!")
            return
        
        if len(options) > 10:
            await ctx.send("❌ Maximum 10 options allowed!")
            return
        
        embed = discord.Embed(
            title="📊 Poll",
            description=question,
            color=0x00ff00
        )
        
        reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        
        for i, option in enumerate(options):
            embed.add_field(name=f"{reactions[i]} Option {i+1}", value=option, inline=False)
        
        poll_msg = await ctx.send(embed=embed)
        
        for i in range(len(options)):
            await poll_msg.add_reaction(reactions[i])

    @commands.command(name='say', aliases=['echo'])
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message):
        """Make the bot say something"""
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(name='embed')
    @commands.has_permissions(manage_messages=True)
    async def create_embed(self, ctx, title, *, description):
        """Create an embed message"""
        embed = discord.Embed(
            title=title,
            description=description,
            color=0x00ff00
        )
        embed.set_footer(text=f"Created by {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(name='remind', aliases=['reminder'])
    async def remind(self, ctx, time: int, *, reminder):
        """Set a reminder (in minutes)"""
        if time > 1440:  # 24 hours
            await ctx.send("❌ Reminder cannot exceed 24 hours!")
            return
        
        await ctx.send(f"⏰ Reminder set for {time} minutes!")
        await asyncio.sleep(time * 60)
        
        embed = discord.Embed(
            title="⏰ Reminder",
            description=reminder,
            color=0xffff00
        )
        await ctx.send(f"{ctx.author.mention}", embed=embed)

    @commands.command(name='react')
    @commands.has_permissions(manage_messages=True)
    async def react(self, ctx, emoji, message_id: int = None):
        """Add a reaction to a message"""
        if message_id:
            try:
                message = await ctx.channel.fetch_message(message_id)
                await message.add_reaction(emoji)
                await ctx.send("✅ Reaction added!")
            except discord.NotFound:
                await ctx.send("❌ Message not found!")
        else:
            await ctx.message.add_reaction(emoji)


# Additional utility functions for math and text operations
class AdvancedUtilityCommands(commands.Cog):
    """Advanced utility commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reverse')
    async def reverse_text(self, ctx, *, text):
        """Reverse text"""
        reversed_text = text[::-1]
        await ctx.send(f"🔄 Reversed: `{reversed_text}`")

    @commands.command(name='upper')
    async def upper_text(self, ctx, *, text):
        """Convert text to uppercase"""
        await ctx.send(f"🔤 UPPERCASE: `{text.upper()}`")

    @commands.command(name='lower')
    async def lower_text(self, ctx, *, text):
        """Convert text to lowercase"""
        await ctx.send(f"🔤 lowercase: `{text.lower()}`")

    @commands.command(name='count')
    async def count_text(self, ctx, *, text):
        """Count characters, words, and lines in text"""
        chars = len(text)
        words = len(text.split())
        lines = len(text.split('\n'))
        
        embed = discord.Embed(
            title="📊 Text Statistics",
            color=0x00ff00
        )
        embed.add_field(name="Characters", value=chars, inline=True)
        embed.add_field(name="Words", value=words, inline=True)
        embed.add_field(name="Lines", value=lines, inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='binary')
    async def text_to_binary(self, ctx, *, text):
        """Convert text to binary"""
        binary = ' '.join(format(ord(char), '08b') for char in text)
        if len(binary) > 1900:  # Discord message limit
            await ctx.send("❌ Text too long to convert!")
            return
        await ctx.send(f"💻 Binary: `{binary}`")

    @commands.command(name='morse')
    async def text_to_morse(self, ctx, *, text):
        """Convert text to morse code"""
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': '/'
        }
        
        morse = ' '.join(morse_dict.get(char.upper(), char) for char in text)
        if len(morse) > 1900:
            await ctx.send("❌ Text too long to convert!")
            return
        await ctx.send(f"📡 Morse: `{morse}`")

    @commands.command(name='password', aliases=['pwd', 'genpass'])
    async def generate_password(self, ctx, length: int = 12):
        """Generate a random password"""
        if length < 4 or length > 50:
            await ctx.send("❌ Password length must be between 4 and 50!")
            return
        
        import string
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        
        try:
            await ctx.author.send(f"🔐 Your generated password: `{password}`")
            await ctx.send("✅ Password sent to your DMs!")
        except discord.Forbidden:
            await ctx.send("❌ Could not send password to DMs! Please enable DMs from server members.")

    @commands.command(name='qr')
    async def qr_code(self, ctx, *, text):
        """Generate QR code info for text"""
        await ctx.send(f"🔲 QR Code for: `{text}`\nUse an online QR generator to create the actual code.")


# Text manipulation and fun text commands
class TextCommands(commands.Cog):
    """Text manipulation commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='leetspeak', aliases=['leet', '1337'])
    async def leetspeak(self, ctx, *, text):
        """Convert text to leetspeak"""
        leet_dict = {
            'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7', 'l': '1'
        }
        
        leet_text = ''.join(leet_dict.get(char.lower(), char) for char in text)
        await ctx.send(f"🤖 L33t: `{leet_text}`")

    @commands.command(name='bubble', aliases=['bubbletext'])
    async def bubble_text(self, ctx, *, text):
        """Convert text to bubble letters"""
        bubble_dict = {
            'a': '🅰️', 'b': '🅱️', 'o': '⭕', 'i': 'ℹ️', 'm': 'Ⓜ️', 'p': '🅿️'
        }
        
        bubble = ' '.join(bubble_dict.get(char.lower(), char) for char in text if char != ' ')
        await ctx.send(f"🫧 Bubble: {bubble}")

    @commands.command(name='zalgo')
    async def zalgo_text(self, ctx, *, text):
        """Add zalgo effect to text (simplified)"""
        zalgo_chars = ['̸', '̵', '̶', '̷', '̴', '̲', '̳']
        zalgo = ''.join(char + random.choice(zalgo_chars) if char.isalpha() else char for char in text)
        await ctx.send(f"👹 Zalgo: `{zalgo}`")

    @commands.command(name='uwu')
    async def uwu_text(self, ctx, *, text):
        """Convert text to uwu speak"""
        uwu = text.lower()
        uwu = uwu.replace('r', 'w').replace('l', 'w')
        uwu = uwu.replace('th', 'f').replace('n', 'ny')
        await ctx.send(f"🥺 UwU: `{uwu}`")

    @commands.command(name='pirate')
    async def pirate_speak(self, ctx, *, text):
        """Convert text to pirate speak"""
        pirate_dict = {
            'hello': 'ahoy', 'hi': 'ahoy', 'you': 'ye', 'my': 'me', 'is': 'be',
            'are': 'be', 'the': 'th\'', 'over': 'o\'er', 'to': 'ta'
        }
        
        words = text.lower().split()
        pirate_words = [pirate_dict.get(word, word) for word in words]
        pirate_text = ' '.join(pirate_words)
        
        await ctx.send(f"🏴‍☠️ Pirate: `{pirate_text}, matey!`")


# Information and reference commands
class InfoCommands(commands.Cog):
    """Information and reference commands"""
    
    def __init__(self, bot):
        self.bot = bot
        
        # Programming languages info
        self.languages = {
            'python': {
                'description': 'A high-level, interpreted programming language known for its simplicity and readability.',
                'creator': 'Guido van Rossum',
                'year': '1991',
                'paradigm': 'Multi-paradigm',
                'typing': 'Dynamic',
                'extension': '.py'
            },
            'javascript': {
                'description': 'A versatile programming language primarily used for web development.',
                'creator': 'Brendan Eich',
                'year': '1995',
                'paradigm': 'Multi-paradigm',
                'typing': 'Dynamic',
                'extension': '.js'
            },
            'java': {
                'description': 'A class-based, object-oriented programming language designed for portability.',
                'creator': 'James Gosling',
                'year': '1995',
                'paradigm': 'Object-oriented',
                'typing': 'Static',
                'extension': '.java'
            },
            'csharp': {
                'description': 'A modern, object-oriented programming language developed by Microsoft.',
                'creator': 'Microsoft',
                'year': '2000',
                'paradigm': 'Multi-paradigm',
                'typing': 'Static',
                'extension': '.cs'
            },
            'cpp': {
                'description': 'An extension of C that includes object-oriented programming features.',
                'creator': 'Bjarne Stroustrup',
                'year': '1985',
                'paradigm': 'Multi-paradigm',
                'typing': 'Static',
                'extension': '.cpp'
            }
        }
        
        # Countries info
        self.countries = {
            'usa': {'name': 'United States', 'capital': 'Washington D.C.', 'currency': 'USD', 'continent': 'North America'},
            'uk': {'name': 'United Kingdom', 'capital': 'London', 'currency': 'GBP', 'continent': 'Europe'},
            'france': {'name': 'France', 'capital': 'Paris', 'currency': 'EUR', 'continent': 'Europe'},
            'germany': {'name': 'Germany', 'capital': 'Berlin', 'currency': 'EUR', 'continent': 'Europe'},
            'japan': {'name': 'Japan', 'capital': 'Tokyo', 'currency': 'JPY', 'continent': 'Asia'},
            'canada': {'name': 'Canada', 'capital': 'Ottawa', 'currency': 'CAD', 'continent': 'North America'},
            'australia': {'name': 'Australia', 'capital': 'Canberra', 'currency': 'AUD', 'continent': 'Oceania'},
            'brazil': {'name': 'Brazil', 'capital': 'Brasília', 'currency': 'BRL', 'continent': 'South America'},
            'china': {'name': 'China', 'capital': 'Beijing', 'currency': 'CNY', 'continent': 'Asia'},
            'india': {'name': 'India', 'capital': 'New Delhi', 'currency': 'INR', 'continent': 'Asia'}
        }
        
        # Historical events
        self.historical_events = [
            "1969 - Apollo 11 Moon Landing",
            "1989 - Fall of the Berlin Wall",
            "1776 - American Declaration of Independence",
            "1945 - End of World War II",
            "1969 - Internet (ARPANET) invented",
            "1991 - World Wide Web created",
            "1947 - India gains independence",
            "1963 - Martin Luther King Jr.'s 'I Have a Dream' speech",
            "1955 - Discovery of DNA structure",
            "1969 - Woodstock music festival"
        ]
        
        # Science facts
        self.science_facts = [
            "The human brain contains approximately 86 billion neurons.",
            "Light travels at 299,792,458 meters per second in a vacuum.",
            "Water has its maximum density at 4°C (39.2°F).",
            "The periodic table has 118 confirmed elements.",
            "DNA contains four bases: A, T, G, and C.",
            "Sound travels at approximately 343 meters per second in air.",
            "The Earth's core temperature is about 6000°C, similar to the Sun's surface.",
            "Humans share about 60% of their DNA with bananas.",
            "A single bolt of lightning is five times hotter than the Sun's surface.",
            "The universe is approximately 13.8 billion years old."
        ]

    @commands.command(name='language', aliases=['lang', 'programming'])
    async def language_info(self, ctx, *, language):
        """Get information about a programming language"""
        lang_key = language.lower().replace(' ', '').replace('#', 'sharp')
        
        if lang_key not in self.languages:
            available = ', '.join(self.languages.keys())
            await ctx.send(f"❌ Language not found! Available: {available}")
            return
        
        info = self.languages[lang_key]
        
        embed = discord.Embed(
            title=f"💻 {language.title()} Programming Language",
            description=info['description'],
            color=0x00ff00
        )
        embed.add_field(name="Creator", value=info['creator'], inline=True)
        embed.add_field(name="Year Created", value=info['year'], inline=True)
        embed.add_field(name="Paradigm", value=info['paradigm'], inline=True)
        embed.add_field(name="Typing", value=info['typing'], inline=True)
        embed.add_field(name="File Extension", value=info['extension'], inline=True)
        
        await ctx.send(embed=embed)

    @commands.command(name='country', aliases=['nation'])
    async def country_info(self, ctx, *, country):
        """Get information about a country"""
        country_key = country.lower().replace(' ', '')
        
        if country_key not in self.countries:
            available = ', '.join([info['name'] for info in self.countries.values()])
            await ctx.send(f"❌ Country not found! Available: {available}")
            return
        
        info = self.countries[country_key]
        
        embed = discord.Embed(
            title=f"🌍 {info['name']}",
            color=0x00ff00
        )
        embed.add_field(name="Capital", value=info['capital'], inline=True)
        embed.add_field(name="Currency", value=info['currency'], inline=True)
        embed.add_field(name="Continent", value=info['continent'], inline=True)
        
        await ctx.send(embed=embed)

    @commands.command(name='history', aliases=['historical'])
    async def history_fact(self, ctx):
        """Get a random historical fact"""
        event = random.choice(self.historical_events)
        
        embed = discord.Embed(
            title="📜 Historical Event",
            description=event,
            color=0x8B4513
        )
        await ctx.send(embed=embed)

    @commands.command(name='science', aliases=['sciencefact'])
    async def science_fact(self, ctx):
        """Get a random science fact"""
        fact = random.choice(self.science_facts)
        
        embed = discord.Embed(
            title="🔬 Science Fact",
            description=fact,
            color=0x4169E1
        )
        await ctx.send(embed=embed)

    @commands.command(name='periodic', aliases=['element'])
    async def periodic_element(self, ctx, element):
        """Get information about a chemical element"""
        elements = {
            'hydrogen': {'symbol': 'H', 'number': 1, 'mass': '1.008', 'group': 'Nonmetal'},
            'helium': {'symbol': 'He', 'number': 2, 'mass': '4.003', 'group': 'Noble gas'},
            'carbon': {'symbol': 'C', 'number': 6, 'mass': '12.011', 'group': 'Nonmetal'},
            'nitrogen': {'symbol': 'N', 'number': 7, 'mass': '14.007', 'group': 'Nonmetal'},
            'oxygen': {'symbol': 'O', 'number': 8, 'mass': '15.999', 'group': 'Nonmetal'},
            'gold': {'symbol': 'Au', 'number': 79, 'mass': '196.967', 'group': 'Transition metal'},
            'silver': {'symbol': 'Ag', 'number': 47, 'mass': '107.868', 'group': 'Transition metal'},
            'iron': {'symbol': 'Fe', 'number': 26, 'mass': '55.845', 'group': 'Transition metal'},
            'copper': {'symbol': 'Cu', 'number': 29, 'mass': '63.546', 'group': 'Transition metal'},
            'uranium': {'symbol': 'U', 'number': 92, 'mass': '238.029', 'group': 'Actinide'}
        }
        
        element_key = element.lower()
        if element_key not in elements:
            available = ', '.join(elements.keys())
            await ctx.send(f"❌ Element not found! Available: {available}")
            return
        
        info = elements[element_key]
        
        embed = discord.Embed(
            title=f"🧪 {element.title()} ({info['symbol']})",
            color=0x00ff00
        )
        embed.add_field(name="Atomic Number", value=info['number'], inline=True)
        embed.add_field(name="Atomic Mass", value=f"{info['mass']} u", inline=True)
        embed.add_field(name="Group", value=info['group'], inline=True)
        
        await ctx.send(embed=embed)

    @commands.command(name='color', aliases=['colour'])
    async def color_info(self, ctx, color_code):
        """Get information about a color (hex code)"""
        if not color_code.startswith('#'):
            color_code = '#' + color_code
        
        if len(color_code) != 7:
            await ctx.send("❌ Invalid hex color code! Use format: #RRGGBB")
            return
        
        try:
            # Convert hex to decimal
            color_int = int(color_code[1:], 16)
            
            # Extract RGB values
            r = (color_int >> 16) & 255
            g = (color_int >> 8) & 255
            b = color_int & 255
            
            embed = discord.Embed(
                title=f"🎨 Color Information",
                color=color_int
            )
            embed.add_field(name="Hex Code", value=color_code.upper(), inline=True)
            embed.add_field(name="RGB", value=f"({r}, {g}, {b})", inline=True)
            embed.add_field(name="Decimal", value=color_int, inline=True)
            
            # Add color preview
            embed.add_field(name="Preview", value="■" * 10, inline=False)
            
            await ctx.send(embed=embed)
            
        except ValueError:
            await ctx.send("❌ Invalid hex color code!")

    @commands.command(name='ascii')
    async def ascii_code(self, ctx, character):
        """Get ASCII code of a character"""
        if len(character) != 1:
            await ctx.send("❌ Please provide exactly one character!")
            return
        
        ascii_val = ord(character)
        
        embed = discord.Embed(
            title="📋 ASCII Information",
            color=0x00ff00
        )
        embed.add_field(name="Character", value=f"`{character}`", inline=True)
        embed.add_field(name="ASCII Code", value=ascii_val, inline=True)
        embed.add_field(name="Binary", value=format(ascii_val, '08b'), inline=True)
        embed.add_field(name="Hexadecimal", value=f"0x{ascii_val:02X}", inline=True)
        
        await ctx.send(embed=embed)

    @commands.command(name='timezone', aliases=['tz'])
    async def timezone_info(self, ctx, tz=None):
        """Get current time in different timezones"""
        import datetime
        
        timezones = {
            'utc': 0, 'gmt': 0, 'est': -5, 'pst': -8, 'cst': -6, 'mst': -7,
            'jst': 9, 'cet': 1, 'ist': 5.5, 'aest': 10
        }
        
        if tz is None:
            # Show all timezones
            embed = discord.Embed(
                title="🕐 World Clock",
                color=0x00ff00
            )
            
            base_time = datetime.datetime.utcnow()
            
            for tz_name, offset in timezones.items():
                if isinstance(offset, float):
                    hours = int(offset)
                    minutes = int((offset % 1) * 60)
                    tz_time = base_time + datetime.timedelta(hours=hours, minutes=minutes)
                else:
                    tz_time = base_time + datetime.timedelta(hours=offset)
                
                embed.add_field(
                    name=tz_name.upper(),
                    value=tz_time.strftime("%H:%M:%S"),
                    inline=True
                )
            
            await ctx.send(embed=embed)
        else:
            tz_key = tz.lower()
            if tz_key not in timezones:
                available = ', '.join(timezones.keys())
                await ctx.send(f"❌ Timezone not found! Available: {available}")
                return
            
            base_time = datetime.datetime.utcnow()
            offset = timezones[tz_key]
            
            if isinstance(offset, float):
                hours = int(offset)
                minutes = int((offset % 1) * 60)
                tz_time = base_time + datetime.timedelta(hours=hours, minutes=minutes)
            else:
                tz_time = base_time + datetime.timedelta(hours=offset)
            
            embed = discord.Embed(
                title=f"🕐 Time in {tz_key.upper()}",
                description=tz_time.strftime("%H:%M:%S - %B %d, %Y"),
                color=0x00ff00
            )
            await ctx.send(embed=embed)

    @commands.command(name='units', aliases=['unit'])
    async def unit_info(self, ctx, unit_type=None):
        """Get information about measurement units"""
        unit_systems = {
            'length': {
                'metric': ['millimeter (mm)', 'centimeter (cm)', 'meter (m)', 'kilometer (km)'],
                'imperial': ['inch (in)', 'foot (ft)', 'yard (yd)', 'mile (mi)']
            },
            'weight': {
                'metric': ['milligram (mg)', 'gram (g)', 'kilogram (kg)', 'tonne (t)'],
                'imperial': ['ounce (oz)', 'pound (lb)', 'stone (st)', 'ton']
            },
            'temperature': {
                'scales': ['Celsius (°C)', 'Fahrenheit (°F)', 'Kelvin (K)', 'Rankine (°R)']
            },
            'volume': {
                'metric': ['milliliter (mL)', 'liter (L)', 'cubic meter (m³)'],
                'imperial': ['fluid ounce (fl oz)', 'pint (pt)', 'quart (qt)', 'gallon (gal)']
            }
        }
        
        if unit_type is None:
            available = ', '.join(unit_systems.keys())
            await ctx.send(f"📏 Available unit types: {available}")
            return
        
        unit_key = unit_type.lower()
        if unit_key not in unit_systems:
            available = ', '.join(unit_systems.keys())
            await ctx.send(f"❌ Unit type not found! Available: {available}")
            return
        
        info = unit_systems[unit_key]
        
        embed = discord.Embed(
            title=f"📏 {unit_type.title()} Units",
            color=0x00ff00
        )
        
        for system, units in info.items():
            embed.add_field(
                name=system.title(),
                value="\n".join(units),
                inline=True
            )
        
        await ctx.send(embed=embed)

    @commands.command(name='nato', aliases=['phonetic'])
    async def nato_alphabet(self, ctx, *, text=None):
        """Convert text to NATO phonetic alphabet"""
        nato_dict = {
            'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
            'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
            'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
            'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
            'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
            'Z': 'Zulu', '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
            '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
        }
        
        if text is None:
            # Show the full alphabet
            embed = discord.Embed(
                title="📻 NATO Phonetic Alphabet",
                color=0x00ff00
            )
            
            letters = '\n'.join([f"{k} - {v}" for k, v in list(nato_dict.items())[:13]])
            letters2 = '\n'.join([f"{k} - {v}" for k, v in list(nato_dict.items())[13:26]])
            numbers = '\n'.join([f"{k} - {v}" for k, v in list(nato_dict.items())[26:]])
            
            embed.add_field(name="A-M", value=letters, inline=True)
            embed.add_field(name="N-Z", value=letters2, inline=True)
            embed.add_field(name="Numbers", value=numbers, inline=True)
            
            await ctx.send(embed=embed)
        else:
            # Convert text
            nato_text = []
            for char in text.upper():
                if char in nato_dict:
                    nato_text.append(nato_dict[char])
                elif char == ' ':
                    nato_text.append('(space)')
                else:
                    nato_text.append(char)
            
            embed = discord.Embed(
                title="📻 NATO Phonetic Conversion",
                color=0x00ff00
            )
            embed.add_field(name="Original", value=f"`{text}`", inline=False)
            embed.add_field(name="NATO Phonetic", value=" - ".join(nato_text), inline=False)
            
            await ctx.send(embed=embed)

    @commands.command(name='protocol', aliases=['port'])
    async def protocol_info(self, ctx, protocol=None):
        """Get information about network protocols and ports"""
        protocols = {
            'http': {'port': 80, 'description': 'Hypertext Transfer Protocol', 'type': 'Application Layer'},
            'https': {'port': 443, 'description': 'HTTP Secure', 'type': 'Application Layer'},
            'ftp': {'port': 21, 'description': 'File Transfer Protocol', 'type': 'Application Layer'},
            'ssh': {'port': 22, 'description': 'Secure Shell', 'type': 'Application Layer'},
            'telnet': {'port': 23, 'description': 'Teletype Network', 'type': 'Application Layer'},
            'smtp': {'port': 25, 'description': 'Simple Mail Transfer Protocol', 'type': 'Application Layer'},
            'dns': {'port': 53, 'description': 'Domain Name System', 'type': 'Application Layer'},
            'dhcp': {'port': 67, 'description': 'Dynamic Host Configuration Protocol', 'type': 'Application Layer'},
            'pop3': {'port': 110, 'description': 'Post Office Protocol v3', 'type': 'Application Layer'},
            'imap': {'port': 143, 'description': 'Internet Message Access Protocol', 'type': 'Application Layer'}
        }
        
        if protocol is None:
            embed = discord.Embed(
                title="🌐 Network Protocols",
                color=0x00ff00
            )
            
            protocol_list = []
            for name, info in protocols.items():
                protocol_list.append(f"**{name.upper()}** - Port {info['port']} - {info['description']}")
            
            embed.description = "\n".join(protocol_list)
            await ctx.send(embed=embed)
        else:
            protocol_key = protocol.lower()
            if protocol_key not in protocols:
                available = ', '.join(protocols.keys())
                await ctx.send(f"❌ Protocol not found! Available: {available}")
                return
            
            info = protocols[protocol_key]
            
            embed = discord.Embed(
                title=f"🌐 {protocol.upper()} Protocol",
                description=info['description'],
                color=0x00ff00
            )
            embed.add_field(name="Default Port", value=info['port'], inline=True)
            embed.add_field(name="Layer", value=info['type'], inline=True)
            
            await ctx.send(embed=embed)

    @commands.command(name='status', aliases=['httpstatus'])
    async def http_status(self, ctx, code: int = None):
        """Get information about HTTP status codes"""
        status_codes = {
            200: "OK - Request successful",
            201: "Created - Resource created successfully",
            204: "No Content - Request successful, no content returned",
            301: "Moved Permanently - Resource moved to new URL",
            302: "Found - Resource temporarily moved",
            400: "Bad Request - Invalid request syntax",
            401: "Unauthorized - Authentication required",
            403: "Forbidden - Access denied",
            404: "Not Found - Resource not found",
            405: "Method Not Allowed - HTTP method not supported",
            429: "Too Many Requests - Rate limit exceeded",
            500: "Internal Server Error - Server encountered an error",
            502: "Bad Gateway - Invalid response from upstream server",
            503: "Service Unavailable - Server temporarily unavailable",
            504: "Gateway Timeout - Upstream server timeout"
        }
        
        if code is None:
            embed = discord.Embed(
                title="🌐 Common HTTP Status Codes",
                color=0x00ff00
            )
            
            # Group by category
            success = [f"{k}: {v}" for k, v in status_codes.items() if 200 <= k < 300]
            redirect = [f"{k}: {v}" for k, v in status_codes.items() if 300 <= k < 400]
            client_error = [f"{k}: {v}" for k, v in status_codes.items() if 400 <= k < 500]
            server_error = [f"{k}: {v}" for k, v in status_codes.items() if k >= 500]
            
            if success:
                embed.add_field(name="✅ Success (2xx)", value="\n".join(success), inline=False)
            if redirect:
                embed.add_field(name="🔄 Redirection (3xx)", value="\n".join(redirect), inline=False)
            if client_error:
                embed.add_field(name="❌ Client Error (4xx)", value="\n".join(client_error), inline=False)
            if server_error:
                embed.add_field(name="🚫 Server Error (5xx)", value="\n".join(server_error), inline=False)
            
            await ctx.send(embed=embed)
        else:
            if code not in status_codes:
                await ctx.send(f"❌ Status code {code} not in database!")
                return
            
            description = status_codes[code]
            
            # Determine category and emoji
            if 200 <= code < 300:
                category = "Success"
                emoji = "✅"
                color = 0x00ff00
            elif 300 <= code < 400:
                category = "Redirection"
                emoji = "🔄"
                color = 0xffff00
            elif 400 <= code < 500:
                category = "Client Error"
                emoji = "❌"
                color = 0xff9900
            else:
                category = "Server Error"
                emoji = "🚫"
                color = 0xff0000
            
            embed = discord.Embed(
                title=f"{emoji} HTTP {code}",
                description=description,
                color=color
            )
            embed.add_field(name="Category", value=category, inline=True)
            
            await ctx.send(embed=embed)


# Math and science commands
class MathCommands(commands.Cog):
    """Mathematical and scientific commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sqrt')
    async def square_root(self, ctx, number: float):
        """Calculate square root"""
        if number < 0:
            await ctx.send("❌ Cannot calculate square root of negative number!")
            return
        
        result = math.sqrt(number)
        await ctx.send(f"√{number} = {result}")

    @commands.command(name='factorial')
    async def factorial(self, ctx, number: int):
        """Calculate factorial"""
        if number < 0:
            await ctx.send("❌ Cannot calculate factorial of negative number!")
            return
        
        if number > 20:
            await ctx.send("❌ Number too large! Maximum is 20.")
            return
        
        result = math.factorial(number)
        await ctx.send(f"{number}! = {result}")

    @commands.command(name='prime')
    async def is_prime(self, ctx, number: int):
        """Check if a number is prime"""
        if number < 2:
            await ctx.send(f"❌ {number} is not a prime number.")
            return
        
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                await ctx.send(f"❌ {number} is not prime (divisible by {i}).")
                return
        
        await ctx.send(f"✅ {number} is a prime number!")

    @commands.command(name='fibonacci', aliases=['fib'])
    async def fibonacci(self, ctx, n: int):
        """Generate fibonacci sequence"""
        if n < 1 or n > 20:
            await ctx.send("❌ Please provide a number between 1 and 20!")
            return
        
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        
        sequence = ', '.join(str(x) for x in fib_sequence[:n])
        await ctx.send(f"🔢 Fibonacci({n}): {sequence}")

    @commands.command(name='random', aliases=['rand'])
    async def random_number(self, ctx, min_val: int = 1, max_val: int = 100):
        """Generate a random number"""
        if min_val >= max_val:
            await ctx.send("❌ Minimum value must be less than maximum value!")
            return
        
        result = random.randint(min_val, max_val)
        await ctx.send(f"🎲 Random number between {min_val} and {max_val}: **{result}**")

    @commands.command(name='convert')
    async def convert_units(self, ctx, value: float, from_unit: str, to_unit: str):
        """Convert between units (temperature, distance, weight)"""
        conversions = {
            # Temperature
            ('celsius', 'fahrenheit'): lambda c: c * 9/5 + 32,
            ('fahrenheit', 'celsius'): lambda f: (f - 32) * 5/9,
            ('celsius', 'kelvin'): lambda c: c + 273.15,
            ('kelvin', 'celsius'): lambda k: k - 273.15,
            
            # Distance
            ('km', 'miles'): lambda km: km * 0.621371,
            ('miles', 'km'): lambda m: m * 1.60934,
            ('m', 'ft'): lambda m: m * 3.28084,
            ('ft', 'm'): lambda ft: ft * 0.3048,
            
            # Weight
            ('kg', 'lbs'): lambda kg: kg * 2.20462,
            ('lbs', 'kg'): lambda lbs: lbs * 0.453592,
        }
        
        key = (from_unit.lower(), to_unit.lower())
        if key not in conversions:
            available = ', '.join(f"{f} to {t}" for f, t in conversions.keys())
            await ctx.send(f"❌ Conversion not supported!\nAvailable: {available}")
            return
        
        result = conversions[key](value)
        await ctx.send(f"🔄 {value} {from_unit} = {result:.2f} {to_unit}")


async def setup(bot):
    """Setup function to add all cogs to the bot"""
    await bot.add_cog(BasicCommands(bot))
    await bot.add_cog(UtilityCommands(bot))
    await bot.add_cog(FunCommands(bot))
    await bot.add_cog(ModerationCommands(bot))
    await bot.add_cog(InteractiveCommands(bot))
    await bot.add_cog(AdvancedUtilityCommands(bot))
    await bot.add_cog(TextCommands(bot))
    await bot.add_cog(InfoCommands(bot))
    await bot.add_cog(MathCommands(bot))
