> **Disclaimer**
this bot is currently under development it may still have bug and incompleted features.Use it at your own discretion and report any issues to help improve the project.

# Features
- Easy Setup
- Use a `config.json` for adjust
- Auto load commands or slash commands from cogs

# Requirements
- Python 3.8 or newer
- pip (comes with python)
- Bot token

## Tutorials
   ```bash
   git clone https://github.com/fleurdefontaine/discord-ticket-bot.git
   cd discord-ticket-bot
   ```

2. Install dependencies:
   ```bash
   npm i
   ```

3. Configure the bot:
   - Open Folder `src/`
   - Rename `config.example.json` to `config.json`
   - Fill in your bot token and other required fields

4. Start the bot:
   ```bash
   npm start
   ```

## Configuration

Edit `config.json` to customize your bot:

```json
{
  "token": "YOUR_BOT_TOKEN",
  "guildId": "YOUR_GUILD_ID",
  "ticketCategory": "TICKET_CATEGORY_ID",
  "staffRoles": ["STAFF_ROLE_ID_1", "STAFF_ROLE_ID_2"],
  "ticketLimit": 1,
  "settingsChannelId": "SETTINGS_CHANNEL_ID",
  "embedDescription": "Click the button below to create a new support ticket.",
  "buttonLabel": "Create Ticket"
}
```

## Commands

### /setup

Sets up the ticket system in a specified channel.

Usage:
```
/setup channel:#channel category:#category description:"Your description" button_label:"Create Ticket"
```

## Project Structure

```bash
discord-ticket-bot/
├── src/
│   ├── events/
│   │   ├── ready.js
│   │   └── interactionCreate.js
│   ├── commands/
│   │   └── setup.js
│   ├── utils/
│   │   └── ticketUtils.js
│   └── config.json
├── index.js
├── package.json
└── README.md
```
