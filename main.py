
from dotenv import load_dotenv
import os
import telebot
from telebot import types

load_dotenv('token.env')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(bot_token);


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇺🇦 Українська')
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇺🇦 Оберіть мову / 🇬🇧 Choose your language", reply_markup=markup)


# Українська
@bot.message_handler(func=lambda message: message.text == "🇺🇦 Українська")
def get_ukrainian(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('📰 Про нас')
    btn2 = types.KeyboardButton('🛠 Часті запитання')
    btn3 = types.KeyboardButton('📚 Реєстрація')
    btn4 = types.KeyboardButton('📣 Виклик адміністратора')
    btn5 = types.KeyboardButton('🔙 Return to language selection')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, "👋 Вас вітає бот проєкту StudySynchronize", reply_markup=markup)
    bot.send_message(message.from_user.id, '👀 Оберіть розділ')

@bot.message_handler(func=lambda message: message.text == '📰 Про нас')
def about_us_ukrainian(message):
    about_text = """
    📚 StudySynchronize- це платформа для спільного навчання за технологією помодоро. Ми створили цей проєкт, щоб забезпечити можливість людям зібратися в маленькі групи та разом вчитися, використовуючи методику ефективного управління часом.

    Наш проєкт надає можливості:

    🤝 Приєднатися до групи навчання та знайти однодумців зі схожими інтересами та навчальними потребами.
    🎥 Використовувати технологію вебкамер для візуального зв'язку з іншими учасниками групи.
    ⏱ Навчатися за методикою помодоро, розділяючи свій час на періоди роботи і відпочинку для максимальної продуктивності.
    📊 Зберігати свої досягнення та відстежувати свій прогрес у навчанні.

    Ми віримо, що спільне навчання та використання технології помодоро допоможе кожному учаснику досягти своїх навчальних цілей та підвищити ефективність свого навчання. Долучайтесь до StudySyncronize та почніть здобувати нові знання разом з нами!
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Повернутись назад')
    markup.add(btn1)
    bot.send_message(message.chat.id, about_text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '🛠 Часті запитання')
def faq_ukrainian(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Що таке технологія навчання "Pomodoro"?', callback_data='q1_ukrainian')
    btn2 = types.InlineKeyboardButton('Яким чином буде відбуватись навчання?', callback_data='q2_ukrainian')
    markup.add(btn1, btn2)
    btn_back = types.KeyboardButton('🔙 Повернутись назад')
    bot.send_message(message.chat.id, "📚 Найчастіші запитання", reply_markup=markup)
    bot.send_message(message.chat.id, "Натисніть на запитання для отримання відповіді.",  reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back))


@bot.message_handler(func=lambda message: message.text == '📚 Реєстрація')
def reg_ukrainian(message):
    reg_text = """
    Скоро
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Повернутись назад')
    markup.add(btn1)
    bot.send_message(message.chat.id, reg_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📣 Виклик адміністратора')
def call_ukrainian(message):
    call_text = """
    Скоро
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Повернутись назад')
    markup.add(btn1)
    bot.send_message(message.chat.id, call_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔙 Return to language selection')
def return_language_ukrainian(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇺🇦 Українська')
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇺🇦 Оберіть мову / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔙 Повернутись назад')
def return_to_menu_ukrainian(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('📰 Про нас')
    btn2 = types.KeyboardButton('🛠 Часті запитання')
    btn3 = types.KeyboardButton('📚 Реєстрація')
    btn4 = types.KeyboardButton('📣 Виклик адміністратора')
    btn5 = types.KeyboardButton('🔙 Return to language selection')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, '👀 Оберіть розділ', reply_markup=markup)




# FAQ_ukrainian
@bot.callback_query_handler(func=lambda call: call.data == 'q1_ukrainian')
def q1_ukrainian(call):
    faq_text = """
    Технологія навчання "Pomodoro" - ⏳ це методика управління часом, яка допомагає покращити продуктивність та зосередженість шляхом розділення часу на періоди активної роботи і коротких перерв. 
    Основна ідея полягає в тому, щоб працювати протягом певного періоду (зазвичай 25 хвилин), а потім робити коротку перерву (зазвичай 5 хвилин). Після кількох циклів роботи і перерви робиться довша перерва, наприклад, 15-30 хвилин. 
    Цей метод дозволяє зберігати високу концентрацію уваги протягом тривалого часу, а також запобігає втомі і перенавантаженню мозку.
    """
    bot.send_message(call.message.chat.id, faq_text)

@bot.callback_query_handler(func=lambda call: call.data == 'q2_ukrainian')
def q2_ukrainian(call):
    faq_text = """
    🌐 Наш онлайн навчальний курс відбуватиметься у форматі Discord. 
    Після реєстрації ви матимете можливість обрати приєднатися до існуючих груп або створити власну. 
    Приєднавшись до групи, ви матимете змогу взаємодіяти з одногрупниками через веб-камеру, що створить ефективне візуальне зв'язок та допоможе вам зберегти дисципліну під час навчання. 
    Мікрофон буде автоматично вимкнено, а чат відключений, щоб максимально сконцентрувати вас на навчанні.
    """
    bot.send_message(call.message.chat.id, faq_text)





# Англійська

@bot.message_handler(func=lambda message: message.text == "🇬🇧 English")
def get_english(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('📰 About us')
    btn2 = types.KeyboardButton('🛠 FAQ')
    btn3 = types.KeyboardButton('📚 Registration')
    btn4 = types.KeyboardButton('📣 Call the administrator')
    btn5 = types.KeyboardButton('🔙 Повернутись до вибору мови')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, "👋 Welcome to the StudySynchronize project bot.", reply_markup=markup)
    bot.send_message(message.from_user.id, '👀 Choose a section')

@bot.message_handler(func=lambda message: message.text == '📰 About us')
def about_us_english(message):
    about_text = """
    📚 StudySynchronize is a platform for collaborative learning using the Pomodoro technique. We've created this project to provide people with the opportunity to gather in small groups and learn together, utilizing effective time management methods.

    Our project offers:

    🤝 Joining study groups and finding like-minded individuals with similar interests and learning needs.
    🎥 Using webcam technology for visual communication with other group participants.
    ⏱ Learning through the Pomodoro technique, dividing time into work and rest periods for maximum productivity.
    📊 Keeping track of achievements and monitoring progress in learning.

    We believe that collaborative learning and the use of the Pomodoro technique will help each participant achieve their educational goals and enhance the effectiveness of their learning. Join StudySyncronize and start acquiring new knowledge together with us!
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Go back')
    markup.add(btn1)
    bot.send_message(message.chat.id, about_text, reply_markup=markup)




@bot.message_handler(func=lambda message: message.text == '🛠 FAQ')
def faq_english(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('What is the "Pomodoro" learning technique?', callback_data='q1_english')
    btn2 = types.InlineKeyboardButton('How will the learning process take place?', callback_data='q2_english')
    markup.add(btn1, btn2)
    btn_back = types.KeyboardButton('🔙 Go back')
    bot.send_message(message.chat.id, "📚 Frequently asked questions", reply_markup=markup)
    bot.send_message(message.chat.id, "Press the question to get the answer.",  reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back))

@bot.message_handler(func=lambda message: message.text == '📚 Registration')
def reg_english(message):
    reg_text = """
    Soon
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Go back')
    markup.add(btn1)
    bot.send_message(message.chat.id, reg_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📣 Call the administrator')
def call_english(message):
    call_text = """
    Soon
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Go back')
    markup.add(btn1)
    bot.send_message(message.chat.id, call_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔙 Повернутись до вибору мови')
def return_language_english(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇺🇦 Українська')
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇺🇦 Оберіть мову / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔙 Go back')
def return_to_menu_english(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('📰 About us')
    btn2 = types.KeyboardButton('🛠 FAQ')
    btn3 = types.KeyboardButton('📚 Registration')
    btn4 = types.KeyboardButton('📣 Call the administrator')
    btn5 = types.KeyboardButton('🔙 Повернутись до вибору мови')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, '👀 Choose a section', reply_markup=markup)


# FAQ_english
@bot.callback_query_handler(func=lambda call: call.data == 'q1_english')
def q1_english(call):
    faq_text = """
    
The Pomodoro Technique ⏳ is a time management method that helps improve productivity and focus by dividing time into periods of focused work and short breaks. 
he main idea is to work for a set period (usually 25 minutes) and then take a short break (usually 5 minutes). After several work and break cycles, a longer break is taken, for example, 15-30 minutes. 
This method helps maintain high levels of focus over extended periods and prevents fatigue and mental overload.
    """
    bot.send_message(call.message.chat.id, faq_text)

@bot.callback_query_handler(func=lambda call: call.data == 'q2_english')
def q2_english(call):
    faq_text = """
    🌐 Our online learning course will take place on Discord. 
    After registration, you'll have the option to join existing groups or create your own. 
    Once in a group, you'll be able to interact with fellow learners via webcam, fostering effective visual communication and helping you maintain discipline during study sessions. 
    Microphones will be automatically muted, and chat will be disabled to maximize your focus on learning.
    """
    bot.send_message(call.message.chat.id, faq_text)


bot.polling(none_stop=True, interval=0)