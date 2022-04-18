# TeoranTranslate

Discord bot that translates English into Teoran, The language of Gwain Saga

![ExampleGif](https://i.imgur.com/ciPpQNk.gif)

[Add to your server!](https://discordapp.com/oauth2/authorize?&client_id=949112039329132616&scope=bot)

## Configuration

download TeoranTranslate.py and TeoranTranslateData.py. put them in the same directory.

Teoran_emojis folder is not required for bot to function.

install the discord.py package using pip

Run TeoranTranslate.py

Config.json is created automatically on launch of TeoranTranslateBot.py.
bot token is in config.json
Prefix is adjustable in config.json. Default prefix is "$"
If you would like DmLogging set it to "True" and
put your discord userid in config.json

## Usage

Send a command in a server the bot is in or in a direct message
### Translate Commands
- `$translate "string"` : Main command of bot, translates anything in quotes into Teoran
- `$translateRaw "string"` : Translates a string into Teoran emoji ids (for copying with nitro)
- `$translateEasy "string"` : Translates a string into easy to read Teoran.
- `$translateRev "string"` : Translates Teoran into English
### Other Commands
- `$help` : Echoes help message
- `$ping` : Echoes latency
- `$echo "string"` : Echoes anything you put in quotes
- `$uptime` : Echoes uptime of bot
### Examples
Correct:

`$translate "Geo Ami"` translates "Geo Ami".

`$translate Gwain` translates "Gwain".

Incorrect:

`$translate "Marlow" "Deva"` only translates "Marlow".

`$translate Lanney Agni` only translates "Lanney".

Supports any char on keyboard.

Does not support fancy quotes or apostrophes.

## Credits

If you would like to use this code just credit me somewhere. Then you can do whatever you like

- [Python: Make a Discord bot](https://www.youtube.com/watch?v=bq80J5rh4Cc). used for learning basic structure of discord.py
- [Teoran font](https://fontstruct.com/fontstructions/show/1833685/teoran-font-v1-04). Used for the emojis
- Teoran alphabet, made by [GeoExe](https://www.youtube.com/c/GeoExeofficial)  
The Teoran alphabet is from the [Gwain Saga Animated Series](https://www.youtube.com/channel/UCI-vHWeZmN-9m5ia10ryT4Q). I recommend watching it, its pretty cool :D


## Contact me

Contact me at Gibgib52#6473 on discord.

## Other things

I used GIMP to manually make 128x128 .png's of each Teoran letter for use as a discord emoji.
