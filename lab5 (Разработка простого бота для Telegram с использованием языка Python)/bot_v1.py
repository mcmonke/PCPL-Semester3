from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "токен удалён в целях безопасности"

# Функция, которая вызывается, когда пользователь вводит команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # создаем список с одной кнопкой
    keyboard = [
        [InlineKeyboardButton("Нажми меня!", callback_data='button_pressed')]
    ]
    # оборачиваем кнопку в InlineKeyboardMarkup для отображения пользователю
    reply_markup = InlineKeyboardMarkup(keyboard)
    # отправляем сообщение с кнопкой пользователю
    await update.message.reply_text('Привет! Это мой первый бот с кнопками.', reply_markup=reply_markup)

# функция, которая вызывается, когда пользователь нажимает на кнопку
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # получаем инфу о нажатии на кнопку
    query = update.callback_query
    # штука для тг, чтобы не было ошибок
    await query.answer()
    # меняем прошлое сообщение на нужный текст при нажатии на кнопку
    await query.edit_message_text(text="Вы нажали на кнопку!")


def main() -> None:
    # инициализация бота
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    # Регистрируем обработчик нажатия на кнопку
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запускаем бота и начинаем polling (циклично докапываться до тг, есть ли новые сообщения?)
    application.run_polling()


if __name__ == '__main__':
    main()