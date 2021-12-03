from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
import bot

"""
BEFORE RUNNING THE BOT, PLEASE READ THE README.TXT FILE
THANKS! AND HAVE FUN!
"""

def main():
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=bot.token_id, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', bot.start)],
        states={
            bot.NAME: [MessageHandler(Filters.text & ~Filters.command, bot.buttons)],
        },
        fallbacks=[CommandHandler('cancel', bot.cancel)]
    )
    dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('menu', bot.menu))
    updater.dispatcher.add_handler(CallbackQueryHandler(bot.button1))
    conv_handler1 = ConversationHandler(
        entry_points=[CommandHandler('check_btc', bot.check_btc),CommandHandler('check_eth', bot.check_eth),
                      CommandHandler('check_general', bot.check_general), CommandHandler('scan_QR',bot.scan_QR)],
        states={
            bot.ADDR_btc: [MessageHandler(Filters.text & ~Filters.command, bot.check_addr_btc)],
            bot.ADDR_eth: [MessageHandler(Filters.text & ~Filters.command, bot.check_addr_eth)],
            bot.GENERAL_ADDR: [MessageHandler(Filters.text & ~Filters.command, bot.check_addr_general)],
            bot.QR: [MessageHandler(Filters.photo, bot.decode_QR)],
        },
        fallbacks=[CommandHandler('cancel', bot.cancel)]
    )
    dispatcher.add_handler(conv_handler1)


    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    updater.idle()


if __name__ == '__main__':
    main()