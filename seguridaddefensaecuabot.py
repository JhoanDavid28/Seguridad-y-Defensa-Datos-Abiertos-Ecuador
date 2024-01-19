from config import * # importar token
import telebot  # para manejar la API de Telegram
from cargar_datos import *
import matplotlib.pyplot as plt
import seaborn as sns
import threading # para hacer hilos que se ejecutan
from telebot.types import ForceReply

# instanciamos el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])
def cmd_start(message):  
    bot.reply_to(message, "Hola, Bienvenido al Bot de Seguridad y Defensa sobre datos de Ecuador, tenemos datos desde Enero a noviembre de 2023.")
    bot.reply_to(message, "Aquí tienes información sobre: \n/detenidos_aprehendidos \n/armas_ilicitas \n/personas_desaparecidas")
   
# responde al comando /detenidos_aprehendidos
@bot.message_handler(commands=["detenidos_aprehendidos"])
def cmd_detenidos_aprendidos(message):
    # = "Puedes ingresar diferentes comandos para conocer datos de las personas detenidas segun: \nubicación "
    # Pregunta sobre la información a consultar
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Ingresa el comando", reply_markup=markup) 
    bot.register_next_step_handler(msg, handle_detenidos_aprehendidos)

def handle_detenidos_aprehendidos(message):
    if message.text == "ubicacion":
        handle_ubicacion(message)     
    else: 
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "ERROR: Ingresa otro comando", reply_markup=markup) 
        bot.register_next_step_handler(msg, handle_detenidos_aprehendidos) 
        

def handle_ubicacion(message):
    # Lógica para /ubicacion dentro de /detenidos_aprehendidos
    bot.send_message(message.chat.id, "Aquí puedes obtener información sobre la ubicación de personas detenidas.")
    # Lógica para /ubicacion dentro de /detenidos_aprehendidos
    bot.send_message(message.chat.id, "Generando gráfico de ubicación...")

    # Crear el gráfico de ubicación usando Seaborn
    # Crear un histograma de provincias
    plt.figure(figsize=(20, 5))
    sns.histplot(df_detenidos_aprehendidos['nombre_provincia'],   orientation='vertical', color='skyblue')
    plt.title('Distribución de Provincias de Personas Detenidas/Aprehendidas')
    plt.xlabel('Provincia')
    plt.ylabel('Frecuencia')
    
    # Guardar el gráfico como una imagen
    plt.savefig('ubicacion_detenidos_aprehendidos.png')
    plt.close()
    # Enviar la imagen al usuario
    with open('ubicacion_detenidos_aprehendidos.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption='Gráfico de Ubicación de Personas Detenidas/Aprehendidas')





# responde al comando /armas_ilicitas
@bot.message_handler(commands=["armas_ilicitas"])
def cmd_armas_ilicitas(message):
    pass
# responde al comando /personas_desaparecidas
@bot.message_handler(commands=["personas_desaparecidas"])
def cmd_personas_desaparecidas(mensaje):
    pass



# responde a los mensaje de texto 
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    texto_informacion = '<b>Para más información visita el siguiente enlace</b>\n'
    texto_informacion += '<a href="https://jhoandavid28.github.io/Seguridad-y-Defensa-Datos-Abiertos-Ecuador/">ENLACE</a>'
    command = message.text.split()[0].lower()
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        bot.send_message(message.chat.id, texto_informacion, parse_mode="html")



# recibe los mensajes desde telegram
def recibir_mensajes():
    bot.infinity_polling()


# main
if __name__ == '__main__':
    # conficuracion de comandos disponibles
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Da la bienvenida"),
        telebot.types.BotCommand("/detenidos_aprehendidos", "Muestra información de personas detenidas o aprehendidas"),
        telebot.types.BotCommand("/armas_ilicidas", "Muestra información de armas ilicitas"),
        telebot.types.BotCommand("/personas_desaparecidas", "Muestra información de personas desaparecidas"), 
    ])
        
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot iniciado')
