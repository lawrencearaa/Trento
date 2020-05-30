import requests as requests
import random

url = "https://api.telegram.org/bot1231315957:AAG_sYHCOWxGPKpHxKtmr1iowV8zy2j8Lhs/"


#create a function that gets the chad id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


#create function that gets the message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


#create a function that gets the last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # gets the last record message update


#create function that lets the bot send a message to the user(reply)
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


#create main function for navigating or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower == "hello":
                send_message(get_chat_id(update), 'Hello Welcome to our bot. Type "Play" to roll the dice!')
            elif get_message_text(update).lower() == "play":
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                _3 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and' + str(_2) + ' and' + str(_3) + ' !\n Your result is ' + str(
                             _1 + _2 + _3) + '!!!')
            else:
                send_message(get_chat_id(update), "Sorry Not understand what you inputted:(")
            update_id += 1



# call the function to make it reply
main()
