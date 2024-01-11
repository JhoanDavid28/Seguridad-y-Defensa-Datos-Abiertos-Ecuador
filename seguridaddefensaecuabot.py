from config import * # importar token
import telebot  # para manejar la API de Telegram

# instanciamos el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)

# responder al comando /start
@bot.message_handler(commands=["start"])

def cmd_start(message):
    """Dar la bienvenida"""
    bot.reply_to(message, "Hola, Bienvenido al Bot de Seguridad y Defensa.")


# main
if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')