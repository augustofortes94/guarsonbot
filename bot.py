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
        updater.start_webhook(listen="0.0.0.0",
                      port=port,
                      url_path=os.getenv('TOKEN'),
                      webhook_url="https://{}.herokuapp.com/{}".format(heroku_app_name, os.getenv('TOKEN')))
        print("CORRIENDO PRODUCCION...")

else:
    defineLogs().info("ERROR: No se especifico el MODE")
    sys.exit

# Creo el bot con el token
if __name__ == "__main__":
    bot = telegram.Bot(token = os.getenv('TOKEN'))

# Enlazamos el updater con el bot
updater = Updater(bot.token, use_context= True)

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

dp.add_handler(CommandHandler("AUG", aug))

dp.add_handler(CommandHandler("AUGCW", augcw))

dp.add_handler(CommandHandler("AUGMW", augmw))

dp.add_handler(CommandHandler("Automata", automata))

dp.add_handler(CommandHandler("AX", ax50))

dp.add_handler(CommandHandler("AX50", ax50))

dp.add_handler(CommandHandler("Ballesta", ballesta))

dp.add_handler(CommandHandler("BAR", bar))

dp.add_handler(CommandHandler("Bizon", bizon))

dp.add_handler(CommandHandler("Blixen", blixen))

dp.add_handler(CommandHandler("Bren", bren))

dp.add_handler(CommandHandler("Bruen", bruen))

dp.add_handler(CommandHandler("Bullfrog", bullfrog))

dp.add_handler(CommandHandler("C58", c58))

dp.add_handler(CommandHandler("Carabina", cooper))

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

dp.add_handler(CommandHandler("FAL", fal))

dp.add_handler(CommandHandler("FAMAS", famas))

dp.add_handler(CommandHandler("FARA", fara))

dp.add_handler(CommandHandler("Fennec", fennec))

dp.add_handler(CommandHandler("FFAR", ffar))

dp.add_handler(CommandHandler("Finn", finn))

dp.add_handler(CommandHandler("FR556", fr556))

dp.add_handler(CommandHandler("G43", g43))

dp.add_handler(CommandHandler("Galil", cr56))

dp.add_handler(CommandHandler("Gallo", gallo))

dp.add_handler(CommandHandler("Garand", m1))

dp.add_handler(CommandHandler("Gracey", gracey))

dp.add_handler(CommandHandler("Grau", grau))

dp.add_handler(CommandHandler("Grav", grav))

dp.add_handler(CommandHandler("Groza", groza))

dp.add_handler(CommandHandler("H4", blixen))

dp.add_handler(CommandHandler("Hauer", hauer))

dp.add_handler(CommandHandler("HDR", hdr))

dp.add_handler(CommandHandler("Holger", holger))

dp.add_handler(CommandHandler("Ironhide", ironhide))

dp.add_handler(CommandHandler("ISO", iso))

dp.add_handler(CommandHandler("ITRA", itra))

dp.add_handler(CommandHandler("JAK", jak12))

dp.add_handler(CommandHandler("JAK12", jak12))

dp.add_handler(CommandHandler("Kar", kar98))

dp.add_handler(CommandHandler("Kar98", kar98))

dp.add_handler(CommandHandler("Kar98MW", kar98mw))

dp.add_handler(CommandHandler("Kar98VG", kar98vg))

dp.add_handler(CommandHandler("KGM40", kgm40))

dp.add_handler(CommandHandler("Kilo", kilo))

dp.add_handler(CommandHandler("Krig", krig))

dp.add_handler(CommandHandler("Klauser", klauser))

dp.add_handler(CommandHandler("KSP", ksp))

dp.add_handler(CommandHandler("LAPA", lapa))

dp.add_handler(CommandHandler("LC10", lc10))

dp.add_handler(CommandHandler("M1", m1))

dp.add_handler(CommandHandler("M13", m13))

dp.add_handler(CommandHandler("M16", m16))

dp.add_handler(CommandHandler("M19", m19))

dp.add_handler(CommandHandler("M1912", m1912))

dp.add_handler(CommandHandler("M1916", m1916))

dp.add_handler(CommandHandler("M4", m4))

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

dp.add_handler(CommandHandler("MP5", mp5))

dp.add_handler(CommandHandler("MP5CW", mp5cw))

dp.add_handler(CommandHandler("MP5MW", mp5mw))

dp.add_handler(CommandHandler("MP7", mp7))

dp.add_handler(CommandHandler("Nikita", nikita))

dp.add_handler(CommandHandler("NZ", nz41))

dp.add_handler(CommandHandler("NZ41", nz41))

dp.add_handler(CommandHandler("Oden", oden))

dp.add_handler(CommandHandler("Origin", origin))

dp.add_handler(CommandHandler("OTS", ots9))

dp.add_handler(CommandHandler("OTS9", ots9))

dp.add_handler(CommandHandler("Owen", owen))

dp.add_handler(CommandHandler("1911", p1911))

dp.add_handler(CommandHandler("1911CW", p1911cw))

dp.add_handler(CommandHandler("1911MW", p1911mw))

dp.add_handler(CommandHandler("1911VG", p1911vg))

dp.add_handler(CommandHandler("P357", p357))

dp.add_handler(CommandHandler("50GS", p50gs))

dp.add_handler(CommandHandler("P90", p90))

dp.add_handler(CommandHandler("Pelington", pelington))

dp.add_handler(CommandHandler("PKM", pkm))

dp.add_handler(CommandHandler("PPSH", ppsh))

dp.add_handler(CommandHandler("PPSHCW", ppshcw))

dp.add_handler(CommandHandler("PPSHVG", ppshvg))

dp.add_handler(CommandHandler("QBZ", qbz))

dp.add_handler(CommandHandler("R1", r1shadowhunter))

dp.add_handler(CommandHandler("R9", r9))

dp.add_handler(CommandHandler("RAAL", raal))

dp.add_handler(CommandHandler("RAM", ram))

dp.add_handler(CommandHandler("RATT", ratt))

dp.add_handler(CommandHandler("Renetti", renetti))

dp.add_handler(CommandHandler("RPD", rpd))

dp.add_handler(CommandHandler("Rytec", rytec))

dp.add_handler(CommandHandler("SA87", sa87))

dp.add_handler(CommandHandler("SCAR", scar))

dp.add_handler(CommandHandler("SKS", sks))

dp.add_handler(CommandHandler("SPR", spr))

dp.add_handler(CommandHandler("Sten", sten))

dp.add_handler(CommandHandler("STG", stg))

dp.add_handler(CommandHandler("Stoner", stoner))

dp.add_handler(CommandHandler("Street", streetsweeper))

dp.add_handler(CommandHandler("Striker", striker))

dp.add_handler(CommandHandler("SVT", svt))

dp.add_handler(CommandHandler("Swiss", swiss))

dp.add_handler(CommandHandler("Sykov", sykov))

dp.add_handler(CommandHandler("TEC", tec9))

dp.add_handler(CommandHandler("TEC9", tec9))

dp.add_handler(CommandHandler("Topbreak", topbreak))

dp.add_handler(CommandHandler("Treslineas", treslineas))

dp.add_handler(CommandHandler("Tundra", tundra))

dp.add_handler(CommandHandler("Type", type))

dp.add_handler(CommandHandler("Type100", type100))

dp.add_handler(CommandHandler("Type11", type11))

dp.add_handler(CommandHandler("Type63", type63))

dp.add_handler(CommandHandler("Type99", type99))

dp.add_handler(CommandHandler("UGM", ugm8))

dp.add_handler(CommandHandler("UGM8", ugm8))

dp.add_handler(CommandHandler("UGR", ugr))

dp.add_handler(CommandHandler("UZI", uzi))

dp.add_handler(CommandHandler("Vargo", vargo))

dp.add_handler(CommandHandler("VLK", vlk))

dp.add_handler(CommandHandler("VOLKS", volks))

dp.add_handler(CommandHandler("Welgun", welgun))

dp.add_handler(CommandHandler("Whitley", whitley))

dp.add_handler(CommandHandler("X16", x16))

dp.add_handler(CommandHandler("XM4", xm4))

dp.add_handler(CommandHandler("ZRG", zrg))


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


# MANEJADOR DE MENSAJES SIN "/"
dp.add_handler(MessageHandler(Filters.text, messageHandler))

# RUN
run(updater)
