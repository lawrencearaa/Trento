from flask import Flask, Response
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
import requests

bot_token = '1231315957:AAG_sYHCOWxGPKpHxKtmr1iowV8zy2j8Lhs'

app = Flask(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.message.from_user.id, text="Hi! Welcome...")
    
def translate(update, context):
	# merging all the words passed from the user
    text = ' '.join(context.args)  # ['hello', 'world'] -> 'hello world'
    context.bot.send_message(chat_id=update.message.from_user.id, text="Translating '" + text + "'")
    
    #route to source_langauge service
    url = 'http://127.0.0.1:5004/language'
    myobj = {
         'user_id': update.message.from_user.id
    }

    res = requests.get(url, params=myobj)    
    src_lang = res.json()['retreived']
    
    #route to destination_langauge service
    url = 'http://127.0.0.1:5003/language'
    myobj = {
         'user_id': update.message.from_user.id
    }

    res = requests.get(url, params=myobj)    
    dest_lang = res.json()['retreived']
    
    # route to the translation service
    url = 'http://127.0.0.1:5002/translate'
    myobj = {
         'text': text,
         'dest_lang': dest_lang,
         'src_lang' : src_lang
    }

    res = requests.post(url, data=myobj)
    # read the json response
    translated = res.json()['response']
    context.bot.send_message(chat_id=update.message.from_user.id, text=translated)

def dest_language(update, context):
	# getting user prefered destination language
    lang = context.args[0]  # ['it'] -> 'it'
    
    # route to the language service
    url = 'http://127.0.0.1:5003/language'
    myobj = {
         'user_id': update.message.from_user.id,
         'dest_lang': lang
    }

    res = requests.post(url, data=myobj)
    context.bot.send_message(chat_id=update.message.from_user.id, text='Selected langauge: ' + lang)
    
def src_language(update, context):
	# getting user prefered destination language
    lang = context.args[0]  # ['it'] -> 'it'
    
    # route to the language service
    url = 'http://127.0.0.1:5004/language'
    myobj = {
         'user_id': update.message.from_user.id,
         'src_lang': lang
    }

    res = requests.post(url, data=myobj)
    context.bot.send_message(chat_id=update.message.from_user.id, text='Selected langauge: ' + lang)
    
def list_languages(update, context):
	# getting user prefered destination language
    languages = ' '.join(context.args)  # ['it'] -> 'it'
    
    # route to the language service
    url = 'http://127.0.0.1:5005/list'
    myobj = {
         'user_id': update.message.from_user.id,
         'list_lang': languages
    }

    res = requests.post(url, data=myobj)
    context.bot.send_message(chat_id=update.message.from_user.id, text='Supported langauges: ' + languages)    
    

def init_bot():
    updater = Updater(token=bot_token, use_context=True)

    dispatcher = updater.dispatcher

    # let accept "/start" messages from the bot
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # let accept "/translate ..." from the bot
    translate_handler = CommandHandler('translate', translate)
    dispatcher.add_handler(translate_handler)
    
    # let accept "/dest_language ..." from the bot
    dest_lang_handler = CommandHandler('dest_language', dest_language)
    dispatcher.add_handler( dest_lang_handler)
    
    # let accept "/src_language ..." from the bot
    src_lang_handler = CommandHandler('src_language', scr_language)
    dispatcher.add_handler( src_lang_handler)
    
     # let accept "/list_languages ..." from the bot
    list_handler = CommandHandler('list_languages', list_languages)
    dispatcher.add_handler(list_handler)

    return updater
    
updater = init_bot()

@app.route('/start', methods=['GET', 'POST'])
def start():
	# start the telegram bot
	updater.start_polling()
	return Response('{"running":true}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
