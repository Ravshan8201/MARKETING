
import job_queue as job_queue
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, \
    CallbackContext
from func import *
from cons import *
from telegram.ext import CommandHandler, Updater
from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackContext
upd = Updater(TOKEN)
dis = upd.dispatcher
j = upd.job_queue
j.run_repeating(callback_timer, interval=60, first=1)
# job_queue.run_repeating(callback_timer,interval=10.0,first=0.0)
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CommandHandler(command='wwwwww', callback=wwwwww))
dis.add_handler(CommandHandler(command='get_date', callback=get_date))
dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))
upd.start_polling()
upd.idle()

