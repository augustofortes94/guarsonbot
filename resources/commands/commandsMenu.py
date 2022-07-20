import logging
import datetime
import os
from ..api.guarsonapi import getListCommands


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


# COMANDOS
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


# CERTIFICADO
def certified(update, context):     # Devuelvo el vencimiento del certificado SSO
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Certificado")
    expire_date = int(os.getenv('sso_expire'))
    update.message.reply_text("Vence el: " + str(datetime.datetime.fromtimestamp(expire_date/1000)))


# PRINTS
def getListArmas():     # Return a string with a list of weapons
    return ("\nFusiles de Asalto:"
            + getListCommands('Fusiles de Asalto')
            + "\n\nSubfusiles:"
            + getListCommands('Subfusiles')
            + "\n\nEscopetas:"
            + getListCommands('Escopetas')
            + "\n\nAmetralladoras Ligeras:"
            + getListCommands('Ametralladoras Ligeras')
            + "\n\nFusiles Tacticos:"
            + getListCommands('Fusiles Tacticos')
            + "\n\nFusiles de Precision:"
            + getListCommands('Fusiles de Precision')
            + "\n\nPistolas:"
            + getListCommands('Pistolas')
            )


def getListBonus():     # Return a string with a list of stats commands
    return ("\n\n-----Bonus-----"
            + "\n-/Alla"
            + "\n-/Cod"
            + "\n-/Conectados"
            + "\n-/Guarson"
            + "\n-/Manco"
            + "\n-/Mancolorian"
            + "\n-/Quaqua"
            )


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
