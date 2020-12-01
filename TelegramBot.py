import string
import random
import re
import requests
import lxml.html as lh
import telegram
from lxml.html import document_fromstring
from lxml.html.clean import clean_html
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

def quitar_acento(mensaje):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    )
    for a, b in replacements:
        mensaje = mensaje.replace(a, b).replace(a.upper(), b.upper())
    return mensaje

def start(update, context):
    update.message.reply_text(f"Mi lord {update.message.from_user.first_name}, \n\nEspero que tenga un buen día, soy su nuevo mayordomo virtual, \n\n¿Cómo puedo ayudarte?")
def info(update, context):
    update.message.reply_text(f"Mi lord {update.message.from_user.first_name}, proximamente tendré más funciones por ahora solo puedo usar /start, perdoneme!")
    
def palabrota(update, context):
    mensaje=update.message.text
    patron=re.compile("hijueputa|bot hp|gonorrea|hp|tonto|bobo|lame vergas|chupa penes|bot de mierda|mierda|bot mierda|puto", re.I)
    patron.search(mensaje)
    patron.match(mensaje)
    coincide=patron.search(mensaje)
    patron=re.compile("perro", re.I)
    patron.search(mensaje)
    patron.match(mensaje)
    perro=patron.search(mensaje)
    patron=re.compile("gato", re.I)
    patron.search(mensaje)
    patron.match(mensaje)
    gato=patron.search(mensaje)
    patron=re.compile("bye|adios|nos vemos|hasta mañana|ciao|chao|nos pi|bye bot|chao bot|chaolin|bot putito|putito", re.I)
    patron.search(mensaje)
    patron.match(mensaje)
    despedida=patron.search(mensaje)
    if coincide:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tratame serio {update.message.from_user.first_name}, malparido... Con todo respeto mi lord.")
        context.bot.reply_text(chat_id=update.effective_chat.id, text="70HP")
    if (mensaje=="ponte verga" or mensaje=="no mames ponte verga" or mensaje=="no mames, ponte verga"  or mensaje=="no mames, ponte verga @rivera_rol_bot"):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"No le entiendo un culo hable en colombiano {update.message.from_user.first_name}")
    if perro:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Guau! Guau!")
    if gato:
        context.bot.send_message(chat_id=update.effective_chat.id, text="La curiosidad lo mató.")
    if despedida:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao amigo!")
    mensaje= mensaje.upper()
    mensaje= quitar_acento(mensaje)
    if (mensaje=="BUEN DIA" or mensaje=="BUENOS DIAS" or mensaje=="BNOS DIAS" or mensaje=="HOLA" or mensaje=="BUENOS DIAS ESTRELLITAS" or mensaje=="BUENOS DIAS TROPA"):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Buen día mi lord {update.message.from_user.first_name}")
    if (mensaje=="BUENOS DÍAS PERRAS" or mensaje=="BUENOS DIAS PERRAS" ):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Buen día {update.message.from_user.first_name} perra canequera!")
        
def frase_aleatoria(update, context):
    frases=["Más fastidioso que una pulga entre la nalga","A mí me gustan las cuentas claras y el chocolate espeso","Uno no es monedita de oro para caerle bien a todo el mundo","Píntemela a ver y yo le digo cuántos pares son tres moscas","Ni que estuviéramos bravos","¿Durmió conmigo anoche o qué, que no saluda?","Esos dos son uña y mugre","Me la puso de pa´rriba","Que se va de playa, ¿no?","Sóbese que no hay pomada","Tengo un filo, que si me agacho me corto","Está que se las pela","¿Qué desea de principio? ¿Garbanzo u arveja?","¡Quite de hay!","Bueno se me van bajando del bus aquí todos","¿Y eso quién pidió pollo?","¿Qué hay pa´hacer? Pues, empanadas que es lo que más se vende.","¡Ay, no se me coloque así!","¡Nanay cucas!","Esto está más largo que una semana sin carne","Váyase por la sombrita","¡Lo visto pero no lo mantengo!","¡Pero, comete alguito!","¡Se ve que se toma la sopita!","¿Cómo está? Regular, tres cuartos...","Nos tocó raspar fiesta como hasta las 5 de la mañana","Pilas... vengo pidiendo vía como Toyota nuevo en carretera destapada","Me sale lo comido por lo servido","¡Oiga, champion!","Ese man baila como un trompo","Lo que le diga es mentira","¡Sale pa´pintura!","¡Tan chistoso! ¿Fue que tomó caldo de payasito?","¡Te vi!","¡Uuuuyyyyyyyy, se nos creció el enano!","¡Déle chancleta!","¡Hmmm, ese huevito quiere sal!","Eso era puro ría que ría","No me abra los ojos que no le voy a echar gotas","No me levante las cejas que no voy a pasar por debajo.","¡Dichosos los ojos!","!Pero, me extraña!","¡Milagrazo, chinazo!","¿Qué se dice, gente?","¡Chaos!","¡Quiubos!","Me hace el favor y le baja al tonito","Aquí en la lucha, moliendo duro","¡Hay que estar mosca, papá!","Pa'qué, pero ese man tiene madera","Esa hembra está mas arreglada que muchacha de servicio en domingo","Yo lo tengo entre ojos","¿Usted qué come, que adivina?","¡Usted si mata un marrano a cantaleta! ¿No?","Mugre que no mata, engorda","Lleguémosle a eso, hermanito","¡Ese man es mas picado que muela de gamin!","¡Oiga, sardino! ¿Qué se dice?","¡Ese man sí tiene swing)!","¡Tengo un filin!","¡Joven aún!","El que tiene tienda, que la atienda","Aquí no se trabaja pero se goza...","Usted está miando fuera del tiesto","¡Hum, ya dijo!","No me alegro, pero sí me da un fresquito...","¡Ese man está que hecha chispas!","Es que yo no le he contado: a mí me embiste la tecnología","Tengo una miada que me sabe la boca a champaña","Esa vieja es más fea que un carro por debajo","Tiene más patas que un chance","¡Pa'las que sean, papá!","A esta vaina no le cabe un tinto","¡Póngase chanclas!","¡Tocó almorzar corrientazo!","A ese man lo dejaron mirando pa'entro o le pusieron la pijama de madera o lo pusieron a chupar gladiolo!","Esa vieja sí que es guapachosa","El viejito esta capando cementerio","¿Cómo se llama tu nombre? ¿Dónde vive tu dirección?","Señor taxista, lléveme al centro, pero pilas con el muñeco en el taximetro","Páreme bolas para que me entienda!!!","Sumercé, ¿se le ofrece algo?","Hágase el marica y así se queda","Tome pa'la gaseosa","Mono, ¿le limpio el vidrio?","Chilla más que un camionado de pollos","La cucha y el catano","Juega más que gato chiquito","Tome cervecita pa'que tenga qué orinar","Un buen colombiano no orina solo","Vecina, ¿me da ñapa?","Juemadre, juemichica, jueldiablo y todos los juez que usted ha escuchado","Mujer que no joda es hombre o tiene mozo","Jincho pero contento","Me eché un motoso","Le rompieron la cara y parte del rostro","Se rumbiaron a la hija de ese man","Le llenaron la barriga de huesitos por andar de patisuelta","Indio patirrajao","Déle forguar a este imeil pa que lo leigan en el ciberespacio","¡Uich, qué boleta","O todos en la cama o todos en el piso","Yerba mala nunca muere","El diablo es puerco","Salte aquí y reclame dos moscas","Pille la nota","Le fue más mal que a perro en misa.","Vale un ojo de la cara","Si como no moñito","Contame una de vaqueros","Yo rajo pero no sostengo","En que familia van?","Haga lo que se le de la Gana"]
    indice=random.randint(0,len(frases))
    update.message.reply_text(frases[indice])


updater = Updater("<TOKEN AQUÍ>", use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("info", info))
updater.dispatcher.add_handler(CommandHandler("frase", frase_aleatoria))
updater.dispatcher.add_handler(MessageHandler(Filters.text ,palabrota))
updater.start_polling()
updater.idle()
