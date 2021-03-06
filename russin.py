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




api_key = "1993871770:AAFhe5p8GCCSa0IB5jvmWHwuMnx0vNvoww4";
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

    ?? = recived_text.replace("??", "A")
    ?? = ??.replace("a", "a")

    ?? = ??.replace("??", "B")
    ?? = ??.replace("??", "b")

    ?? = ??.replace("??", "V")
    ?? = ??.replace("??", "v")

    ?? = ??.replace("??", "G")
    ?? = ??.replace("??", "g")

    ???? = ??.replace("????", "J")
    ???? = ????.replace("????", "J")
    ???? = ????.replace("????", "j")
    ???? = ????.replace("????", "j")

    ?? = ????.replace("??", "D")
    ?? = ??.replace("??", "d")

    ?? = ??.replace("??", "Ye")
    ?? = ??.replace("??", "ye")

    ?? = ??.replace("??", "Yo")
    ?? = ??.replace("??", "yo")

    ?? = ??.replace("??", "Z")
    ?? = ??.replace("??", "z")

    ?? = ??.replace("??", "I")
    ?? = ??.replace("??", "i")

    ?? = ??.replace("??", "Y")
    ?? = ??.replace("??", "y")

    ?? = ??.replace("??", "K")
    ?? = ??.replace("??", "k")

    ?? = ??.replace("??", "L")
    ?? = ??.replace("??", "l")

    ?? = ??.replace("??", "M")
    ?? = ??.replace("??", "m")

    ?? = ??.replace("??", "N")
    ?? = ??.replace("??", "n")

    ?? = ??.replace("??", "O")
    ?? = ??.replace("??", "o")

    ?? = ??.replace("??", "P")
    ?? = ??.replace("??", "p")

    ?? = ??.replace("??", "R")
    ?? = ??.replace("??", "r")

    ?? = ??.replace("??", "S")
    ?? = ??.replace("??", "s")

    ?? = ??.replace("??", "T")
    ?? = ??.replace("??", "t")

    ?? = ??.replace("??", "U")
    ?? = ??.replace("??", "u")

    ?? = ??.replace("??", "F")
    ?? = ??.replace("??", "f")

    ?? = ??.replace("??", "H")
    ?? = ??.replace("??", "h")

    ?? = ??.replace("??", "Sh")
    ?? = ??.replace("??", "Sh")

    ?? = ??.replace("??", "Ch")
    ?? = ??.replace("??", "ch")

    ?? = ??.replace("??", "Sh")
    ?? = ??.replace("??", "sh")

    ?? = ??.replace("??", "sh")
    ?? = ??.replace("??", "sh")

    ?? = ??.replace("??", "Th")
    ?? = ??.replace("??", "th")

    ?? = ??.replace("??", "yo")
    ?? = ??.replace("??", "yo")

    ?? = ??.replace("??", "Th")
    ?? = ??.replace("??", "th")

    ?? = ??.replace("??", "E")
    ?? = ??.replace("??", "e")

    ?? = ??.replace("??", "U")
    ?? = ??.replace("??", "u")

    ?? = ??.replace("??", "Ya")
    ?? = ??.replace("??", "ya")


    result = ??
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

#     #setting up the webhook
#     updater.start_webhook(listen="0.0.0.0",
#                           port=int(PORT),
#                           url_path=api_key)
#     updater.bot.setWebhook(server_url_with_https,api_key)


if __name__ == '__main__':
    main()
