# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a simple Discord bot built with discord.py that provides basic commands and serves as a foundation for Discord bot development. The bot uses environment variables for configuration and includes basic command handling.

## Development Commands

### Setup and Installation
```powershell
# Install dependencies
pip install -r requirements.txt

# Set up environment file
Copy-Item .env.example .env
# Then edit .env to add your DISCORD_TOKEN
```

### Running the Bot
```powershell
# Start the bot
python bot.py
```

### Development Testing
```powershell
# Test bot connection and basic functionality
python bot.py
# Look for "Bot has connected to Discord!" message
# Test commands in Discord: !hello, !ping, !info
```

## Architecture

### Core Structure
- **Single-file architecture**: The entire bot logic is contained in `bot.py`
- **Command-based design**: Uses discord.py's `commands.Bot` with prefix-based commands (`!`)
- **Environment-based configuration**: Bot token stored in `.env` file
- **Event-driven**: Responds to Discord events (`on_ready`, `on_message`) and commands

### Key Components
- **Bot initialization**: Sets up Discord intents and command prefix
- **Command handlers**: Three basic commands (`hello`, `ping`, `info`)
- **Event handlers**: Connection acknowledgment and message processing
- **Error handling**: Basic token validation and environment variable checking

### Dependencies
- `discord.py>=2.3.0`: Main Discord API wrapper
- `python-dotenv>=1.0.0`: Environment variable management

## Discord Bot Setup Requirements

When adding new functionality, ensure:
- Bot token is properly configured in `.env`
- Required Discord intents are enabled (message_content is already enabled)
- Commands follow the existing pattern with proper docstrings
- Embed responses use consistent color scheme (0x00ff00 for success)

## Environment Configuration

The bot requires:
- `DISCORD_TOKEN`: Your Discord bot token from the Discord Developer Portal
- Python 3.11+ (current version: 3.11.9)

## Deployment Notes

The README mentions several hosting platforms (Railway, Render, Heroku, Replit) for 24/7 operation. When deploying:
- Ensure environment variables are properly set on the hosting platform
- The bot expects to run continuously (`bot.run()` is blocking)
- No database or external services required for basic functionality