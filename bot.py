import os
import sys
import telegram
from dotenv import load_dotenv
from pathlib import Path
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from resources.commands.commandsMenu import *
from resources.commands.bonus import *
from resources.commands.botonera import *
from resources.commands.lobbys import *
from resources.commands.stats import *
from resources.commands.streamers import *
from resources.commands.weapons import *


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

if os.getenv('MODE') == "dev":
    # Acceso local
    def run(updater):
        updater.start_polling()
        print("CORRIENDO DESARROLLO...")
        updater.idle()  # permite finalizar el bot con ctrl+C

elif os.getenv('MODE') == "prod":
    # Acceso HEROKU (produccion)
    def run(updater):
        port = int(os.environ.get('PORT', '8443'))
        heroku_app_name = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0", port=port, url_path=os.getenv('TOKEN'), webhook_url="https://{}.herokuapp.com/{}".format(heroku_app_name, os.getenv('TOKEN')))
        print("CORRIENDO PRODUCCION...")

else:
    defineLogs().info("ERROR: No se especifico el MODE")
    sys.exit

# Creo el bot con el token
if __name__ == "__main__":
    bot = telegram.Bot(token=os.getenv('TOKEN'))

# Enlazamos el updater con el bot
updater = Updater(bot.token, use_context=True)

# Creamos un depachador
dp = updater.dispatcher

# LLAMADOS A COMANDOS #

# COMANDOS
dp.add_handler(CommandHandler("Armas", armas))

dp.add_handler(CommandHandler("Comandos", comandos))

dp.add_handler(CommandHandler("Hola", hola))

dp.add_handler(CommandHandler("Lobbys", lobbys))

dp.add_handler(CommandHandler("Stats", stats))

dp.add_handler(CommandHandler("Streamers", streamers))


# ARMAS
dp.add_handler(CommandHandler("AK47", ak47))

dp.add_handler(CommandHandler("AUG", aug))

dp.add_handler(CommandHandler("M1", m1))

dp.add_handler(CommandHandler("Kar", kar98))

dp.add_handler(CommandHandler("Kar98", kar98))

dp.add_handler(CommandHandler("M4", m4))

dp.add_handler(CommandHandler("MP5", mp5))

dp.add_handler(CommandHandler("1911", p1911))

dp.add_handler(CommandHandler("PPSH", ppsh))

dp.add_handler(CommandHandler("Type", type))

dp.add_handler(CommandHandler("Vargo", vargo))

# STREAMERS
dp.add_handler(CommandHandler("Aydan", aydan))

dp.add_handler(CommandHandler("LobbyAmir", lobbyAmir))

dp.add_handler(CommandHandler("LobbyAydan", lobbyAydan))

dp.add_handler(CommandHandler("LobbyFlexz", lobbyFlexz))

dp.add_handler(CommandHandler("LobbyIron", lobbyIron))

dp.add_handler(CommandHandler("LobbyMirrey", lobbyMirrey))

dp.add_handler(CommandHandler("LobbySoki", lobbySoki))

dp.add_handler(CommandHandler("LobbyTaison", lobbyTaison))

dp.add_handler(CommandHandler("Mutex", mutex))


# BONUS
dp.add_handler(CommandHandler("Alla", alla))

dp.add_handler(CommandHandler("Api", api))

dp.add_handler(CommandHandler("BotConchadetumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotConchatumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotLaConchadetumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotLaConchatumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotRapido", botrapido))

dp.add_handler(CommandHandler("Cod", codsignal))

dp.add_handler(CommandHandler("Fortnite", fortnite))

dp.add_handler(CommandHandler("Guarson", guarson))

dp.add_handler(CommandHandler("Manco", manco))

dp.add_handler(CommandHandler("Mancolorian", mancolorian))

dp.add_handler(CommandHandler("Matchmaking", matchmaking))

dp.add_handler(CommandHandler("Quaqua", quaqua))

dp.add_handler(CommandHandler("Tabla", tableColour))


# COD-API
dp.add_handler(CommandHandler("Bolsonaro", bolsonaro))

dp.add_handler(CommandHandler("BolsonaroKD", bolsonarokd))

dp.add_handler(CommandHandler("Conectados", conectados))

dp.add_handler(CommandHandler("Berisso1", elch000))

dp.add_handler(CommandHandler("Berisso1KD", elch000kd))

dp.add_handler(CommandHandler("Hormigator", hormigator))

dp.add_handler(CommandHandler("HormigatorKD", hormigatorkd))

dp.add_handler(CommandHandler("Leko", leko))

dp.add_handler(CommandHandler("LekoKD", lekokd))

dp.add_handler(CommandHandler("LobbyBerisso1", lobbyElch000))

dp.add_handler(CommandHandler("LobbyBolsonaro", lobbyBolsonaro))

dp.add_handler(CommandHandler("LobbyHormigator", lobbyHormigator))

dp.add_handler(CommandHandler("LobbyLeko", lobbyLeko))

dp.add_handler(CommandHandler("LobbyLuquitas", lobbyLuquitas))

dp.add_handler(CommandHandler("LobbyMandalorian", lobbyMandalorian))

dp.add_handler(CommandHandler("LobbyPablo", lobbyPablo))

dp.add_handler(CommandHandler("LobbyRapax", lobbyRapax))

dp.add_handler(CommandHandler("Luquitas", luquitas))

dp.add_handler(CommandHandler("LuquitasKD", luquitaskd))

dp.add_handler(CommandHandler("Mandalorian", mandalorian))

dp.add_handler(CommandHandler("MandalorianKD", mandaloriankd))

dp.add_handler(CommandHandler("Pablo", pablo))

dp.add_handler(CommandHandler("PabloKD", pablokd))

dp.add_handler(CommandHandler("Rapax", rapax))

dp.add_handler(CommandHandler("RapaxKD", rapaxkd))


# BOTONERA
# dp.add_handler(CommandHandler("bot", botoneraAdapter))


# CERTIFICADO
dp.add_handler(CommandHandler("Certificado", certified))


# COMANDOS DINAMICOS
dp.add_handler(MessageHandler(Filters.regex(r"^/\w+$"), weaponRegex))


# MANEJADOR DE MENSAJES SIN "/"
# dp.add_handler(MessageHandler(Filters.text, messageHandler))


# RUN
run(updater)
