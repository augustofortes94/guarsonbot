from resources.commands.commandsMenu import defineLogs
from ..api.guarsonapi import getWeaponFromApi


# ARMAS
def ak47(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK-47")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AK-47:\n\n-Para AK-47 de ColdWar /AK47CW\n-Para AK-47 de Modern Warfare /AK47MW")


def aug(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AUG")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AUG:\n\n-Para AUG de ColdWar /AUGCW\n-Para AUG de Modern Warfare /AUGMW")


def kar98(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kar98")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kar98k:\n\n-Para Kar98k de Modern Warfare /Kar98MW\n-Para Kar98k de Vanguard /Kar98VG")


def m1(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M1 Garand")
    context.bot.send_message(chat_id=update.effective_chat.id, text=getWeaponFromApi('M1Garand'))


def m4(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M4")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M4:\n\n-Para M4 de ColdWar /XM4\n-Para M4 de Modern Warfare /M4A1")


def mp5(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP5")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MP5:\n\n-Para MP5 de ColdWar /MP5CW\n-Para MP5 de Modern Warfare /MP5MW")


def p1911(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por 1911")
    context.bot.send_message(chat_id=update.effective_chat.id, text="1911:\n\n-Para 1911 de ColdWar /1911CW\n-Para 1911 de Modern Warfare /1911MW\n-Para 1911 de Vanguard /1911VG")


def ppsh(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PPSH")
    context.bot.send_message(chat_id=update.effective_chat.id, text="PPSH-41:\n\n-Para PPSH-41 de ColdWar /PPSHCW\n-Para PPSH-41 de Vanguard /PPSHVG")


def type(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type:\n\n-Para Type 11 de Vanguard /Type11\n-Para Type 63 de ColdWar /Type63\n-Para Type 99 de Vanguard /Type99\n-Para Type 100 de Vanguard /Type100")


def vargo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Vargo 52")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Vargo:\n\n-Para Vargo 52 de Coldwar /Vargo52\n-Para Vargo-S de Vanguard /VargoS")

# HARDCODE WEAPONS



def ak47cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK47CW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AK-47 (ColdWar):\n\n-Silenciador GRU\n-Cañon Spetsnaz de 58.4 cm\n-Mira Axial Arms x3\n-Acople Empuñadura Spetsnaz\n-Municion de 45 balas\n\nAlternativa: Para AK-47 de Modern Warfare preguntar por /AK47MW")

def ak47mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK47MW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AK-47 (Modern Warfare):\n\n-Silenciador Monolitico\n-Cañon Rumano de 58.4 cm\n-Laser Tactico\n-Municion de 40 balas\n-Ventaja Prestidigitacion\n\nAlternativa: Para AK-47 de ColdWar preguntar por /AK47CW")

def ak74u(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK74U")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AK74u:\n\n-Silenciador Gru\n-Cañon Fuerza Operativa de 40.6 cm\n-Culata de Armazon KGB\n-Municion Tambor Spetsnaz de 50 balas\n-Empuñadura Trasera de Serpiente\n\nAlternativa: reemplazar Culata de Armazon KGB por Mira LED Microflex")

def ametralladora(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Ametralladora")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pistola Ametralladora:\n\n-Silenciador M1929\n-Cañon VDD de 140 mm HE\n-Mira Reflector Slate\n-Sistema del Gatillo Estable\n-Cargadores de 8 mm Nambu con 20 Proyectiles\n-Municion Incendiaria\n-Empuñadura de Cuero\n-Ventaja 1 Refuerzo\n-Ventaja 2 Rapido")

def amp(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AMP")
    context.bot.send_message(chat_id=update.effective_chat.id, text=".50 GS:\n\n-Silenciador Agency\n-Cañon Fuerza Operativa de 18.3 cm\n-Laser Mira Laser SWAT de 5 mW\n-Culata a dos Manos\n-Municion Cargador Rapido Salvo de 23 balas")

def an94(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AN94")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AN94:\n\n-Silenciador Monolitico\n-Cañon AN94 Estandar X de 438mm\n-Mira x3 VLK\n-Acople Frontal de Ranger\n-Municion Cargador de Caja Curvos de 60 balas")

def antitanque(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Antitanque")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fusil Antitanque Gorenko:\n\n-Silenciador Mercury\n-Cañon Empress de 420 mm\n-Mira PU para SVT-40 (x3-6)\n-Culata Reforzada\n-Acople Bipode\n-Cargadores de 13 mm con 10 Proyectiles\n-Municion Alargada\n-Empuñadura Trasera Punteada\n-Ventaja 1 Velo\n-Ventaja 2 Totalmente Cargado")

def armaguerra(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Armaguerra")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Armaguerra 43:\n\n-Amplificador de Retroceso\n-Cañon Botti 570 mm Precisione\n-Mira Reflector Slate\n-Culata Imerito SA Plegable\n-Acople M1930 Guerrillero en Angulo\n-Cargadores de 9 mm con 60 Proyectiles\n-Municion Subsonica\n-Empuñadura Trasera con Cinta\n-Ventaja 1 Vital\n-Ventaja 2 Rapido")

def p1911cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P1911CW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="1911 (ColdWar):\n\n-Silenciador Agency\n-Cañon Fuerza Operativa de 16.6 cm\n-Laser Foco de Equipo de Tigre\n-Municion de 12 balas\n-Empuñadura Trasera de Serpiente\n\nAlternativa: Para 1911 de Modern Warfare preguntar por /1911MW Para 1911 de Vanguard preguntar por /1911VG")

def p1911mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P1911MW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="1911 (Modern Warfare):\n\n-Cañon 1911 Acechador\n-Laser de 5 mW\n-Sistema de Gatillo Ligero\n-Municion de 15 balas\n-Ventaja Duales\n\nAlternativa: ara 1911 de ColdWar preguntar por /1911CW Para 1911 de Vanguard preguntar por /1911VG")

def p1911vg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P1911VG")
    context.bot.send_message(chat_id=update.effective_chat.id, text="1911 (Vanguard):\n\n-Boca de Cañon Estabilizador F8\n-Cañon Cooper de 16.51 cm\n-Mira G16 x 2.5\n-Sistema del Gatillo Ligero\n-Cargadores de Calibre 45 ACP con 18 Proyectiles\n-Municion Incendiaria\n-Empuñadura con Brea de Pino\n-Ventaja 1 Duales\n-Ventaja 2 Totalmente Cargado\n\nAlternativa: Para 1911 de ColdWar preguntar por /1911CW Para 1911 de Modern Warfare preguntar por /1911MW")

def p50gs(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P50GS")
    context.bot.send_message(chat_id=update.effective_chat.id, text=".50 GS:\n\n-Cañon Forge TAC ampliado\n-Laser de 5 mW\n-Sistema de Gatillo Ligero\n-Municion de 13 balas\n-Ventaja Duales")
