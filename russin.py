#!/usr/bin/python3.9
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
#with webhook

"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
import os




api_key = "1909966279:AAH0h8_gqhXVe8yfJx4YUSMMH4aMEPq9NRc";
server_url_with_https = "https://pawanvikasitha.pythonanywhere.com/";


updater = Updater(token=api_key)
dispatcher = updater.dispatcher
PORT = int(os.environ.get('PORT', 80))


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def echo(update,context):
    user = update.effective_user
    first_name = user.first_name
    if first_name == "TOKIO":
        recived_text = update.message.text



    recived_text.encode('unicode_escape')

    А = recived_text.replace("А", "A")
    а = А.replace("a", "a")

    Б = а.replace("Б", "B")
    б = Б.replace("б", "b")

    В = б.replace("В", "V")
    в = В.replace("в", "v")

    Г = в.replace("Г", "G")
    г = Г.replace("г", "g")

    ДЖ = г.replace("ДЖ", "J")
    Дж = ДЖ.replace("Дж", "J")
    дЖ = Дж.replace("дЖ", "j")
    дж = дЖ.replace("дж", "j")

    Д = дж.replace("Д", "D")
    д = Д.replace("д", "d")

    Е = д.replace("Е", "Ye")
    е = Е.replace("е", "ye")

    Ё = е.replace("Ё", "Yo")
    ё = Ё.replace("ё", "yo")

    З = ё.replace("З", "Z")
    з = З.replace("з", "z")

    И = з.replace("И", "I")
    и = И.replace("и", "i")

    Й = и.replace("Й", "Y")
    й = Й.replace("й", "y")

    К = й.replace("К", "K")
    к = К.replace("к", "k")

    Л = к.replace("Л", "L")
    л = Л.replace("л", "l")

    М = л.replace("М", "M")
    м = М.replace("м", "m")

    Н = м.replace("Н", "N")
    н = Н.replace("н", "n")

    О = н.replace("О", "O")
    о = О.replace("о", "o")

    П = о.replace("П", "P")
    п = П.replace("п", "p")

    Р = п.replace("Р", "R")
    р = Р.replace("р", "r")

    С = р.replace("С", "S")
    с = С.replace("с", "s")

    Т = с.replace("Т", "T")
    т = Т.replace("т", "t")

    У = т.replace("У", "U")
    у = У.replace("у", "u")

    Ф = у.replace("Ф", "F")
    ф = Ф.replace("ф", "f")

    Х = ф.replace("Х", "H")
    х = Х.replace("х", "h")

    Ц = х.replace("Ц", "Sh")
    ц = Ц.replace("ц", "Sh")

    Ч = ц.replace("Ч", "Ch")
    ч = Ч.replace("ч", "ch")

    Ш = ч.replace("Ш", "Sh")
    ш = Ш.replace("ш", "sh")

    Щ = ш.replace("Щ", "sh")
    щ = Щ.replace("щ", "sh")

    Ъ = щ.replace("Ъ", "Th")
    ъ = Ъ.replace("ъ", "th")

    Ы = ъ.replace("Ы", "yo")
    ы = Ы.replace("ы", "yo")

    Ь = ы.replace("Ь", "Th")
    ь = Ь.replace("ь", "th")

    Э = ь.replace("Э", "E")
    э = Э.replace("э", "e")

    Ю = э.replace("Ю", "U")
    ю = Ю.replace("ю", "u")

    Я = ю.replace("Я", "Ya")
    я = Я.replace("я", "ya")


    result = я
    update.message.reply_text(result)




def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')



def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(api_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))


    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    #setting up the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=api_key)
    updater.bot.setWebhook(server_url_with_https,api_key)


if __name__ == '__main__':
    main()