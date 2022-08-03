import logging
import datetime
import os
import requests
from ..api.guarsonapi import getListCommands, getListWeaponCommands, getWeaponFromApi, login
from ..api.codapi import getLobbyTotalInfo


# Defino la info para los logs
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


# COMMAND HANDLER
def commandRegex(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por " + update['message']['text'][1:])
    cookie = login()
    data = requests.get(os.getenv('apiurl') + 'api/commands/?command=' + update['message']['text'][1:], cookies=cookie).json()
    try:
        if data['command']['category'] == 'Lobbys':
            update.message.reply_text(getLobbyTotalInfo(data['command']['parameter1'], data['command']['parameter2']))
        elif 'usiles' in data['command']['category'] or 'Escopeta' in data['command']['category'] or 'Pistolas' in data['command']['category'] or 'Ametralladoras Ligeras' in data['command']['category']:
            update.message.reply_text(getWeaponFromApi(data['command']['name'], cookie))
        elif data['command']['category'] == 'Bonus':
            update.message.reply_text(data['command']['text'].replace('/n', "\n"))
        elif data['command']['category'] == 'Streamers':
            if data['command']['category']['text']:
                update.message.reply_text(data['command']['text'].replace('/n', "\n"))
            else:
                update.message.reply_text(getLobbyTotalInfo(data['command']['parameter1'], data['command']['parameter2']))
    except:
        update.message.reply_text('No se encontro el comando')


# COMANDOS
def armas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Armas")
    update.message.reply_text("/Comandos para armas:\n\n" + getListWeaponCommands())


def comandos(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos")
    update.message.reply_text(
                            "/Hola soy el /bot Guarson, hasta ahora los /Comandos disponibles son los siguientes:\n\n"
                            + "\n-----/Armas-----\n"
                            + getListWeaponCommands()
                            + "\n\n-----/Streamers-----"
                            + getListCommands('Streamers')
                            + getListCommands('Bonus')
                            + "\n\n-----/Stats-----"
                            + getListStats()
                            + "\n\n-----/Lobbys-----"
                            + getListCommands('Lobbys')
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


# CERTIFICADO
def certified(update, context):     # Devuelvo el vencimiento del certificado SSO
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Certificado")
    expire_date = int(os.getenv('SSO_EXPIRE'))
    update.message.reply_text("Vence el: " + str(datetime.datetime.fromtimestamp(expire_date/1000)))


def getListLobbys():     # Return a string with a list of stats commands
    return ("\n\nLobbys:"
            + "\n-/LobbyBerisso1"
            + "\n-/LobbyBolsonaro"
            + "\n-/LobbyHormigator"
            + "\n-/LobbyLeko"
            # + "\n-/LobbyLuquitas"
            + "\n-/LobbyMandalorian"
            # + "\n-/LobbyPablo"
            # + "\n-/LobbyRapax"
            + "\n-/Matchmaking"
            + "\n-/Tabla"
            )


def getListStats():     # Return a string with a list of stats commands
    return ("\n\nStats:"
            + "\n-/Berisso1"
            + "\n-/Bolsonaro"
            + "\n-/Hormigator"
            + "\n-/Leko"
            # + "\n-/Luquitas"
            + "\n-/Mandalorian"
            # + "\n-/Pablo"
            # + "\n-/Rapax"
            + "\n\nKD:"
            + "\n-/Berisso1KD"
            + "\n-/BolsonaroKD"
            + "\n-/HormigatorKD"
            + "\n-/LekoKD"
            # + "\n-/LuquitasKD"
            + "\n-/MandalorianKD"
            # + "\n-/PabloKD"
            # + "\n-/RapaxKD"
            )


def getListStreamers():     # Return a string with streamers list
    return ("\nStreamers:"
            + "\n-/Aydan (Loadout de Aydan)"
            + "\n-/LobbyAmir"
            + "\n-/LobbyAydan"
            + "\n-/LobbyFlexz"
            + "\n-/LobbyIron"
            + "\n-/LobbyMirrey"
            + "\n-/LobbySoki"
            + "\n-/LobbyTaison"
            + "\n-/Mutex (Loadout de Mutex)"
            )
