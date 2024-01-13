from config import * # importar token
import telebot  # para manejar la API de Telegram

# instanciamos el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# responder al comando /start
@bot.message_handler(commands=["start"])
def cmd_start(message):
    """Dar la bienvenida"""
    bot.reply_to(message, "Hola, Bienvenido al Bot de Seguridad y Defensa.")

# responde a los mensaje de texto que no son comandos 
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    pagina_web = '<a href="https://jhoandavid28.github.io/Seguridad-y-Defensa-Datos-Abiertos-Ecuador/">ENLACE</a> '
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        bot.send_message(message.chat.id, pagina_web, parse_mode="html")

# main
if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
