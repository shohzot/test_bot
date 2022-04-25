from telegram import *
from telegram.ext import *
from telebot import *
import database
from datetime import date


def startCommand(update: Update, context: CallbackContext):
    try:
        print(database.user_region.find_one({"id":update.effective_chat.id})["id"])
        main_menu = [[KeyboardButton("Online test"),KeyboardButton("Test buyurtma qilish")],[KeyboardButton("Natijalarni tekshirish"),KeyboardButton("Yo'riqnoma")],[KeyboardButton("Shaxsiy kabinet"),KeyboardButton("Mening natijalarim")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="Xush kelibsiz!",reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Assalomu alaykum, Oliygoh test platformasining maxsus telegram-botiga xush kelibsiz!\n\nUshbu bot orqali har hafta DTM standarti asosida BLOK TESTLAR bo'lib o'tadi")
        # main_menu = [[KeyboardButton(text="Raqamni yuborish",request_contact=True)]]
        # context.bot.send_message(chat_id=update.effective_chat.id, text="Platformadan foydalanish uchun raqamingizni tasdiqlang 👇",reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        context.bot.send_message(chat_id=update.effective_chat.id, text="Platformadan foydalanish uchun raqamingizni tasdiqlang 👇")
        
        
        
        







def message_handler(update: Update, context: CallbackContext):
    try:
        print(database.user_region.find_one({"id":update.effective_chat.id})["id"])
        if update.message.text=="Yo'riqnoma":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Assalomu Aleykum\n\nBu bot orqali siz har qanday fanlarni yaxshigina o'rganib tayyorlansayiz bo'ladi bularni barchasini biz bilan qo'lga kirita olasiz!\n\nAgarda siz bu botni qanday ishlatishni soragan bo'lsangiz bu juda oddiy bu botda har hafta tekin online test bo'ladi buning uchun sizlarga 3 soat vaqt ajratilib beriladi!")
        elif update.message.text == "Shaxsiy kabinet":
            try:
                print(database.user_attempt.find_one({'id':update.effective_chat.id})['attempt'])
                print(database.user_balans.find_one({'id':update.effective_chat.id})['balans'])
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"Shaxsiy ma'lumotlar\n\nIsmi Familiya: {database.user_fullname.find_one({'id':update.effective_chat.id})['fullname']}\nTelefon nomeri: {database.user_ph_number.find_one({'id':update.effective_chat.id})['number']}\nYashash hududi: {database.user_region.find_one({'id':update.effective_chat.id})['region']}\n\nQo'shimcha ma'lumotlar\n\nNechi marta testga qatnashgani: {database.user_attempt.find_one({'id':update.effective_chat.id})['attempt']}\nBalans: {database.user_balans.find_one({'id':update.effective_chat.id})['balans']} so'm")
            except:
                try:
                    print(database.user_attempt.find_one({'id':update.effective_chat.id})['attempt'])
                    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Shaxsiy ma'lumotlar\n\nIsmi Familiya: {database.user_fullname.find_one({'id':update.effective_chat.id})['fullname']}\nTelefon nomeri: {database.user_ph_number.find_one({'id':update.effective_chat.id})['number']}\nYashash hududi: {database.user_region.find_one({'id':update.effective_chat.id})['region']}\n\nQo'shimcha ma'lumotlar\n\nNechi marta testga qatnashgani: {database.user_attempt.find_one({'id':update.effective_chat.id})['attempt']}\nBalans: 0 so'm")
                except:
                    try:
                        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Shaxsiy ma'lumotlar\n\nIsmi Familiya: {database.user_fullname.find_one({'id':update.effective_chat.id})['fullname']}\nTelefon nomeri: {database.user_ph_number.find_one({'id':update.effective_chat.id})['number']}\nYashash hududi: {database.user_region.find_one({'id':update.effective_chat.id})['region']}\n\nQo'shimcha ma'lumotlar\n\nNechi marta testga qatnashgani: 0\nBalans: {database.user_balans.find_one({'id':update.effective_chat.id})['balans']} so'm")
                    except:
                        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Shaxsiy ma'lumotlar\n\nIsmi Familiya: {database.user_fullname.find_one({'id':update.effective_chat.id})['fullname']}\nTelefon nomeri: {database.user_ph_number.find_one({'id':update.effective_chat.id})['number']}\nYashash hududi: {database.user_region.find_one({'id':update.effective_chat.id})['region']}\n\nQo'shimcha ma'lumotlar\n\nNechi marta testga qatnashgani: 0\nBalans: 0 so'm")
        elif update.message.text == "Natijalarni tekshirish":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Natijalarni tekshirish uchun quyidagi formatda kiriting bo'lmasa sizning kiritgan variantlariz to'g'ri kelmasligi mumkin!\n\n\nMasalan: 000001*AAAAAAAA...  (000001 - bu test savoli raqami) \nshu holatda kiritilsa bo'ladi.")
        elif update.message.text == "Online test":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Online testda qatnashish uchun kerakli vaqtni tanlab registratsiya qilib qo'ying!")
            keyboard = [[InlineKeyboardButton('18:00',callback_data='18:00'),InlineKeyboardButton('21:00',callback_data='21:00')]]
            update.message.reply_text(database.user_fullname.find_one({'id':update.effective_chat.id})['fullname'],reply_markup=InlineKeyboardMarkup(keyboard))
               
        else:  
            context.bot.send_message(chat_id=update.effective_chat.id, text="Xato tarzda kiritildi!!!")              
    except:
        try:
            print(database.user_fullname.find_one({"id":update.effective_chat.id})["fullname"])
            database.user_reg(update.effective_chat.id,update.message.text)   
            main_menu = [[KeyboardButton("Online test"),KeyboardButton("Test buyurtma qilish")],[KeyboardButton("Natijalarni tekshirish"),KeyboardButton("Yo'riqnoma")],[KeyboardButton("Shaxsiy kabinet"),KeyboardButton("Mening natijalarim")]]
            context.bot.send_message(chat_id=update.effective_chat.id, text="Xush kelibsiz!",reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        except:
            try:
                print(database.user_ph_number.find_one({"id":update.effective_chat.id})["number"])
                database.user_full(update.effective_chat.id,update.message.text)
                context.bot.send_message(chat_id=update.effective_chat.id, text="Hududingizni tanlang!")
            except:    
                database.user_ph_number_func(update.effective_chat.id, update.message.text)
                context.bot.send_message(chat_id=update.effective_chat.id, text="Ism va Familiyangizni to'liq kiriting.\n(Masalan: Nurullayev Shohzot)")
        
        
        






def button(update: Update, context: CallbackContext) -> None:
    try:
        print(database.user_test_dates.find_one({'id':update.effective_chat.id})['name'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Siz allaqachon registratsiya qilingansiz!\n\n\nSizning bo'limingiz [{database.user_test_dates.find_one({'id':update.effective_chat.id})['dates']}]")
    except:
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=f"Sizning tanlovingiz: {update.callback_query.data}")
        database.user_dates(database.user_fullname.find_one({'id':update.effective_chat.id})['id'],database.user_fullname.find_one({'id':update.effective_chat.id})['fullname'],update.callback_query.data.split()[0]) 
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{database.user_fullname.find_one({'id':update.effective_chat.id})['fullname']} siz registratsiya qilindingiz!\n\n\nSizning bo'limingiz [{update.callback_query.data.split()[0]}]")
        
        
        
    
    
    
    
    