from tkinter import N


try:
    import telebot
    from telebot import *
    import urllib.request
    import time
    import os
    import requests
except:
    print('error')

token= '2096189305:AAFzKW6ubrAPnrHIybvIYUmJn2XckuYKG8w'
bot = telebot.TeleBot(token)
class A():
    @bot.message_handler(commands=['start'])
    def start(message, message2):
        for i in range(20):
            bot.send_message(message.chat.id,  'امرا وطاعة سيدي ايش تطلب؟')
            if message2.text == '^stop' or 'stop':
                break
    @bot.message_handler(regexp='^اريد الايدي يخدامي')
    def Id(message):
            bot.send_message(message.chat.id,  text='id :'+str(message.chat.id))
    @bot.message_handler(regexp='^بطل يالخدام')
    def any(message):
            bot.send_message(message.chat.id,  text='تهيني ورجلك على راسي سيدي')
    @bot.message_handler(regexp='^اريد ايدي هذا الولد')
    def any2(message):
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            bot.send_message(message.chat.id, text=id)
    @bot.message_handler(regexp='^اطلع برا')
    def any11(message):
        if message.from_user.id == 1626922754:
            bot.send_message(message.chat.id, text='bay ):')
            bot.leave_chat(message.chat.id)
        else:
            bot.send_message(message.chat.id, 'انت مو مشرف')
    @bot.message_handler(regexp='^rep')
    def stop(message):
        a = message.text.replace('rep',"")
        bot.send_message(message.chat.id, text='{}'.format(a))
                
    @bot.message_handler(commands=['hello', 'hi'])
    def hello(message):
        bot.send_message(message.chat.id, 'hello')

    @bot.message_handler(commands=['help'])
    def help(message):
        bot.send_message(message.chat.id, 'if you want to show the image type /img')

    @bot.message_handler(commands=['img'])
    def photo(message):
        bot.send_message(message.chat.id, 'Waiting...')
        while True:
            s = open('ss.jpg', 'rb')
            bot.send_photo(message.chat.id, s)
            time.sleep(5)
        
        
        #url = urllib.request.urlretrieve(message.text.replace('/jpg ', ''))
        #bot.send_message(message.chat.id, url)
        #bot.send_message(message.chat.id, 'Waiting...')


        #for i in os.listdir():
        #   if i.split('.')[-1]:
        #      print(i)
        #     bot.send_photo(message.chat.id, open(i, 'rb'))
            #    os.remove(i)





while True:
    try:
        bot.polling()
    except:
        time.sleep(5)

