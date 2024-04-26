from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time

def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text='VERIFY YOUR NOT ROBOT ✅', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("VERIFY", callback_data='verify')]]))

def callback_query(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    if query.data == 'verify':
        context.bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
        context.bot.send_message(chat_id=chat_id, text='Masukkan URL atau IP :')

def message(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    if text and not text.startswith('http://') and not text.startswith('https://'):
        context.bot.send_message(chat_id=chat_id, text='Tolong masukkan URL yang valid (dimulai dengan http:// atau https://)')
    else:
        context.bot.send_message(chat_id=chat_id, text='Tunggu sebentar...')
        start_time = time.time()
        # Lakukan proses pengiriman request ke URL atau IP disini
        # Contoh:
        time.sleep(2) # Contoh delay 2 detik
        end_time = time.time()
        result_time = int((end_time - start_time) * 1000)
        context.bot.send_message(chat_id=chat_id, text=f'Berapa MS resultnya: {result_time}ms')

def main():
    updater = Updater(token='7162012025:AAE1Ud8F_W3xzzJ4UXKqwF4dxaboz7pLEjQ', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(callback_query))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
                                   
