from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "токен удалён в целях безопасности"

# Функция, которая вызывается, когда пользователь вводит команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # создаем список с одной кнопкой 1_1
    keyboard = [
        [InlineKeyboardButton("Нажми меня!", callback_data='button_pressed')]
    ]
    # оборачиваем кнопку в InlineKeyboardMarkup для отображения пользователю
    reply_markup = InlineKeyboardMarkup(keyboard)
    # отправляем сообщение с кнопкой 1_1 пользователю
    await update.message.reply_text('Привет! Это мой первый бот с кнопками.', reply_markup=reply_markup)

# функция, которая вызывается, когда пользователь нажимает на кнопку 1_1
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # получаем инфу о нажатии на кнопку 1_1
    query = update.callback_query
    # штука для тг, чтобы не было ошибок
    await query.answer()

    # создаем новый список кнопок
    new_keyboard = [
        [InlineKeyboardButton("Новая кнопка 1", callback_data='new_button_1')],
        [InlineKeyboardButton("Новая кнопка 2", callback_data='new_button_2')]
    ]
    # оборачиваем новый список в InlineKeyboardMarkup
    reply_markup = InlineKeyboardMarkup(new_keyboard)
    # заменяем сообщение на новое с другим списком кнопок
    await query.edit_message_text(text="Выберите новую кнопку:", reply_markup=reply_markup)

# функция для обработки нажатия на кнопку 2_1
async def new_button_1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вы нажали на Новую кнопку 1!")

# функция для обработки нажатия на кнопку 2_2
async def new_button_2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вы нажали на Новую кнопку 2!")

def main() -> None:
    # инициализация бота
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    # Регистрируем обработчик нажатия на кнопку 1_1
    application.add_handler(CallbackQueryHandler(button_handler, pattern='button_pressed'))
    # Регистрируем обработчик нажатия на кнопку 2_1
    application.add_handler(CallbackQueryHandler(new_button_1_handler, pattern='new_button_1'))
    # Регистрируем обработчик нажатия на кнопку 2_2
    application.add_handler(CallbackQueryHandler(new_button_2_handler, pattern='new_button_2'))

    # Запускаем бота и начинаем polling (циклично докапываться до тг, есть ли новые сообщения?)
    application.run_polling()

if __name__ == '__main__':
    main()