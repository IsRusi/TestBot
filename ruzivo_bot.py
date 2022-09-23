from sken import sek
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime


bot = telebot.TeleBot(sek)


NowTime = datetime.datetime.now()
x = NowTime.strftime('%Y-%m-%d | %H:%M:%S')



Owner = '@Isrusi'



# keyboard buttons
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup
# callback anwer for button 
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")


 
@bot.message_handler(func=lambda message:True)
def InfoUser(message):
    #user's date
    userid= message.from_user.id # message.chat.id == message.from_user.id
    user_name= message.from_user.username
    if user_name == None:
        user_name = message.from_user.first_name
    mstext = message.text
    userbot = bot.get_me()

    # text for commands
    txt = (f"hello, i bot , my name is {userbot.first_name} \n")
    txt2 = (f'your name is {user_name}')
    txt1= (f'my owner is {Owner}')

    #logs
    print(f'\n1)message from id:', userid,'\n2)name:',user_name,'\n3)message:',mstext,'\n''4)time:',x)
    # commands
    if message.text == '/start':
        bot.send_message(userid,txt)
        

        bot.send_message(userid,txt2)
        bot.send_message(userid, 'Im right?', reply_markup=gen_markup())
    elif message.text == '/about':
        bot.send_message(userid,txt1)
    
    else:
        bot.send_message(userid,'wrong input')





bot.infinity_polling()