# ________________________________________________________
# ________________________________________________________
# packages and files:
from telebot import types
from localization.lang import *



# ________________________________________________________
# ________________________________________________________
# generate languages keyboards:
def generate_language():
    keyboard = types.InlineKeyboardMarkup()
    btn_uz = types.InlineKeyboardButton(text="🇺🇿Uz", callback_data="uz")
    btn_ar = types.InlineKeyboardButton(text="🇸🇦Ar", callback_data="ar")
    btn_en = types.InlineKeyboardButton(text="🇺🇸En", callback_data="en")
    btn_gr = types.InlineKeyboardButton(text="🇩🇪Gr", callback_data="gr")
    btn_fr = types.InlineKeyboardButton(text="🇫🇷Fr", callback_data="fr")
    keyboard.row(btn_uz, btn_ar, btn_en, btn_gr, btn_fr)
    return keyboard



# ________________________________________________________
# ________________________________________________________
# main menu keyboards:
def generate_main_menu(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_about = types.KeyboardButton(about_bot[lang])
    btn_connect = types.KeyboardButton(connect_lang[lang])
    btn_social = types.KeyboardButton(network[lang])
    btn_news = types.KeyboardButton(news_lang[lang])
    btn_idea = types.KeyboardButton(competitions[lang])
    btn_data = types.KeyboardButton(resurs_lang[lang])
    btn_back = types.KeyboardButton(change_lang[lang])
    keyboard.row(btn_about, btn_connect)
    keyboard.row(btn_social, btn_news)
    keyboard.row(btn_idea, btn_data)
    keyboard.row(btn_back)
    return keyboard



# ________________________________________________________
# ________________________________________________________
# back keyboard:
def generate_back(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_back = types.KeyboardButton(text=back_lang[lang])
    keyboard.row(btn_back)
    return keyboard



# ________________________________________________________
# ________________________________________________________
# biz bilan bog'laning keyboards:
def generate_connect(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_quest = types.KeyboardButton(text=quest_lang[lang])
    btn_location = types.KeyboardButton(text=location[lang])
    btn_back = types.KeyboardButton(text=back_lang[lang])
    keyboard.row(btn_quest, btn_location)
    keyboard.row(btn_back)
    return keyboard



# ________________________________________________________
# ________________________________________________________
# kanalga commit qilish uchun so'rov keyboards:
def commit(lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_yes = types.InlineKeyboardButton(text=yes_lang[lang], callback_data="yes")
    btn_no = types.InlineKeyboardButton(text=no_lang[lang], callback_data="no")
    keyboard.row(btn_yes, btn_no)
    return keyboard



# ________________________________________________________
# ________________________________________________________
# contact uchun keyboards:
def contact(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton(text=send_contact_lang[lang], request_contact=True)
    keyboard.row(btn)
    return keyboard




# ________________________________________________________
# ________________________________________________________
# social media keyboards:
def socialmedia(lang, url1, url2, url3, url4):
    keyboard = types.InlineKeyboardMarkup()
    btn_facebook = types.InlineKeyboardButton(text="Facebook", url=url1)
    btn_instagram = types.InlineKeyboardButton(text="Instagram", url=url2)
    btn_twitter = types.InlineKeyboardButton(text="Twitter", url=url3)
    btn_youtube = types.InlineKeyboardButton(text="YouTube", url=url4)
    btn_back = types.InlineKeyboardButton(text=back_lang[lang], callback_data="_back")
    keyboard.row(btn_facebook, btn_instagram)
    keyboard.row(btn_twitter, btn_youtube)
    keyboard.row(btn_back)
    return keyboard



# ________________________________________________________
# ________________________________________________________
# globalopportunities keyboards:
def globalopportunities(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_request = types.KeyboardButton(text=keyboard_lang[lang])
    btn_workplaces = types.KeyboardButton(text=job_prompts[lang])
    btn_opportunities = types.KeyboardButton(text=research_lang[lang])
    btn_back = types.KeyboardButton(text=back_lang[lang])
    keyboard.row(btn_request, btn_workplaces, btn_opportunities)
    keyboard.row(btn_back)
    return keyboard



# ________________________________________________________
# ________________________________________________________
# resource keyboards:
def generate_resource(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_request = types.KeyboardButton(text=educational_materials_lang[lang])
    btn_workplaces = types.KeyboardButton(text=keyboard_lang_path[lang])
    btn_opportunities = types.KeyboardButton(text="1")
    btn_back = types.KeyboardButton(text=back_lang[lang])
    keyboard.row(btn_request, btn_workplaces, btn_opportunities)
    keyboard.row(btn_back)
    return keyboard