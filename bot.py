import telebot 
# توکن ربات تلگرام خود را در این قسمت قرار دهید 
TOKEN = '6383331646:AAEiZbQn1EDTSLQP0mBx-13LHjxxJn4tjjc' 
# ساخت شی از کلاس تلگرام برای ربات 
bot = telebot.TeleBot(TOKEN) # تعریف دکوریتور برای استقبال از دستور /start 
@bot.message_handler(commands=['start']) 
def send_welcome(message): 
  bot.reply_to(message, 'خوش آمدید!') 
# شروع گوش‌کردن ربات به پیام‌های دریافتی 
  bot.polling()
