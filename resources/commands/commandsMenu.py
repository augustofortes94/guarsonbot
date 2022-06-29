import logging
import datetime
from telegram import *
from resources.api.codapi import *

#Defino la info para los logs
def defineLogs():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
        )
    logger = logging.getLogger()
    return logger

logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
        )
logger = logging.getLogger()

#####   COMANDOS    #####
def armas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Armas")
    update.message.reply_text("/Comandos para armas:\n\n" + getListArmas())

def comandos(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos")
    update.message.reply_text(
        "/Hola soy el /bot Guarson, hasta ahora los /Comandos disponibles son los siguientes:\n\n"
        + "\n-----/Armas-----\n"
        + getListArmas()
        + "\n\n-----/Streamers-----"
        + getListStreamers()
        + getListBonus()
        + "\n\n-----/Stats-----"
        + getListStats()
        + "\n\n-----/Lobbys-----"
        + getListLobbys()
        )

def hola(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hola")
    name = update.effective_user['username']
    update.message.reply_text(f"Hola {name}, soy guarson, un bot creado para LMD2 con la intencion de dejar guardado todas las configuraciones de armas de Warzone, como asi tambien ofrecer estadisticas de las lobbies de los miembros del clan.")

def lobbys(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Lobbys")
    update.message.reply_text("/Comandos para Lobbys:\n\n" + getListLobbys())

def stats(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Estadisticas")
    update.message.reply_text("/Comandos para estadisticas:\n\n" + getListStats() + getListLobbys())

def streamers(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Streamers")
    update.message.reply_text("/Comandos para streamers:\n\n" + getListStreamers())

#####   CERTIFICADO   #####
def certified(update, context):     #Devuelvo el vencimiento del certificado SSO
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Certificado")
    expire_date = int(os.getenv('sso_expire'))
    update.message.reply_text("Vence el: " + str(datetime.datetime.fromtimestamp(expire_date/1000)))

#####   PRINTS  #####
def getListArmas():     #Return a string with a list of weapons
    return ("\nFusiles de Asalto:"
        + "\n-/AK47MW"
        + "\n-/AK47CW"
        + "\n-/AN94"
        + "\n-/AS44"
        + "\n-/ASVAL"
        + "\n-/Automata"
        + "\n-/BAR"
        + "\n-/C58"
        + "\n-/Cooper"
        + "\n-/CR56"
        + "\n-/EM2"
        + "\n-/FAL"
        + "\n-/FARA"
        + "\n-/FFAR"
        + "\n-/FR556"
        + "\n-/Grau"
        + "\n-/Grav"
        + "\n-/Groza"
        + "\n-/ITRA"
        + "\n-/KGM40"
        + "\n-/Kilo"
        + "\n-/Krig"
        + "\n-/M13"
        + "\n-/M4A1"
        + "\n-/Nikita"
        + "\n-/NZ41"
        + "\n-/Oden"
        + "\n-/QBZ"
        + "\n-/RAM"
        + "\n-/SCAR"
        + "\n-/STG"
        + "\n-/Vargo"
        + "\n-/Volks"
        + "\n-/XM4"
        + "\n\nSubfusiles:"
        + "\n-/AK74U"
        + "\n-/Armaguerra"
        + "\n-/AUGMW"
        + "\n-/Bizon"
        + "\n-/Blixen"
        + "\n-/Bullfrog"
        + "\n-/CX9"
        + "\n-/Fennec"
        + "\n-/ISO"
        + "\n-/KSP"
        + "\n-/LAPA"
        + "\n-/LC10"
        + "\n-/M1912"
        + "\n-/MAC"
        + "\n-/Marco"
        + "\n-/Milano"
        + "\n-/MP40"
        + "\n-/MP5CW"
        + "\n-/MP5MW"
        + "\n-/MP7"
        + "\n-/OTS9"
        + "\n-/Owen"
        + "\n-/P90"
        + "\n-/PPSHCW"
        + "\n-/PPSHVG"
        + "\n-/Sten"
        + "\n-/Striker"
        + "\n-/TEC9"
        + "\n-/Type100"
        + "\n-/UGR"
        + "\n-/Uzi"
        + "\n-/Welgun"
        + "\n\nEscopetas:"
        + "\n-/Combate"
        + "\n-/Doble"
        + "\n-/E725"
        + "\n-/Einhorn"
        + "\n-/Gallo"
        + "\n-/Gracey"
        + "\n-/Hauer"
        + "\n-/Ironhide"
        + "\n-/JAK12"
        + "\n-/Modelo"
        + "\n-/Origin"
        + "\n-/R9"
        + "\n-/Street"
        + "\n-/VLK"
        + "\n\nAmetralladoras Ligeras:"
        + "\n-/Bren"
        + "\n-/Bruen"
        + "\n-/DP27"
        + "\n-/FINN"
        + "\n-/Holger"
        + "\n-/M60"
        + "\n-/M91"
        + "\n-/MG34"
        + "\n-/MG42"
        + "\n-/MG82"
        + "\n-/PKM"
        + "\n-/RAAL"
        + "\n-/RPD"
        + "\n-/SA87"
        + "\n-/Stoner"
        + "\n-/Type11"
        + "\n-/UGM8"
        + "\n-/Whitley"
        + "\n\nFusiles Tacticos:"
        + "\n-/AUGCW"
        + "\n-/Ballesta"
        + "\n-/Carv2"
        + "\n-/DMR"
        + "\n-/EBR14"
        + "\n-/G43"
        + "\n-/Kar98MW"
        + "\n-/M1"
        + "\n-/M16"
        + "\n-/M1916"
        + "\n-/MK2"
        + "\n-/R1"
        + "\n-/SKS"
        + "\n-/SPR"
        + "\n-/SVT"
        + "\n-/Type63"
        + "\n\nFusiles de Precision:"
        + "\n-/Antitanque"
        + "\n-/AX50"
        + "\n-/Dragunov"
        + "\n-/HDR"
        + "\n-/Kar98VG"
        + "\n-/M82"
        + "\n-/Pelington"
        + "\n-/Rytec"
        + "\n-/Swiss"
        + "\n-/Treslineas"
        + "\n-/Tundra"
        + "\n-/Type99"
        + "\n-/ZRG"
        + "\n\nPistolas:"
        + "\n-/1911CW"
        + "\n-/1911MW"
        + "\n-/1911VG"
        + "\n-/50GS"
        + "\n-/Ametralladora"
        + "\n-/AMP"
        + "\n-/Diamatti"
        + "\n-/Klauser"
        + "\n-/M19"
        + "\n-/Magnum"
        + "\n-/Marshal"
        + "\n-/P357"
        + "\n-/RATT"
        + "\n-/Renetti"
        + "\n-/Sykov"
        + "\n-/Topbreak"
        + "\n-/X16")

def getListBonus():     #Return a string with a list of stats commands
    return ("\n\n-----Bonus-----"
        + "\n-/Alla"
        + "\n-/Cod"
        + "\n-/Conectados"
        + "\n-/Guarson"
        + "\n-/Manco"
        + "\n-/Mancolorian"
        + "\n-/Quaqua")

def getListLobbys():     #Return a string with a list of stats commands
    return ("\n\nLobbys:"
        + "\n-/LobbyBerisso1"
        + "\n-/LobbyBolsonaro"
        + "\n-/LobbyHormigator"
        + "\n-/LobbyLeko"
        #+ "\n-/LobbyLuquitas"
        + "\n-/LobbyMandalorian"
        #+ "\n-/LobbyPablo"
        #+ "\n-/LobbyRapax"
        + "\n-/Matchmaking"
        + "\n-/Tabla")

def getListStats():     #Return a string with a list of stats commands
    return ("\n\nStats:"
        + "\n-/Berisso1"
        + "\n-/Bolsonaro"
        + "\n-/Hormigator"
        + "\n-/Leko"
        #+ "\n-/Luquitas"
        + "\n-/Mandalorian"
        #+ "\n-/Pablo"
        #+ "\n-/Rapax"
        + "\n\nKD:"
        + "\n-/Berisso1KD"
        + "\n-/BolsonaroKD"
        + "\n-/HormigatorKD"
        + "\n-/LekoKD"
        #+ "\n-/LuquitasKD"
        + "\n-/MandalorianKD"
        #+ "\n-/PabloKD"
        #+ "\n-/RapaxKD"
        )

def getListStreamers():     #Return a string with streamers list
    return ("\nStreamers:"
        + "\n-/Aydan (Loadout de Aydan)"
        + "\n-/LobbyAmir"
        + "\n-/LobbyAydan"
        + "\n-/LobbyFlexz"
        + "\n-/LobbyIron"
        + "\n-/LobbyMirrey"
        + "\n-/LobbySoki"
        + "\n-/LobbyTaison"
        + "\n-/Mutex (Loadout de Mutex)")