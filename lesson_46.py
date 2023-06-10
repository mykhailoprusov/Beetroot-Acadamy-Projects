import telegram.ext

with open('token', 'r') as api:
    TOKEN = api.read()

def start(update, context):
    update.message.reply_text("Hello! Welcome to my telegram Bot!")


def help(update, context):
    update.message.reply_text("""Available commands:
            /start
            /help
            /content
            /contact
    """)

def content(update, context):
    update.message.reply_text("There will be content in the future")

def contact_info(update, context):
    update.message.reply_text("You can contact me via gmail")


def handle_message(update,context):
    update.message.reply_text(f"You said: {update.message.text}")

def error_handler_fuction(update,context):
    print(f"Update: {update} caused error: {context.error}")

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.CommandHandler("content",content))
disp.add_handler(telegram.ext.CommandHandler("contact",contact_info))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message))

disp.add_error_handler(error_handler_fuction)
updater.start_polling()
updater.idle()
