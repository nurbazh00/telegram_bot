# Telegram bot for weather
> ОПИСАНИЕ: Этот телеграм бот показывает погоду выбранного вами города
## Как поднять проект локально

```
git clone https://github.com/nurbazh00/telegram_bot.git
cd telegram_bot
cd envs
touch env.local // insert bot token to file
source env.local
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/base.txt
python telegram_bot_for_weather.py
```

## Необходимые программы
- Python 3