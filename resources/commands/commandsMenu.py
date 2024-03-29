import logging
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
    data = requests.get(os.getenv('apiurl') + 'api/commands/?command=' + update['message']['text'][1:] + '&warzone_version=' + os.getenv('warzone_version'), headers=headers).json()
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
    context.bot.send_message(chat_id=update.effective_chat.id, text="/Comandos para armas:\n\n" + getListWeaponCommands())
    """
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
                                                                    + '\n-/KGM40'
                                                                    + '\n-/Kilo'
                                                                    + '\n-/Krig'
                                                                    + '\n-/M13'
                                                                    + '\n-/M4A1'
                                                                    + '\n-/Nikita'
                                                                    + '\n-/NZ41'
                                                                    + '\n-/Oden'
                                                                    + '\n-/QBZ'
                                                                    + '\n-/RAM'
                                                                    + '\n-/Scar'
                                                                    + '\n-/STG'
                                                                    + '\n-/Vargo52'
                                                                    + '\n-/Vargos'
                                                                    + '\n-/Volks'
                                                                    + '\n-/XM4'

                                                                    + '\n\nSubfusiles:'
                                                                    + '\n-/AK74U'
                                                                    + '\n-/Armaguerra'
                                                                    + '\n-/Bizon'
                                                                    + '\n-/Blixen'
                                                                    + '\n-/Bullfrog'
                                                                    + '\n-/CX9'
                                                                    + '\n-/Fennec'
                                                                    + '\n-/ISO'
                                                                    + '\n-/KSP'
                                                                    + '\n-/LAPA'
                                                                    + '\n-/LC10'
                                                                    + '\n-/M1912'
                                                                    + '\n-/MAC'
                                                                    + '\n-/Marco'
                                                                    + '\n-/Milano'
                                                                    + '\n-/MK2'
                                                                    + '\n-/MP40'
                                                                    + '\n-/MP5CW'
                                                                    + '\n-/MP5MW'
                                                                    + '\n-/MP7'
                                                                    + '\n-/OTS9'
                                                                    + '\n-/Owen'
                                                                    + '\n-/P90'
                                                                    + '\n-/PPSHCW'
                                                                    + '\n-/PPSHVG'
                                                                    + '\n-/RA225'
                                                                    + '\n-/Sten'
                                                                    + '\n-/Striker'
                                                                    + '\n-/TEC9'
                                                                    + '\n-/Type100'
                                                                    + '\n-/UGR'
                                                                    + '\n-/Uzi'
                                                                    + '\n-/Welgun'

                                                                    + '\n\nEscopetas:'
                                                                    + '\n-/Combate'
                                                                    + '\n-/Doble'
                                                                    + '\n-/E725'
                                                                    + '\n-/Einhorn'
                                                                    + '\n-/Gallo'
                                                                    + '\n-/Gracey'
                                                                    + '\n-/Hauer'
                                                                    + '\n-/Ironhide'
                                                                    + '\n-/JAK12'
                                                                    + '\n-/Modelo'
                                                                    + '\n-/Origin'
                                                                    + '\n-/R9'
                                                                    + '\n-/Street'
                                                                    + '\n-/VLK'

                                                                    + '\n\nAmetralladoras Ligeras:'
                                                                    + '\n-/Bren'
                                                                    + '\n-/Bruen'
                                                                    + '\n-/DP27'
                                                                    + '\n-/FINN'
                                                                    + '\n-/Holger'
                                                                    + '\n-/Lienna'
                                                                    + '\n-/M60'
                                                                    + '\n-/M91'
                                                                    + '\n-/MG34'
                                                                    + '\n-/MG42'
                                                                    + '\n-/MG82'
                                                                    + '\n-/PKM'
                                                                    + '\n-/RAAL'
                                                                    + '\n-/RPD'
                                                                    + '\n-/SA87'
                                                                    + '\n-/Stoner'
                                                                    + '\n-/Type11'
                                                                    + '\n-/UGM8'
                                                                    + '\n-/Whitley'

                                                                    + '\n\nFusiles Tacticos:'
                                                                    + '\n-/AUGCW'
                                                                    + '\n-/AUGMW'
                                                                    + '\n-/Ballesta'
                                                                    + '\n-/Carv2'
                                                                    + '\n-/DMR'
                                                                    + '\n-/EBR14'
                                                                    + '\n-/G43'
                                                                    + '\n-/Kar98MW'
                                                                    + '\n-/M16'
                                                                    + '\n-/M1916'
                                                                    + '\n-/M1Garand'
                                                                    + '\n-/R1'
                                                                    + '\n-/SKS'
                                                                    + '\n-/SVT'
                                                                    + '\n-/Type63'

                                                                    + '\n\nFusiles de Precision:'
                                                                    + '\n-/Antitanque'
                                                                    + '\n-/AX50'
                                                                    + '\n-/Dragunov'
                                                                    + '\n-/HDR'
                                                                    + '\n-/Kar98VG'
                                                                    + '\n-/M82'
                                                                    + '\n-/Pelington'
                                                                    + '\n-/Rytec'
                                                                    + '\n-/SPR'
                                                                    + '\n-/Swiss'
                                                                    + '\n-/Treslineas'
                                                                    + '\n-/Tundra'
                                                                    + '\n-/Type99'
                                                                    + '\n-/ZRG'

                                                                    + '\n\nPistolas:'
                                                                    + '\n-/1911CW'
                                                                    + '\n-/1911MW'
                                                                    + '\n-/1911VG'
                                                                    + '\n-/50GS'
                                                                    + '\n-/Ametralladora'
                                                                    + '\n-/AMP'
                                                                    + '\n-/Diamatti'
                                                                    + '\n-/Klauser'
                                                                    + '\n-/M19'
                                                                    + '\n-/Magnum'
                                                                    + '\n-/Marshal'
                                                                    + '\n-/P357'
                                                                    + '\n-/RATT'
                                                                    + '\n-/Renetti'
                                                                    + '\n-/Sykov'
                                                                    + '\n-/Topbreak'
                                                                    + '\n-/X16'
                                                                    )"""

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
