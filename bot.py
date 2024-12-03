#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# packages and files:
import os
import time
from telebot import TeleBot
from keyboards import *
from localization.lang import *
from dotenv import load_dotenv



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# from .env:
load_dotenv()
token = os.getenv("TOKEN")
bot = TeleBot(token)

user_data = {}
user_langs = {}
personal_details = {}
canal_id = os.getenv("CANAL_ID")
group_id = os.getenv("GROUP_ID")
instagram_link = os.getenv("INSTAGRAM_URL")
facebook_link = os.getenv("FACEBOOK_URL")
youtube_link = os.getenv("YOUTUBE_URL")
twitter_link = os.getenv("TWITTER_URL")



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# bot start:
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    photo = open("media/start_image.jpg", "rb")
    bot.send_photo(chat_id, photo, start_message[lang], reply_markup=generate_language())



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# select lang:
@bot.callback_query_handler(func=lambda call: call.data in ["uz", "ar","en", "gr","fr"])
def language(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if call.data == "uz":
        lang = "uz"

    elif call.data == "ar":
        lang = "ar"

    elif call.data == "en":
        lang = "en"

    elif call.data == "gr":
        lang = "gr"

    elif call.data == "fr":
        lang = "fr"


    bot.send_message(chat_id, choose_language[lang], reply_markup=generate_main_menu(lang))

    bot.register_next_step_handler(call.message, main_menu)
    user_langs[chat_id] = lang



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# main menu:
def main_menu(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    photo = open("media/vision.png", 'rb')

    # ________________________________________________________
    # ________________________________________________________
    # --about us(biz xaqimizda):
    if message.text == about_bot[lang]:
        bot.send_photo(chat_id, photo, caption=about_caption[lang],
                                                parse_mode="HTML", reply_markup=generate_back(lang))
        bot.register_next_step_handler(message, back)


    # --connect us(biz bilan bog'laning):
    elif message.text == connect_lang[lang]:
        bot.send_message(chat_id, connect_line_text[lang], reply_markup=generate_connect(lang))
        bot.register_next_step_handler(message, connect)

    # --network(social media):
    elif message.text == network[lang]:
        bot.send_message(chat_id, text_network[lang], reply_markup=socialmedia(lang, facebook_link, instagram_link, twitter_link, youtube_link))
        bot.register_next_step_handler(message, back)

    # --news(yangiliklar):
    elif message.text == news_lang[lang]:
        bot.send_message(chat_id, news_lang[lang], reply_markup=globalopportunities(lang))
        bot.register_next_step_handler(message, news)

    # --competitions(musaboqlar):
    elif message.text == competitions[lang]:
        bot.send_message(chat_id, chalange[lang])
        time.sleep(1)
        bot.send_message(chat_id, category[lang], reply_markup=generate_main_menu(lang))

    # --resources(yoshlar uchun resurslar):
    elif message.text == resurs_lang[lang]:
        bot.send_message(chat_id, message.text, reply_markup=generate_resource(lang))
        bot.register_next_step_handler(message, news)

    # --select lang(tilni o'zgartirish)::
    elif message.text == change_lang[lang]:
        return start(message)



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# connect us(biz bilan bo'glaning):
def connect(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text == location[lang]:
        bot.send_message(chat_id, location[lang])
        bot.send_location(chat_id, latitude=40.86091, longitude=69.58965, reply_markup=generate_back(lang))
        bot.register_next_step_handler(message, back_connect)

    elif message.text == quest_lang[lang]:
        bot.send_message(chat_id, question_lang[lang])
        bot.register_next_step_handler(message, user_name)


    elif message.text == back_lang[lang]:
        return back(message)


# --savol va so'rovlar:
def user_name(message):
    quest = message.text
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.send_message(chat_id, fio_lang[lang])
    bot.register_next_step_handler(message, user_question, quest)

def user_question(message, quest):
    name = message.text
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.send_message(chat_id, phone_number_lang[lang], reply_markup=contact(lang))
    bot.register_next_step_handler(message, send_group_message, name, quest)

# --sorovlarni gruppaga yuborish:
def send_group_message(message, name, quest):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text:
        phone = message.text
        personal_details['name'] = name
        personal_details['quest'] = quest
        personal_details['phone'] = phone
        bot.send_message(chat_id, f"{confirm_lang[lang]} {name}\n"
                                  f"{quest_offer_lang[lang]}{quest}\n"
                                  f"{user_phone_number_lang[lang]} {phone}", reply_markup=commit(lang))

    elif message.contact:
        phone = message.contact.phone_number
        personal_details['name'] = name
        personal_details['quest'] = quest
        personal_details['phone'] = phone
        bot.send_message(chat_id, f"{confirm_lang[lang]} {name}\n"
                                  f"{quest_offer_lang[lang]}{quest}\n"
                                  f"{user_phone_number_lang[lang]} {phone}", reply_markup=commit(lang))


# --so'rov yuborilsinmi yes or no:
@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no"])
def message_commit(call):
    chat_id = call.message.chat.id
    name = personal_details['name']
    quest = personal_details['quest']
    phone = personal_details['phone']
    lang = user_langs.get(chat_id, "uz")

    if call.data == 'yes':
        bot.send_message(chat_id, information_received_lang[lang])
        bot.send_message(canal_id, f"{confirm_lang[lang]} {name}\n"
                                  f"{quest_offer_lang[lang]}{quest}\n"
                                  f"{user_phone_number_lang[lang]} {phone}")
        time.sleep(3)
        bot.send_message(chat_id, choose_language[lang], reply_markup=generate_main_menu(lang))
        bot.register_next_step_handler(call.message, main_menu)

    elif call.data == "no":
        bot.send_message(chat_id, connect_line_text[lang], reply_markup=generate_connect(lang))
        bot.register_next_step_handler(call.message, connect)



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# ijtimoiy tarmoqlar(social network):
def social_media(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text == back_lang[lang]:
        return back(message)


# --back to connect:
def back_connect(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text == back_lang[lang]:
        bot.send_message(chat_id, connect_line_text[lang], reply_markup=generate_connect(lang))
        bot.register_next_step_handler(message, connect)

# --back main menu func:
def back(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == back_lang[lang]:
        bot.send_message(chat_id, choose_language[lang], reply_markup=generate_main_menu(lang))

        bot.register_next_step_handler(message, main_menu)



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# news(yangiliklar):
def news(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    bot.send_message(chat_id, choose_language[lang], reply_markup=generate_main_menu(lang))
    bot.register_next_step_handler(message, main_menu)



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# (competitions)musaboqa:
def send_answer_tournament(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    username = message.from_user.username
    bot.send_message(chat_id, accept_answer_lang[lang])
    bot.send_message(group_id, f"Savol @{username}:\n\n{message.text}")
    time.sleep(2)
    bot.send_message(chat_id, choose_language[lang], reply_markup=generate_main_menu(lang))
    bot.register_next_step_handler(message, main_menu)



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# inline keyboards:
@bot.callback_query_handler(func=lambda call: call.data == "siyrat")
def siyrat_inline(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.send_message(chat_id, question_lang[lang])
    bot.register_next_step_handler(call.message, send_answer_tournament)


# --orqaga qaytish uchun main inline func:
@bot.callback_query_handler(func=lambda call: call.data == "_back")
def back_inline(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    bot.send_message(chat_id, choose_language[lang], reply_markup=generate_main_menu(lang))

    bot.register_next_step_handler(call.message, main_menu)





#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________
# bot run:
bot.polling(non_stop=True)