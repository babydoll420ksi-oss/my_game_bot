import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- CONFIGURATION ---
# 1. Apna Bot Token yahan dalein
BOT_TOKEN = "8597887764:AAGEwvVQL2Zh6Dj8eiTamFZ8YI-bLpg1s6E" 

# 2. Render Deploy karne ke baad jo URL milega, wo yahan dalna hai
# Example: "https://your-game-name.onrender.com"
GAME_URL = "https://my-game-bot.onrender.com" 

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_game(message):
    markup = InlineKeyboardMarkup()
    btn_play = InlineKeyboardButton("🚀 Play Scrap Master", web_app=WebAppInfo(url=GAME_URL))
    markup.add(btn_play)
    
    bot.send_message(
        message.chat.id, 
        "<b>Welcome to Scrap Master!</b>\n\nTap, Earn, and Invite Friends! 💰\n\n👇 Click below to start:", 
        parse_mode="HTML", 
        reply_markup=markup
    )

print("Bot is running...")
bot.infinity_polling()
