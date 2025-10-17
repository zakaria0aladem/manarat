from telegram import Bot
import asyncio
from datetime import datetime
import csv

BOT_TOKEN = "8415783103:AAFyQi7w05NDSlaxwW6u5-MJfowavN9l_5A"
CHANNEL_ID = "-1002618330740"  # or "@YourChannelUsername"
CSV_FILE = r"C:\Users\zakar\Downloads\test - Sheet1.csv"

# Load messages from CSV
def load_messages():
    messages = []
    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            messages.append(row["message"])
    return messages

async def send_message(message: str):
    bot = Bot(token=BOT_TOKEN)
    date = datetime.now().strftime("%Y-%m-%d")
    full_message = f"{message}\n🕰️ التاريخ: {date}"
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=full_message)
        print(" Message sent:", full_message)
    except Exception as e:
        print(" Failed to send message:", e)

async def scheduler():
    messages = load_messages()
    while True:
        now = datetime.now()
        # Change hour and minute to your desired sending time
        if now.hour == 15 and now.minute == 55:
            # Pick message based on the day number
            day_index = (now.toordinal() - 738156) % len(messages)
            await send_message(messages[day_index])
            await asyncio.sleep(60)  # avoid sending twice in the same minute
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(scheduler())
