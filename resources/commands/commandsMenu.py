import logging
import datetime
import os
import requests
from ..api.guarsonapi import getListCommands, getListWeaponCommands, getWeaponFromApi, getToken
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
    # Consulto para obtener la categoria del comando asi se que endpoint consultar para el contenido del comando (MEJORABLE)
    headers = {'Authorization': 'Bearer ' + getToken()}
    data = requests.get(os.getenv('apiurl') + 'api/commands/?command=' + update['message']['text'][1:], headers=headers).json()
    mssg = context.bot.send_message
    try:
        if data['command']['category'] == 'Lobbys':
            mssg(chat_id=update.effective_chat.id, text=getLobbyTotalInfo(data['command']['parameter1'], data['command']['parameter2']))
        elif 'usiles' in data['command']['category'] or 'Escopeta' in data['command']['category'] or 'Pistolas' in data['command']['category'] or 'Ametralladoras Ligeras' in data['command']['category']:
            mssg(chat_id=update.effective_chat.id, text=getWeaponFromApi(data['command']['name'], headers))
        elif data['command']['category'] == 'Bonus':
            mssg(chat_id=update.effective_chat.id, text=data['command']['text'].replace('/n', "\n"))
        elif data['command']['category'] == 'Streamers':
            if data['command']['text'] is not None:
                mssg(chat_id=update.effective_chat.id, text=data['command']['text'].replace('/n', "\n"))
            else:
                mssg(chat_id=update.effective_chat.id, text=getLobbyTotalInfo(data['command']['parameter1'], data['command']['parameter2']))
    except:
        mssg(chat_id=update.effective_chat.id, text='No se encontro el comando')


# COMANDOS
def armas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Armas")
    #context.bot.send_message(chat_id=update.effective_chat.id, text="/Comandos para armas:\n\n" + getListWeaponCommands())
    context.bot.send_message(chat_id=update.effective_chat.id, text="/Comandos para armas:\n\n"
                                                                    + '\nFusiles de Asalto:'
                                                                    + '\n-/AK47CW'
                                                                    + '\n-/AK47MW'
                                                                    + '\n-/AN94'
                                                                    + '\n-/AS44'
                                                                    + '\n-/ASVAL'
                                                                    + '\n-/Automata'
                                                                    + '\n-/BAR'
                                                                    + '\n-/BP50'
                                                                    + '\n-/C58'
                                                                    + '\n-/Cooper'
                                                                    + '\n-/CR56'
                                                                    + '\n-/EM2'
                                                                    + '\n-/EX1'
                                                                    + '\n-/FAL'
                                                                    + '\n-/FARA'
                                                                    + '\n-/FFAR'
                                                                    + '\n-/FR556'
                                                                    + '\n-/Grau'
                                                                    + '\n-/Grav'
                                                                    + '\n-/Groza'
                                                                    + '\n-/ITRA'
                                                                    + '\n-/'

                                                                    + '\n\nSubfusiles:'
                                                                    + '\n-/AK74U'
                                                                    + '\n-/Armaguerra'
                                                                    + '\n-/Bizon'
                                                                    + '\n-/Blixen'
                                                                    + '\n-/Bullfrog'
                                                                    + '\n-/CX9'
                                                                    + '\n-/Fennec'
                                                                    + '\n-/ISO'
                                                                    + '\n-/'

                                                                    + '\n\nEscopetas:'
                                                                    + '\n-/Combate'
                                                                    + '\n-/Doble'
                                                                    + '\n-/E725'
                                                                    + '\n-/Einhorn'
                                                                    + '\n-/Gallo'
                                                                    + '\n-/Gracey'
                                                                    + '\n-/Hauer'
                                                                    + '\n-/Ironhide'
                                                                    + '\n-/'

                                                                    + '\n\nAmetralladoras Ligeras:'
                                                                    + '\n-/Bren'
                                                                    + '\n-/Bruen'
                                                                    + '\n-/DP27'
                                                                    + '\n-/FINN'
                                                                    + '\n-/Holger'
                                                                    + '\n-/'

                                                                    + '\n\nFusiles Tacticos:'
                                                                    + '\n-/AUGCW'
                                                                    + '\n-/AUGMW'
                                                                    + '\n-/Ballesta'
                                                                    + '\n-/Carv2'
                                                                    + '\n-/DMR'
                                                                    + '\n-/EBR14'
                                                                    + '\n-/G43'
                                                                    + '\n-/'

                                                                    + '\n\nFusiles de Precision:'
                                                                    + '\n-/Antitanque'
                                                                    + '\n-/AX50'
                                                                    + '\n-/Dragunov'
                                                                    + '\n-/HDR'
                                                                    + '\n-/'

                                                                    + '\n\nPistolas:'
                                                                    + '\n-/1911CW'
                                                                    + '\n-/1911MW'
                                                                    + '\n-/1911VG'
                                                                    + '\n-/50GS'
                                                                    + '\n-/Ametralladora'
                                                                    + '\n-/AMP'
                                                                    + '\n-/Diamatti'
                                                                    + '\n-/')

"""
def comandos(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos")
    context.bot.send_message(chat_id=update.effective_chat.id, text=
                                                                    "/Hola soy el /bot Guarson, hasta ahora los /Comandos disponibles son los siguientes:\n\n"
                                                                    + "\n-----/Armas-----\n"
                                                                    + getListWeaponCommands()
                                                                    + "\n\n-----/Streamers-----"
                                                                    + getListCommands('Streamers')
                                                                    + "\n"
                                                                    + getListCommands('Bonus')
                                                                    #+ "\n\n-----/Stats-----"
                                                                    #+ getListStats()
                                                                    + "\n\n-----/Lobbys-----"
                                                                    + getListCommands('Lobbys')
                                                                    )"""

def comandos(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos")
    context.bot.send_message(chat_id=update.effective_chat.id, text=
                                                                    "/Hola soy el /bot Guarson, hasta ahora los /Comandos disponibles son los siguientes:\n\n"
                                                                    + "\n-----/Armas-----\n"
                                                                    + armas()
                                                                    + "\n\n-----/Streamers-----"
                                                                    #+ getListCommands('Streamers')
                                                                    + "\n"
                                                                    #+ getListCommands('Bonus')
                                                                    #+ "\n\n-----/Stats-----"
                                                                    #+ getListStats()
                                                                    + "\n\n-----/Lobbys-----"
                                                                    #+ getListCommands('Lobbys')
                                                                    )

def hola(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hola")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hola {update.effective_user['username']}, soy guarson, un bot creado para LMD2 con la intencion de dejar guardado todas las configuraciones de armas de Warzone, como asi tambien ofrecer estadisticas de las lobbies de los miembros del clan.")


def lobbys(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Lobbys")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/Comandos para Lobbys:\n\n" + getListCommands('Lobbys'))


def stats(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Estadisticas")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/Comandos para estadisticas:\n\n" + getListStats() + getListCommands('Lobbys'))


def streamers(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Streamers")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/Comandos para streamers:\n\n" + getListCommands('Streamers'))


# CERTIFICADO
def certified(update, context):     # Devuelvo el vencimiento del certificado SSO
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Certificado")
    expire_date = int(os.getenv('SSO_EXPIRE'))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Vence el: " + str(datetime.datetime.fromtimestamp(expire_date/1000)))
    

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
