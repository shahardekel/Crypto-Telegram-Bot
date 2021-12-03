from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from functions import get_crypto_balance, balance_btc, balance_eth, check_valid_general, check_QR

token_id='2127683555:AAHaU-i00adUh7oY80dUZaxS-uBYNt20bEU' # unique for every bot
NAME, GENERAL_ADDR, ADDR_btc, ADDR_eth, QR = range(5)

# Commands
def start(update: Update, context: CallbackContext):
    """Starts the conversation and asks the user about their name"""
    update.message.reply_text('Hi!🌈\nWhat is your name?')
    return NAME

# calls this function only after /start
def buttons(update: Update, context: CallbackContext):
    """Sends a greeting message with 6 inline choosing buttons attached"""
    user = update.message.text
    update.message.reply_text(f'Hi {user}!🙌🏽 I am the Crypto Bot!🤖\nYou can always go back with /menu .\n What do you want to know?')
    keyboard = [
        [
            InlineKeyboardButton("Current Bitcoin Currency💰", callback_data='1'),
            InlineKeyboardButton("Current Ethereum Currency💰", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Check My Bitcoin Adress🔑", callback_data='3'),
            InlineKeyboardButton("Check My Ethereum Adress🔑", callback_data='4')
        ],
        [
            InlineKeyboardButton("I don't know what coin I'm using!\n check my address and tell me!🔎", callback_data='5')
        ],
        [
            InlineKeyboardButton("Scan QR Code📸", callback_data='6')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('What do you want to know?', reply_markup=reply_markup)

    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    """Cancels and ends the conversation"""
    update.message.reply_text(
        '🤖 Leaving so soon? press /menu to go back, or /start for redo!\n See you soon!', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def menu(update: Update, context: CallbackContext):
    """Sends a message with 6 inline buttons attached"""
    keyboard = [
        [
            InlineKeyboardButton("Current Bitcoin Currency💰", callback_data='1'),
            InlineKeyboardButton("Current Ethereum Currency💰", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Check My Bitcoin Address🔑", callback_data='3'),
            InlineKeyboardButton("Check My Ethereum Address🔑", callback_data='4')
        ],
        [
            InlineKeyboardButton("I don't know what coin I'm using!\n check my address and tell me!🔎", callback_data='5')
        ],
        [
            InlineKeyboardButton("Scan QR Code📸", callback_data='6')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('What do you want to know?', reply_markup=reply_markup)

def button1(update: Update, context: CallbackContext):
    """calls the right functions for each button"""
    query = update.callback_query
    query.answer()
    if query.data=='1':
        query.edit_message_text(text="🤖 "+get_crypto_balance(coin="Bitcoin"))
    if query.data=='2':
        query.edit_message_text(text="🤖 "+get_crypto_balance(coin="Ethereum"))
    if query.data=='3':
        query.edit_message_text(text='🤖 to check your Bitcoin address, please click /check_btc')
    if query.data=='4':
        query.edit_message_text(text='🤖 to check your Bitcoin address, please click /check_eth')
    if query.data=='5':
        query.edit_message_text(text='🤖 to check your address, please click /check_general')
    if query.data=='6':
        query.edit_message_text(text='🤖 to check your QR code, click /scan_QR')


# commands for Bitcoin
def check_btc(update: Update, context: CallbackContext):
    update.message.reply_text('🤖 Enter your Bitcoin address')
    return ADDR_btc

def check_addr_btc(update: Update, context: CallbackContext):
    addr=update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=balance_btc(addr))



# commands for Ethereum
def check_eth(update: Update, context: CallbackContext):
    update.message.reply_text('🤖 Enter your Ethereum address')
    return ADDR_eth

def check_addr_eth(update: Update, context: CallbackContext):
    addr=update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=balance_eth(addr))



# commands for general addresses
def check_general(update: Update, context: CallbackContext):
    update.message.reply_text('🤖 Enter your address')
    return GENERAL_ADDR

def check_addr_general(update: Update, context: CallbackContext):
    addr=update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=check_valid_general(addr))



# commands for QR code scanner
def scan_QR(update: Update, context: CallbackContext):
    update.message.reply_text('🤖 please scan your QR code! you can take a photo or upload one')
    return QR

def decode_QR(update: Update, context: CallbackContext):
    qr_img = update.message.photo[-1].get_file()
    qr_img.download("output.jpg")
    context.bot.send_message(chat_id=update.effective_chat.id, text=check_QR("output.jpg"))


updater = Updater(token=token_id, use_context=True)
dispatcher = updater.dispatcher

