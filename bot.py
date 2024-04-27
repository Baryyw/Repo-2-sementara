import telebot
import time
import ping3

# Masukkan token bot Telegram Anda di sini
TOKEN = '7162012025:AAE1Ud8F_W3xzzJ4UXKqwF4dxaboz7pLEjQ'

# Inisialisasi bot
bot = telebot.TeleBot(TOKEN)

# Fungsi untuk menangani perintah /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = generate_markup()
    bot.send_message(message.chat.id, "VERIFY YOU'RE NOT A ROBOT:", reply_markup=markup)

# Fungsi untuk membuat tombol "VERIFY" dalam format yang diinginkan
def generate_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    verify_button = telebot.types.InlineKeyboardButton('VERIFY', callback_data='verify')
    markup.add(verify_button)
    return markup

# Fungsi untuk menangani callback dari tombol "VERIFY"
@bot.callback_query_handler(func=lambda call: call.data == 'verify')
def callback_verify(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)  # Hapus pesan "VERIFY YOU'RE NOT A ROBOT"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Masukkan IP atau URL:")

# Fungsi untuk menangani pesan teks dari pengguna
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    address = message.text
    bot.reply_to(message, "Tunggu sebentar..")
    try:
        response_time = ping3.ping(address)  # Ping alamat IP atau URL
        if response_time is not None:
           response_time_seconds = response_time * 1000  # Konversi ke detik
           bot.send_message(message.chat.id, f"Result: {response_time_seconds:.2f}ms")
        else:
           bot.send_message(message.chat.id, "Ping timeout")
    except ValueError:
        bot.send_message(message.chat.id, "Invalid address")

# Jalankan bot
bot.polling()
