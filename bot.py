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
from resources.commands.weapons import *


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

telegram_token = os.getenv('TELEGRAM_TOKEN')

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
        host_url = os.environ.get("HOST_URL")
        updater.start_webhook(listen="0.0.0.0", port=port, url_path=telegram_token, webhook_url= host_url + telegram_token)
        print("CORRIENDO PRODUCCION...")

else:
    defineLogs().info("ERROR: No se especifico el MODE")
    sys.exit

# Creo el bot con el token
if __name__ == "__main__":
    bot = telegram.Bot(token=telegram_token)

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

dp.add_handler(CommandHandler("M1", m1garand))

dp.add_handler(CommandHandler("Kar", kar98))

dp.add_handler(CommandHandler("Kar98", kar98))

dp.add_handler(CommandHandler("M4", m4))

dp.add_handler(CommandHandler("MP5", mp5))

dp.add_handler(CommandHandler("1911", p1911))

dp.add_handler(CommandHandler("PPSH", ppsh))

dp.add_handler(CommandHandler("Type", type))

dp.add_handler(CommandHandler("Vargo", vargo))

# BONUS
dp.add_handler(CommandHandler("BotConchadetumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotConchatumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotLaConchadetumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotLaConchatumadre", botconchatumadre))

dp.add_handler(CommandHandler("BotRapido", botrapido))

dp.add_handler(CommandHandler("Cod", codsignal))

dp.add_handler(CommandHandler("Dolar", dolar))

dp.add_handler(CommandHandler("Fortnite", fortnite))

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
#dp.add_handler(MessageHandler(Filters.regex(r"^/\w+$"), commandRegex))


# MANEJADOR DE MENSAJES SIN "/"
# dp.add_handler(MessageHandler(Filters.text, messageHandler))


# HARDCODE WEAPONS

dp.add_handler(CommandHandler("AK47CW", ak47cw))

dp.add_handler(CommandHandler("AK47MW", ak47mw))

dp.add_handler(CommandHandler("AK74U", ak74u))

dp.add_handler(CommandHandler("Ametralladora", ametralladora))

dp.add_handler(CommandHandler("AMP", amp))

dp.add_handler(CommandHandler("AN94", an94))

dp.add_handler(CommandHandler("Antitanque", antitanque))

dp.add_handler(CommandHandler("Armaguerra", armaguerra))

dp.add_handler(CommandHandler("AS44", as44))

dp.add_handler(CommandHandler("ASVAL", asval))

dp.add_handler(CommandHandler("AUGCW", augcw))

dp.add_handler(CommandHandler("AUGMW", augmw))

dp.add_handler(CommandHandler("Automata", automata))

dp.add_handler(CommandHandler("AX50", ax50))

dp.add_handler(CommandHandler("Ballesta", ballesta))

dp.add_handler(CommandHandler("BAR", bar))

dp.add_handler(CommandHandler("Bizon", bizon))

dp.add_handler(CommandHandler("Blixen", blixen))

dp.add_handler(CommandHandler("BP50", bp50))

dp.add_handler(CommandHandler("Bren", bren))

dp.add_handler(CommandHandler("Bruen", bruen))

dp.add_handler(CommandHandler("Bullfrog", bullfrog))

dp.add_handler(CommandHandler("C58", c58))

dp.add_handler(CommandHandler("Carv2", carv2))

dp.add_handler(CommandHandler("Combate", combate))

dp.add_handler(CommandHandler("Cooper", cooper))

dp.add_handler(CommandHandler("CR56", cr56))

dp.add_handler(CommandHandler("CX9", cx9))

dp.add_handler(CommandHandler("Diamatti", diamatti))

dp.add_handler(CommandHandler("DMR", dmr))

dp.add_handler(CommandHandler("Doble", doble))

dp.add_handler(CommandHandler("DP27", dp27))

dp.add_handler(CommandHandler("Dragunov", dragunov))

dp.add_handler(CommandHandler("E725", e725))

dp.add_handler(CommandHandler("EBR14", ebr14))

dp.add_handler(CommandHandler("Einhorn", einhorn))

dp.add_handler(CommandHandler("EM2", em2))

dp.add_handler(CommandHandler("EX1", ex1))

dp.add_handler(CommandHandler("FAL", fal))

dp.add_handler(CommandHandler("FARA", fara))

dp.add_handler(CommandHandler("Fennec", fennec))

dp.add_handler(CommandHandler("FFAR", ffar))

dp.add_handler(CommandHandler("FFAR1", ffar))

dp.add_handler(CommandHandler("FINN", finn))

dp.add_handler(CommandHandler("FR556", fr556))

dp.add_handler(CommandHandler("G43", g43))

dp.add_handler(CommandHandler("Gallo", gallo))

dp.add_handler(CommandHandler("Gracey", gracey))

dp.add_handler(CommandHandler("Grau", grau))

dp.add_handler(CommandHandler("Grav", grav))

dp.add_handler(CommandHandler("Groza", groza))

dp.add_handler(CommandHandler("Hauer", hauer))

dp.add_handler(CommandHandler("HDR", hdr))

dp.add_handler(CommandHandler("Holger", holger))

dp.add_handler(CommandHandler("Ironhide", ironhide))

dp.add_handler(CommandHandler("ISO", iso))

dp.add_handler(CommandHandler("ITRA", itra))

dp.add_handler(CommandHandler("JAK12", jak12))

dp.add_handler(CommandHandler("Kar98MW", kar98mw))

dp.add_handler(CommandHandler("Kar98VG", kar98vg))

dp.add_handler(CommandHandler("KGM40", kgm40))

dp.add_handler(CommandHandler("Kilo", kilo))

dp.add_handler(CommandHandler("Klauser", klauser))

dp.add_handler(CommandHandler("Krig", krig))

dp.add_handler(CommandHandler("KSP", ksp))

dp.add_handler(CommandHandler("LAPA", lapa))

dp.add_handler(CommandHandler("LC10", lc10))

dp.add_handler(CommandHandler("Lienna", lienna))

dp.add_handler(CommandHandler("M13", m13))

dp.add_handler(CommandHandler("M16", m16))

dp.add_handler(CommandHandler("M19", m19))

dp.add_handler(CommandHandler("M1912", m1912))

dp.add_handler(CommandHandler("M1916", m1916))

dp.add_handler(CommandHandler("M1Garand", m1garand))

dp.add_handler(CommandHandler("M4A1", m4a1))

dp.add_handler(CommandHandler("M60", m60))

dp.add_handler(CommandHandler("M82", m82))

dp.add_handler(CommandHandler("M91", m91))

dp.add_handler(CommandHandler("MAC", mac))

dp.add_handler(CommandHandler("Magnum", magnum))

dp.add_handler(CommandHandler("Marco", marco))

dp.add_handler(CommandHandler("Marshal", marshal))

dp.add_handler(CommandHandler("MG34", mg34))

dp.add_handler(CommandHandler("MG42", mg42))

dp.add_handler(CommandHandler("MG82", mg82))

dp.add_handler(CommandHandler("Milano", milano))

dp.add_handler(CommandHandler("MK2", mk2))

dp.add_handler(CommandHandler("Modelo", modelo))

dp.add_handler(CommandHandler("MP40", mp40))

dp.add_handler(CommandHandler("MP5CW", mp5cw))

dp.add_handler(CommandHandler("MP5MW", mp5mw))

dp.add_handler(CommandHandler("MP7", mp7))

dp.add_handler(CommandHandler("Nikita", nikita))


dp.add_handler(CommandHandler("1911CW", p1911cw))

dp.add_handler(CommandHandler("1911MW", p1911mw))

dp.add_handler(CommandHandler("1911VG", p1911vg))

dp.add_handler(CommandHandler("50GS", p50gs))

# RUN
run(updater)
