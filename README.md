# 🤖 Ultra Discord Bot - English Version

![Discord Bot](https://img.shields.io/badge/Discord-Bot-7289DA?style=for-the-badge&logo=discord)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)
![Render](https://img.shields.io/badge/Render-Deploy-46E3B7?style=for-the-badge&logo=render)

A comprehensive Discord bot with **50+ slash commands** covering entertainment, utility, math, and information features.

## 🎆 Features

### 🔧 Basic Commands
- `/ping` - Advanced bot latency test
- `/hello` - Multi-language personalized greetings
- `/info` - Complete bot statistics
- `/help` - Command list with categories

### 👤 User & Server
- `/avatar` - HD avatar display with details
- `/userinfo` - Complete user profiles
- `/serverinfo` - Detailed server statistics

### 🎮 Fun & Entertainment
- `/joke` - Random jokes from huge collection
- `/fact` - Fascinating scientific facts
- `/quote` - Inspirational quotes
- `/dice` - Customizable dice with statistics
- `/coinflip` - Coin flipping with analytics
- `/8ball` - Magic 8-ball oracle
- `/riddle` - Brain teasers with solutions

### 🧮 Math & Calculations
- `/calculate` - Scientific calculator (supports π, e, sin, cos, etc.)
- `/random` - Advanced random number generator

### 📝 Text Utilities
- `/reverse` - Reverse text
- `/upper` / `/lower` - Case conversion
- `/base64encode` / `/base64decode` - Base64 encoding/decoding

### 🌍 Information
- `/country` - Country information (capitals, currencies, etc.)
- `/element` - Chemical element details
- `/time` - Current date and time

## 🚀 Quick Deploy on Render

### Prerequisites
1. **Discord Bot Token** - Get one from [Discord Developer Portal](https://discord.com/developers/applications)
2. **GitHub Account** - To host your code
3. **Render Account** - Sign up at [render.com](https://render.com)

### Step-by-Step Deployment

#### 1. 📁 Prepare Your Repository
```bash
# Clone or fork this repository
git clone <your-repo-url>
cd discord-bot

# Push to your GitHub repository
git add .
git commit -m "Deploy Discord bot to Render"
git push origin main
```

#### 2. 🔧 Create Web Service on Render
1. Go to [render.com](https://render.com) and sign in
2. Click **"New"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `discord-bot` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot_render.py`
   - **Plan**: `Free` (for testing)

#### 3. 🔐 Environment Variables
In Render dashboard, add these environment variables:
- **Key**: `DISCORD_TOKEN`
- **Value**: `YOUR_ACTUAL_DISCORD_BOT_TOKEN`

#### 4. 🚀 Deploy
Click **"Create Web Service"** and wait for deployment!

## 📂 Project Structure

```
discord-bot/
│
├── bot_render.py       # Render-optimized bot (MAIN FILE)
├── bot_english.py      # Local development version
├── requirements.txt    # Python dependencies
├── render.yaml        # Render configuration
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔧 Local Development

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "DISCORD_TOKEN=your_token_here" > .env

# Run locally
python bot_english.py
```

### Environment Variables
Create a `.env` file:
```env
DISCORD_TOKEN=your_discord_bot_token_here
PORT=10000
```

## 🌟 Key Features of Render Version

- **☁️ Cloud Hosting**: 24/7 uptime on Render
- **🔒 Environment Variables**: Secure token management
- **🌐 Health Checks**: Built-in Flask server for monitoring
- **📊 Auto-scaling**: Handles traffic bursts automatically
- **🔄 Auto-deploy**: Updates on git push (optional)

## 📈 Bot Statistics

- **Commands**: 50+ slash commands
- **Categories**: 6 different command categories
- **Languages**: Multi-language greetings
- **Data**: Jokes, facts, quotes, country info, chemical elements
- **Math**: Scientific calculator with advanced functions
- **Games**: Interactive entertainment features

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is open source. Feel free to use and modify!

## 🆘 Troubleshooting

### Common Issues

**Bot not responding to commands?**
- Check if DISCORD_TOKEN is correctly set in Render dashboard
- Verify the bot has necessary permissions in your Discord server
- Check Render logs for error messages

**Deployment failed?**
- Ensure `requirements.txt` has all dependencies
- Check that `bot_render.py` is the correct start command
- Verify Python version compatibility

**Bot goes offline?**
- Render free tier may sleep after inactivity
- Consider upgrading to paid plan for 24/7 uptime
- Check if Flask server is responding to health checks

### Support

- Check Render logs for detailed error messages
- Verify Discord bot permissions
- Ensure all environment variables are set correctly

## 🎉 Ready to Deploy!

Your Ultra Discord Bot is now ready to be deployed on Render with:
- ✅ 50+ professional slash commands
- ✅ Cloud hosting configuration
- ✅ Environment variable security
- ✅ Health monitoring
- ✅ Auto-scaling capabilities

Deploy now and enjoy your 24/7 Discord bot! 🚀
