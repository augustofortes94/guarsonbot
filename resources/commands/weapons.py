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


"""
def ak47cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK47CW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AK-47 (ColdWar):\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon Spetsnaz de 58.4 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n-Municion de 45 balas"
                                                                    + "\n\nPara AK-47 de Modern Warfare preguntar por /AK47MW")

def ak47mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK47MW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AK-47 (Modern Warfare):\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Rumano de 58.4 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Municion de 40 balas"
                                                                    + "\n-Ventaja Prestidigitacion"
                                                                    + "\n\nPara AK-47 de ColdWar preguntar por /AK47CW")

def ak74u(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK74U")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AK74u:\n"
                                                                    + "\n-Silenciador Gru"
                                                                    + "\n-Cañon Fuerza Operativa de 40.6 cm"
                                                                    + "\n-Culata de Armazon KGB"
                                                                    + "\n-Municion Tambor Spetsnaz de 50 balas"
                                                                    + "\n-Empuñadura Trasera de Serpiente"
                                                                    + "\n\nAlternativa: reemplazar Culata de Armazon KGB por Mira LED Microflex")

def ametralladora(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Ametralladora")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pistola Ametralladora:\n"
                                                                    + "\n-Silenciador M1929"
                                                                    + "\n-Cañon VDD de 140 mm HE"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Sistema del Gatillo Estable"
                                                                    + "\n-Cargadores de 8 mm Nambu con 20 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura de Cuero"
                                                                    + "\n-Ventaja 1 Refuerzo"
                                                                    + "\n-Ventaja 2 Rapido")

def amp(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AMP")
    context.bot.send_message(chat_id=update.effective_chat.id, text=".50 GS:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 18.3 cm"
                                                                    + "\n-Laser Mira Laser SWAT de 5 mW"
                                                                    + "\n-Culata a dos Manos"
                                                                    + "\n-Municion Cargador Rapido Salvo de 23 balas")

def an94(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AN94")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AN94:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon AN94 Estandar X de 438mm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Ranger"
                                                                    + "\n-Municion Cargador de Caja Curvos de 60 balas")

def antitanque(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Antitanque")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fusil Antitanque Gorenko:\n"
                                                                    + "\n-Silenciador Mercury"
                                                                    + "\n-Cañon Empress de 420 mm"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Reforzada"
                                                                    + "\n-Acople Bipode"
                                                                    + "\n-Cargadores de 13 mm con 10 Proyectiles"
                                                                    + "\n-Municion Alargada"
                                                                    + "\n-Empuñadura Trasera Punteada"
                                                                    + "\n-Ventaja 1 Velo\n-Ventaja 2 Totalmente Cargado")

def armaguerra(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Armaguerra")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Armaguerra 43:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon Botti 570 mm Precisione"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Imerito SA Plegable"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargadores de 9 mm con 60 Proyectiles"
                                                                    + "\n-Municion Subsonica"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Vital\n-Ventaja 2 Rapido")

def as44(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AS44")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AS44:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Kovalevskaya de 615 mm"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata ZAC 12B Personalizado"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargadores del Calibre 30 Russian Short con 60 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera Sombreada"
                                                                    + "\n-Ventaja 1 Estabilizador"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def asval(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por ASVAL")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AS-VAL:\n"
                                                                    + "\n-Cañon VLK Osa de 200mm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 30 balas"
                                                                    + "\n-Ventaja Prestidigitacion"
                                                                    + "\n\nAlternativa: reemplazar prestidigitacion por totalmente cargado o Acople Frontal de Comando por Mercenario para tiro desde la cadera")

def augcw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AUGCW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AUG (ColdWar):\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuego Rapido de 45.7 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Frontal de Agente de Campo"
                                                                    + "\n-Municion Stanag de 54 balas"
                                                                    + "\n\nPara AUG de Modern Warfare preguntar por /AUGMW")

def augmw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AUGMW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AUG (Modern Warfare):\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion Cargadores de 32 balas"
                                                                    + "\n-Empuñadura Trasera Adhesivo Punteado"
                                                                    + "\n\nPara AUG de ColdWar preguntar por /AUGCW")

def automata(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Automata")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Automata:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon ZAC de 600 mm BFA"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Anastasia Acolchada"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargador Tambores de 6.5 mm Sakura con 75 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera con Surcos"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def ax50(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AX50")
    context.bot.send_message(chat_id=update.effective_chat.id, text="AX-50:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon de Fabrica de 81.3 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata Singuard Arms Asesino"
                                                                    + "\n-Empuñadura Trasera Adhesivo Punteado"
                                                                    + "\n\nAlternativa: reemplazar Empuñadura Trasera por Municion de 9 balas")

def ballesta(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Ballesta")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ballesta MW:\n"
                                                                    + "\n-Cable de 28 Hebras"
                                                                    + "\n-Arco XRK Thunder de 91 kg"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Municion Proyectiles FTAC Fury de 50.8 cm"
                                                                    + "\n-Ventaja Prestidigitacion"
                                                                    + "\n\nPara ballesta de ColdWar preguntar por /R1")

def bar(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por BAR")
    context.bot.send_message(chat_id=update.effective_chat.id, text="BAR:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon CGC de 76.2 cm XL"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Cooper SP"
                                                                    + "\n-Acople Empuñadura Delantera para Carver"
                                                                    + "\n-Cargadores de 8 mm con 40 proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Incansable"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def bizon(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bizon")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bizon:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Acero de 22.1 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata sin Culata"
                                                                    + "\n-Empuñadura Trasera Adhesivo Punteado"
                                                                    + "\n\nPara Bizon de ColdWar preguntar por /Bullfrog")

def blixen(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Blixen")
    context.bot.send_message(chat_id=update.effective_chat.id, text="H4 Blixen:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon Bergstrom F3 de 43.18 cm"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Eliminada"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargadores Gorenko de 7.62 mm con 54 Proyectiles"
                                                                    + "\n-Municion Punta Hueca"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Rapido"
                                                                    + "\n-Ventaja 2 Rapido")

def bp50(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por BP50")
    context.bot.send_message(chat_id=update.effective_chat.id, text="BP50:\n"
                                                                    + "\n-Silenciador Mx"
                                                                    + "\n-Cañon Desmet 540 mm PMH"
                                                                    + "\n-Laser Linterna Desmet A-D"
                                                                    + "\n-Mira G16 x 2,5"
                                                                    + "\n-Culata Desmet NOM 11S"
                                                                    + "\n-Cargadores de 7.62 x 54 mm R con 50 Proyectiles"
                                                                    + "\n-Municion Alargada"
                                                                    + "\n-Empuñadura Trasera de Polimero"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def bren(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bren")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bren:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Queen's de 705 mm Royal"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Queen's Model 11 BH"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargador Tambores de Calibre 303 con 100 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera Granulada"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def bruen(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bruen")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bruen MK9:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon XRK Summit de 68.1 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Empuñadura Frontal de Comando"
                                                                    + "\n-Municion de 60 balas")

def bullfrog(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bullfrog")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bullfrog:\n"
                                                                    + "\n-Silenciador Gru"
                                                                    + "\n-Cañon Fuerza Operativa de 18.7 cm"
                                                                    + "\n-Culata PKM Spetsnaz"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente"
                                                                    + "\n\n(Viene con 50 balas)"
                                                                    + "\n\nPara Bullfrog de Modern Warfare preguntar por /Bizon")

def c58(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por C58")
    context.bot.send_message(chat_id=update.effective_chat.id, text="C58:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 47 cm"
                                                                    + "\n-Mira Axial x3"
                                                                    + "\n-Acople Empuñadura de Agente de Campo"
                                                                    + "\n-Municion Tambor de 45 balas")

def carv2(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Carv2")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Carv2:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon 52.8 cm de Equipo de Asalto"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Frontal de Agente de Campo"
                                                                    + "\n-Municion Tambor de 45 balas")

def combate(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Combate")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Escopeta de Combate:\n"
                                                                    + "\n-Boca de Cañon Estrangulador Completo para M97"
                                                                    + "\n-Cañon Chariot de 40.64 cm Corto"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata CGC 3M Ajustable"
                                                                    + "\n-Acople Armazon Mk. VI"
                                                                    + "\n-Cargador Tubo del Calibre 12 con 5 Cartuchos"
                                                                    + "\n-Municion Perdigones y Postas"
                                                                    + "\n-Empuñadura Trasera de Tela"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def cooper(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Cooper")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Carabina Cooper:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Cooper de 55.9 cm Personalizado"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Acolchado Personalizado"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Tambores de 9 mm con 60 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera Punteada"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def cr56(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por CR56")
    context.bot.send_message(chat_id=update.effective_chat.id, text="CR-56 Amax:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon XRK Zodiac S440"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Ranger"
                                                                    + "\n-Municion de 45 balas")

def cx9(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por CX9")
    context.bot.send_message(chat_id=update.effective_chat.id, text="CX9:\n"
                                                                    + "\n-Cañon CX-38S"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion Tambor de 50 balas"
                                                                    + "\n-Empuñadura Trasera CX-9 Tac")

def diamatti(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Diamatti")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Diamatti:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 18.3 cm"
                                                                    + "\n-Laser Mira Laser SWAT de 5 mW"
                                                                    + "\n-Municion Cargador Rapido Salvo de 30 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente"
                                                                    + "\n\nAlternativa: Reemplazar Empuñadura Trasera Vendaje de Serpiente por Culata a dos Manos")

def dmr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por DMR")
    context.bot.send_message(chat_id=update.effective_chat.id, text="DMR:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 52.8 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Frontal de Agente de Campo"
                                                                    + "\n-Municion Stanag de 40 balas")

def doble(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Doble")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Doble Cañon:\n"
                                                                    + "\n-Estrangulador Completo para M97"
                                                                    + "\n-Cañon Recortada"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Eliminada"
                                                                    + "\n-Acople Empuñadura de Pistola para SMLA"
                                                                    + "\n-Cargador Algo Doble"
                                                                    + "\n-Municion Punta Hueca"
                                                                    + "\n-Empuñadura Trasera de Tela"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Rapido")

def dp27(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por DP27")
    context.bot.send_message(chat_id=update.effective_chat.id, text="DP27:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Kovalevskaya de 680 mm B02D"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata ZAC S3 TAK"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargadores de Ruleta de Calibre 30-06 con 81 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Incansable"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def dragunov(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Dragunov")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Dragunov:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Ampliado de 660 mm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata FTAC Cazador-Explorador"
                                                                    + "\n-Municion Cargador de 20 balas")

def e725(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por E725")
    context.bot.send_message(chat_id=update.effective_chat.id, text="725:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Tempus de Competencia"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata Recortada"
                                                                    + "\n-Municion Cartuchos de Balas")

def ebr14(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por EBR14")
    context.bot.send_message(chat_id=update.effective_chat.id, text="EBR-14:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Forge TAC de Precision de 55.9 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 20 balas")

def einhorn(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Einhorn")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Einhorn Rotativa:\n"
                                                                    + "\n-Estrangulador Completo para M97"
                                                                    + "\n-Cañon Klauser de 560 mm Rapido"
                                                                    + "\n-Mira G16 x 2.5"
                                                                    + "\n-Culata VDD Hunter"
                                                                    + "\n-Acople Empuñadura de Pistola para SMLE"
                                                                    + "\n-Cargador Cilindro de Calibre 16 con 12 Proyectiles"
                                                                    + "\n-Municion Perdigones y Postas"
                                                                    + "\n-Empuñadura Trasera de Tela"
                                                                    + "\n-Ventaja 1 Prestidigitacion"
                                                                    + "\n-Ventaja 2 Rapido")

def em2(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por EM2")
    context.bot.send_message(chat_id=update.effective_chat.id, text="EM2:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 65.5 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion Stanag de 50 balas"
                                                                    + "\n\nAlternativa Subfusil: reemplazar Silenciador Agency por Silenciador, mira por Mira LED Microflex, cañon por Culata Raider y Municion de 40 balas")

def ex1(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por EX1")
    context.bot.send_message(chat_id=update.effective_chat.id, text="EX1:\n"
                                                                    + "\n-Amplificador de Bobina"
                                                                    + "\n-Cañon SD Grat Instantaneo"
                                                                    + "\n-Mira G16 x 2,5"
                                                                    + "\n-Culata Ancla AC-Titanium"
                                                                    + "\n-Acople Tope de Mano de Iones"
                                                                    + "\n-Cargador Bateria de Carga Rapida Actual PWN"
                                                                    + "\n-Empuñadura Trasera de Polimero"
                                                                    + "\n-Ventaja 1 Observador"
                                                                    + "\n-Ventaja 2 Disponible")

def fal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FAL")
    context.bot.send_message(chat_id=update.effective_chat.id, text="FN FAL:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon XRK de Tirador"
                                                                    + "\n-Mira Reflex IG Mini"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 30 balas"
                                                                    + "\n\nAlternativa: reemplazar mira reflex IG por x3 VLK")

def fara(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FARA")
    context.bot.send_message(chat_id=update.effective_chat.id, text="FARA 83:\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon Spetsnaz RPK de 47.5 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n-Municion Spetsnaz de 50 balas")

def fennec(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Fennec")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fennec:\n"
                                                                    + "\n-Cañon ZLR Deadfall de 45.7 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Acople Empuñadura Frontal de Comando"
                                                                    + "\n-Municion Tambor de 40 balas"
                                                                    + "\n-Empuñadura Trasera Adhesivo Engomado")

def ffar(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FFAR")
    context.bot.send_message(chat_id=update.effective_chat.id, text="FFAR1:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 40.6 cm"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion Stanag de 50 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def finn(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FINN")
    context.bot.send_message(chat_id=update.effective_chat.id, text="FINN LMG:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon XRK Longshot Adverso"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n\nAlternativa: reemplazar mira por Municion Cintas de 75 balas 5.56 CT para movilidad")

def fr556(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FR556")
    context.bot.send_message(chat_id=update.effective_chat.id, text="FR 5.56:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon FR de Francotirador de 62 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 50 balas")

def g43(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por G43")
    context.bot.send_message(chat_id=update.effective_chat.id, text="G-43:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Wyvern de Rafagas"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Fitzherbert Reforzada"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargador Tambores de 8 mm Klauser con 20 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Totalmente Cargado"
                                                                    + "\n\nAlternativa: Reemplazar el cañon por Cañon ZP de 770 mm de Precision")

def gallo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Gallo")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Gallo SA12:\n"
                                                                    + "\n-Estrangulador Agency"
                                                                    + "\n-Cañon Reforzado Pesado de 54.3 cm"
                                                                    + "\n-Culata Maraton"
                                                                    + "\n-Municion Tambor Stanag de 12 balas"
                                                                    + "\n-Empuñadura Trasera de Serpiente")

def gracey(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Gracey")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Gracey Automatica:\n"
                                                                    + "\n-Boca de Cañon Estrangulador Completo para M97"
                                                                    + "\n-Cañon CGC de 55.88 cm Rapido"
                                                                    + "\n-Mira G16 x 2.5"
                                                                    + "\n-Culata Chariot Deportiva"
                                                                    + "\n-Acople Empuñadura de Pistola para SMLE"
                                                                    + "\n-Tambores de Calibre 12 con 10 Cartuchos"
                                                                    + "\n-Municion Perdigones y Postas"
                                                                    + "\n-Empuñadura Trasera de Tela"
                                                                    + "\n-Ventaja 1 Arrollador"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def grau(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Grau")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Grau:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Tempus Arcangel de 67.1 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 60 balas"
                                                                    + "\n\nAlternativa: reemplazar Mira por Laser Tactico")

def grav(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Grav")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Grav:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 54.10 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion de 50 balas")

def groza(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Groza")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Groza:\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon Grado Militar CMV de 42 cm"
                                                                    + "\n-Culata Almohadilla de la KGB"
                                                                    + "\n-Acople Empuñadura Rapida Spetsnaz"
                                                                    + "\n-Municion Tambor Spetsnaz de 60 balas"
                                                                    + "\n\nAlternativa: Cambiar Culata por Mira Axial Arms x3")

def hauer(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hauer")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hauer 77:\n"
                                                                    + "\n-Boca de Cañon Estrangulador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 40.6 cm"
                                                                    + "\n-Laser Identificador de Objetivos FOE"
                                                                    + "\n-Culata sin Culata"
                                                                    + "\n-Municion Tubo de 7 balas")

def hdr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por HDR")
    context.bot.send_message(chat_id=update.effective_chat.id, text="HDR:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon HDR Pro de 68.3 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Mira Optica con Zoom Variable"
                                                                    + "\n-Culata FTAC Campeon"
                                                                    + "\n\nAlternativa: reemplazar Laser Tactico por Municion de 7 u 9 balas")

def holger(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Holger")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Holger-26:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Empuñadura Trasera Adhesivo Punteado")

def ironhide(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Ironhide")
    context.bot.send_message(chat_id=update.effective_chat.id, text=".410 Ironhide:\n"
                                                                    + "\n-Boca de Cañon Estrangulador Agency"
                                                                    + "\n-Cañon Forjado a Mano de 43.43 cm"
                                                                    + "\n-Culata Maraton"
                                                                    + "\n-Municion Tubo Stanag de 8 proyectiles"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def iso(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por ISO")
    context.bot.send_message(chat_id=update.effective_chat.id, text="ISO:\n"
                                                                    + "\n-Cañon FSS Nightshade"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata Plegable ISO"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion Tambor de 50 balas")

def itra(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por ITRA")
    context.bot.send_message(chat_id=update.effective_chat.id, text="ITRA de Rafagas:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Perfetto de 140 mm Rapido"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Empuñadura Acolchada Perfetto"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargador Tambores de 8 mm Klauser con 32 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def jak12(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por JAK12")
    context.bot.send_message(chat_id=update.effective_chat.id, text="JAK12:\n"
                                                                    + "\n-Boca de Cañon Forge TAC Merodeador"
                                                                    + "\n-Cañon ZLR J-2800 Influx"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Acople Frontal de Mercenario"
                                                                    + "\n-Municion Aliento de Dragon de 8 Cartuchos")

def kar98mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kar98MW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kar98k (Modern Warfare):\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Singuard Personalizado de 63.8 cm"
                                                                    + "\n-Mira Optica con Zoom Variable"
                                                                    + "\n-Empuñadura Trasera Adhesivo Punteado"
                                                                    + "\n-Ventaja Prestidigitacion"
                                                                    + "\n\nAlternativa: reemplazar Ventaja Prestidigitacion por Laser Tactico y Mira Zoom Variable por Mira de Francotirador"
                                                                    + "\n\nPara Kar98k de Vanguard /Kar98VG")

def kar98vg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kar98VG")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kar98k (Vanguard):\n"
                                                                    + "\n-Silenciador SD"
                                                                    + "\n-Cañon VDD de 660 mm 05HE"
                                                                    + "\n-Culata VDD 98"
                                                                    + "\n-Acople Empuñadura Delantera Pesada"
                                                                    + "\n-Cargadores Rapidos de 8 mm Klauser con 5 Proyectiles"
                                                                    + "\n-Municion Alargada"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Velo"
                                                                    + "\n-Ventaja 2 Totalmente Cargado"
                                                                    + "\n\nPara Kar98k de Modern Warfare /Kar98MW")

def kgm40(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por KGM40")
    context.bot.send_message(chat_id=update.effective_chat.id, text="KG M40:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Reisdorf de 720 mm Cubierta"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata VDD 22G Acolchada"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargador Tambores Calibre 30-06 con 60 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera Granulada"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def kilo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kilo")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kilo:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Singuard Arms de Merodeador de 50.3 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 60 balas")

def klauser(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Klauser")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Klauser:\n"
                                                                    + "\n-Silenciador M1929"
                                                                    + "\n-Cañon Fitzherbert de 200 mm BL"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Sistema del Gatillo Accion Rapida"
                                                                    + "\n-Cargadores del Calibre 45 ACP con 12 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura de Tela"
                                                                    + "\n-Ventaja 1 Prestidigitacion"
                                                                    + "\n-Ventaja 2 Rapido")

def krig(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Krig")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Krig 6:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon CMV Militar de 38.1 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura de Agente de Campo"
                                                                    + "\n-Municion Stanag de 60 balas")

def ksp(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por KSP")
    context.bot.send_message(chat_id=update.effective_chat.id, text="KSP 45:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 40.6 cm"
                                                                    + "\n-Mira LED Microflex"
                                                                    + "\n-Acople Empuñadura Frontal de Agente de Campo"
                                                                    + "\n-Municion Stanag de 48 balas")

def lapa(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por LAPA")
    context.bot.send_message(chat_id=update.effective_chat.id, text="LAPA:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Estriado de 20 cm"
                                                                    + "\n-Mira LED Microflex"
                                                                    + "\n-Municion Stanag de 50 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def lc10(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por LC10")
    context.bot.send_message(chat_id=update.effective_chat.id, text="LC-10:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Reforzado Pesado de 30.2 cm"
                                                                    + "\n-Acople Empuñadura de Agente de Campo"
                                                                    + "\n-Municion Stanag de 55 balas"
                                                                    + "\n-Empuñadura Trasera de la Jungla SASR")

def lienna(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lienna")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lienna 57:\n"
                                                                    + "\n-Silenciador Mx"
                                                                    + "\n-Cañon Frei de 432 mm Cubierto"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Baumann GMK-2"
                                                                    + "\n-Empuñadura Delantera para Carver"
                                                                    + "\n-Cargadores de 8 mm Klauser con 50 Proyectiles"
                                                                    + "\n-Municion Alargada"
                                                                    + "\n-Empuñadura Trasera de Polimero"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def m13(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M13")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M13:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Tempus de Tirador"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 60 balas")

def m16(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M16")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M16:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Calibre de 52 cm de Competencia"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Frontal de Agente de Comando"
                                                                    + "\n-Municion Stanag de 60 balas")

def m19(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M19")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M19:\n"
                                                                    + "\n-Cañon XRK V Ampliado"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Sistema de Gatillo Ligero"
                                                                    + "\n-Municion de 32 balas"
                                                                    + "\n-Ventaja Duales"
                                                                    + "\n\nAlternativa: Reemplazar Ventaja Duales por Totalmente Cargado y Laser de 5 mW por Silenciador Monolitico")

def m1912(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M1912")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M1912:\n"
                                                                    + "\n-Silenciador M1929"
                                                                    + "\n-Cañon Chariot de 6.35 cm Rapido"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Ragdoll T2 Support"
                                                                    + "\n-Acople Empuñadura Delantera para Carver"
                                                                    + "\n-Cargador Tambores de 8 mm Kurz con 50 Proyectiles"
                                                                    + "\n-Municion Punta Hueca"
                                                                    + "\n-Empuñadura Trasera de Polimero"
                                                                    + "\n-Ventaja 1 Rapido"
                                                                    + "\n-Ventaja 2 Rapido")

def m1916(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M1916")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M1916:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon ZP 762 mm de Precision"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Fitzherbert Reforzada"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargadores de 6.5 mm Sakura con 20 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def m1garand(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M1Garand")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M1 Garand:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Cooper de 63.5 cm Personalizada"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Cooper Ajustable"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Tambores del Calibre 30-06 con 20 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def m4a1(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M4A1")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M4A1 (Modern Warfare):\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon M16 Granadero de serie"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 60 balas"
                                                                    + "\n\nAlternativa: reemplazar mira x3 VLK por Laser Tactico"
                                                                    + "\n\nPara M4 de ColdWar preguntar por /XM4")

def m60(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M60")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M60:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Calibre 57.9 de Competencia"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Frontal de Operador de Campo"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def m82(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M82")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M82:\n"
                                                                    + "\n-Silenciador Cubierto"
                                                                    + "\n-Cañon Combate de Reconocimiento de 57.4 cm"
                                                                    + "\n-Laser Mira Laser de SWAT 5mW"
                                                                    + "\n-Acople Empuñadura Frontal"
                                                                    + "\n-Municion Cargador Aceler de 7 balas")

def m91(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M91")
    context.bot.send_message(chat_id=update.effective_chat.id, text="M91:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Fuerzas Espaciales M91"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando")

def mac(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MAC")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MAC-10:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 15 cm"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion Tambor Stanag de 53 balas"
                                                                    + "\n-Empuñadura Trasera de Serpiente"
                                                                    + "\n\nAlternativa: reemplazar Empuñadura Trasera por Culata de Alambre y la Municion Stanag por cargador rapido (para disparo de la cadera)")

def magnum(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Magnum")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Magnum:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon 11.9 cm de Cañon Corto Estrecho"
                                                                    + "\n-Laser de Avistamiento Ember"
                                                                    + "\n-Culata Duales"
                                                                    + "\n-Municion Cargador Rapido de 12 balas Stanag")

def marco(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Marco")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Marco 5:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon Perfecto Lesto de 355 mm"
                                                                    + "\n-Mira Reflect Slate"
                                                                    + "\n-Culata Imerito FR"
                                                                    + "\n-Acople Armazon Mk. VI"
                                                                    + "\n-Cargador Nambu con 64 Proyectiles"
                                                                    + "\n-Municion Subsonica"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Arrollador"
                                                                    + "\n-Ventaja 2 Rapido"
                                                                    + "\n\nAlternativa Duales: reemplazar -Cañon Botti de 285 mm Personalizado, -Mira G16 x 2,5, -Culata Botti HF Plegable, -Empuñadura Trasera con Brea de Pino, -Ventaja 1 Duales")

def marshal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Marshal")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Marshal:\n"
                                                                    + "\n-Cañon Recortado de 16.51 cm"
                                                                    + "\n-Culata a dos Manos"
                                                                    + "\n-Municion Cargador Aliento de Dragon")

def mg34(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MG34")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MG34:\n"
                                                                    + "\n-Silenciador Ligero"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion Cinta de 100 balas")

def mg42(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MG42")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MG 42:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon VDD de 890 mm 32M Lufschutz"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata VDD 64M"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargadores Rapidos de 8 mm Klauser con 50 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def mg82(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MG82")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MG 82:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Recortado de 37.34 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion Cargador Acelerado de 125 balas"
                                                                    + "\n\nAlternativa: reemplazar Cañon Recortado por Cañon de Fuerza Operativa para mas alcance pero menos movilidad")

def milano(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Milano")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Milano:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 40.6 cm"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion Tambor Stanag de 50 balas"
                                                                    + "\n-Empuñadura Trasera de Serpiente")

def mk2(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MK2")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MK2 Carabina:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon FSS de 50.8 cm Estandar"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Empuñadura Trasera Adhesivo Engomado")

def modelo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Modelo")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Modelo 680:\n"
                                                                    + "\n-Boca de Cañon Forge TAC Merodeador"
                                                                    + "\n-Cañon XRK Deportivo de 76.2 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata sin Culata"
                                                                    + "\n-Municion de Aliento de Dragon")

def mp40(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP40")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MP-40:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon VDD de 189 Corto"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Krausnick 33M Plegable"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargadores de 7.62 mm Gorenko con 45 Proyectiles"
                                                                    + "\n-Municion Subsonica"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Refuerzo"
                                                                    + "\n-Ventaja 2 Rapido")

def mp5cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP5CW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MP5 (ColdWar):\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Culata Raider"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion Tambor Stanag de 50 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente"
                                                                    + "\n\nAlternativa: reemplazar culata por Cañon Reforzado Pesado de 24.1 cm"
                                                                    + "\n\nPara MP5 de Modern Warfare preguntar por /MP5MW")

def mp5mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP5MW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MP5 (Modern Warfare):\n"
                                                                    + "\n-Cañon Integrado Monolitico"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Culata Plegable FTAC"
                                                                    + "\n-Acople Frontal de Mercenario"
                                                                    + "\n-Municion de 45 balas"
                                                                    + "\n\nPara MP5 de ColdWar preguntar por /MP5CW")

def mp7(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP7")
    context.bot.send_message(chat_id=update.effective_chat.id, text="MP7:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon FSS de Reconocimiento"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 60 balas"
                                                                    + "\n\nAlternativa: reemplazar Cañon por Empuñadura Puntuada para corto")

def nikita(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Nikita")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Nikita AVT:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Empress de 613 mm BFA"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Empress Notch"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargadores de 7.62 x 54 mm R con 50 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Perfeccionista"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def nz41(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por NZ41")
    context.bot.send_message(chat_id=update.effective_chat.id, text="NZ-41:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Orbweaver de 360 mm BC"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Orbweaver E Pack"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargador de 6.5 mm Sakura con 50 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Sombreada"
                                                                    + "\n-Ventaja 1 Refuerzo"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def oden(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Oden")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Oden:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Oden Estandar de 810mm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 30 balas")

def origin(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Origin")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Origin 12:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Forge TAC Precision"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Culata sin Culata"
                                                                    + "\n-Municion de 12 balas")

def ots(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por OTS9")
    context.bot.send_message(chat_id=update.effective_chat.id, text="OTs 9:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 20.57 cm"
                                                                    + "\n-Culata de Armazon KGB"
                                                                    + "\n-Municion Spetsnaz de 40 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def owen(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Owen")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Subfusil Owen:\n"
                                                                    + "\n-Silenciador M1929"
                                                                    + "\n-Cañon Gawain de 188 mm Cubierto"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata LOR Plegable"
                                                                    + "\n-Acople Empuñadura Delantera para Carver"
                                                                    + "\n-Cargador Tambores de 7.62 mm Gorenko con 72 Proyectiles"
                                                                    + "\n-Municion Punta Hueca"
                                                                    + "\n-Empuñadura Trasera de Polimero"
                                                                    + "\n-Ventaja 1 Rapido"
                                                                    + "\n-Ventaja 2 Rapido")

def p1911cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P1911CW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="1911 (ColdWar):\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 16.6 cm"
                                                                    + "\n-Laser Foco de Equipo de Tigre"
                                                                    + "\n-Municion de 12 balas"
                                                                    + "\n-Empuñadura Trasera de Serpiente"
                                                                    + "\n\nAlternativa: Para 1911 de Modern Warfare preguntar por /1911MW Para 1911 de Vanguard preguntar por /1911VG")

def p1911mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P1911MW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="1911 (Modern Warfare):\n"
                                                                    + "\n-Cañon 1911 Acechador"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Sistema de Gatillo Ligero"
                                                                    + "\n-Municion de 15 balas"
                                                                    + "\n-Ventaja Duales"
                                                                    + "\n\nAlternativa: ara 1911 de ColdWar preguntar por /1911CW Para 1911 de Vanguard preguntar por /1911VG")

def p1911vg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P1911VG")
    context.bot.send_message(chat_id=update.effective_chat.id, text="1911 (Vanguard):\n"
                                                                    + "\n-Boca de Cañon Estabilizador F8"
                                                                    + "\n-Cañon Cooper de 16.51 cm"
                                                                    + "\n-Mira G16 x 2.5"
                                                                    + "\n-Sistema del Gatillo Ligero"
                                                                    + "\n-Cargadores de Calibre 45 ACP con 18 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura con Brea de Pino"
                                                                    + "\n-Ventaja 1 Duales"
                                                                    + "\n-Ventaja 2 Totalmente Cargado"
                                                                    + "\n\nAlternativa: Para 1911 de ColdWar preguntar por /1911CW Para 1911 de Modern Warfare preguntar por /1911MW")

def p357(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P357")
    context.bot.send_message(chat_id=update.effective_chat.id, text=".357:\n"
                                                                    + "\n-Cañon Silverfield Ordnance cal. 357"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Sistema de Gatillo Ligero"
                                                                    + "\n-Municion Disparo de Perdigones"
                                                                    + "\n-Ventaja Duales")

def p50gs(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P50GS")
    context.bot.send_message(chat_id=update.effective_chat.id, text=".50 GS:\n"
                                                                    + "\n-Cañon Forge TAC ampliado"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Sistema de Gatillo Ligero"
                                                                    + "\n-Municion de 13 balas"
                                                                    + "\n-Ventaja Duales")

def p90(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P90")
    context.bot.send_message(chat_id=update.effective_chat.id, text="P90:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata Correa Moderna"
                                                                    + "\n-Acople Adhesivo Granulado"
                                                                    + "\n-Empuñadura Trasera Adhesivo Punteado")

def pelington(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Pelington")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pelington:\n"
                                                                    + "\n-Silenciador Cubierto"
                                                                    + "\n-Cañon Combate de Reconocimiento de 69 cm"
                                                                    + "\n-Laser Mira Laser de SWAT 5mW"
                                                                    + "\n-Municion Cargador Acelerado de 7 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def pkm(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PKM")
    context.bot.send_message(chat_id=update.effective_chat.id, text="PKM:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Compacto de 46.2 cm"
                                                                    + "\n-Culata sin Culata"
                                                                    + "\n-Acople Empuñadura Rapida"
                                                                    + "\n-Municion Cinta de 200 balas")

def ppshcw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PPSHCW")
    context.bot.send_message(chat_id=update.effective_chat.id, text="PPSH-41 (Coldwar):\n"
                                                                    + "\n-Silenciador de Sonido"
                                                                    + "\n-Cañon Fuerza Operativa de 39.9 cm"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n-Municion Tambor Spetsnaz de 55 balas"
                                                                    + "\n-Empuñadura Trasera de Serpiente")

def ppshvg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PPSHVG")
    context.bot.send_message(chat_id=update.effective_chat.id, text="PPSH-41 (Vanguard):\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon Kovalevskaya de 230 mm B03P"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Armazon Kovalevskaya"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargadores de 8 mm Nambu con 71 Proyectiles"
                                                                    + "\n-Municion Subsonica"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Rapido")

def qbz(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por QBZ")
    context.bot.send_message(chat_id=update.effective_chat.id, text="QBZ-83:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa 40.6 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura de Agente de Campo"
                                                                    + "\n-Municion Stanag de 60 balas")

def r1(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por R1")
    context.bot.send_message(chat_id=update.effective_chat.id, text="R1 Shadowhunter:\n"
                                                                    + "\n-Fusiles Tacticos"
                                                                    + "\n-Mira LED Microflex"
                                                                    + "\n\nPara Ballesta de Modern Warfare preguntar por /Ballesta")

def r9(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por R9")
    context.bot.send_message(chat_id=update.effective_chat.id, text="R9-0:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Forge TAC Centinela"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Acople Empuñadura Frontal de Mercenario"
                                                                    + "\n-Municion de Aliento de Dragon")

def ra225(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RA225")
    context.bot.send_message(chat_id=update.effective_chat.id, text="RA 225:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon Urban Rapido de 28 cm"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Urbana Tactica"
                                                                    + "\n-Acople Estabilizador para M1915"
                                                                    + "\n-Cargador Tambores de 9 mm con 55 Proyectiles"
                                                                    + "\n-Municion Punta Hueca"
                                                                    + "\n-Empuñadura Trasera de Polimero"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Rapido")

def raal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RAAL")
    context.bot.send_message(chat_id=update.effective_chat.id, text="RAAL:\n"
                                                                    + "\n-Boca de Cañon RAAL de Nucleo Monolitico"
                                                                    + "\n-Cañon RAAL Linea de Ruptura de 81.3 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople FSS oblicuo"
                                                                    + "\n-Municion Cintas de 50 balas")

def ram(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RAM")
    context.bot.send_message(chat_id=update.effective_chat.id, text="RAM-7:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon FSS Ranger"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 50 balas"
                                                                    + "\n\nAlternativa Subfusil: reemplazar cañon por Laser Tactico y mira por Mira Reflex IG Mini")

def ratt(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RATT")
    context.bot.send_message(chat_id=update.effective_chat.id, text="RATT:\n"
                                                                    + "\n-Silenciador M1929"
                                                                    + "\n-Cañon ZAC de 98 mm"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Sistema del Gatillo Accion Rapida"
                                                                    + "\n-Cargadores de 9 mm con 20 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Tela"
                                                                    + "\n-Ventaja 1 Rapido"
                                                                    + "\n-Ventaja 2 Rapido")

def renetti(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Renetti")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Renetti:\n"
                                                                    + "\n-Cañon MK1 Ampliado"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Sistema de Gatillo Ligero"
                                                                    + "\n-Municion de 27 balas"
                                                                    + "\n-Ventaja Duales")

def rpd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RPD")
    context.bot.send_message(chat_id=update.effective_chat.id, text="RPD:\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon Fuerza Operativa de 51.5 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Culata de Armazon KGB"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n\nAlternativa: reemplazar culata por Cargador Acelerado de 120 balas")

def rytec(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Rytec")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Rytec AMR:\n"
                                                                    + "\n-Silenciador de Rytec AMR"
                                                                    + "\n-Cañon FTAC Seven Straight"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Municion Cargador de 25 x 59 mm de termita x5"
                                                                    + "\n-Ventaja Claridad Mental")

def sa87(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SA87")
    context.bot.send_message(chat_id=update.effective_chat.id, text="SA87:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon SA87 de 64.5 cm Estandar"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion Cargador de 60 balas")

def scar(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SCAR")
    context.bot.send_message(chat_id=update.effective_chat.id, text="FN Scar 17:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Forge TAC de 50.8 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 30 balas")

def sks(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SKS")
    context.bot.send_message(chat_id=update.effective_chat.id, text="SKS:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon FSS M59/66 de 55.8 cm"
                                                                    + "\n-Mira x3 VLK"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 30 balas")

def spr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SPR")
    context.bot.send_message(chat_id=update.effective_chat.id, text="SP-R 208 - SP:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon SP-R de 66 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Mira Optica con Zoom Variable"
                                                                    + "\n-Municion Cargadores de Calibre 300 Norma x5"
                                                                    + "\n\nAlternativa: Mira Zoom Variable por Mira de Francotirador")

def sten(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Sten")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sten:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon SA de 65 mm Rapido"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Gawain Personalizada"
                                                                    + "\n-Acople Armazon Mk. VI"
                                                                    + "\n-Cargador Tambores de 9 mm con 50 Proyectiles"
                                                                    + "\n-Municion Subsonica"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Acrobatico"
                                                                    + "\n-Ventaja 2 Rapido")

def stg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por STG")
    context.bot.send_message(chat_id=update.effective_chat.id, text="STG44:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon VDD de 760 mm 05B"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata VDD 34S con Peso"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargador de 7.62 mm Gorenko con 50 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera con Surcos"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def stoner(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Stoner")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stoner 63:\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Lancero de Caballeria de 55.4 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Culata Almohadilla Raider"
                                                                    + "\n-Acople Empuñadura Frontal de Agente de Campo"
                                                                    + "\n\nAlternativa: reemplazar culata por Cargador Acelerado de 120 balas")

def street(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Street")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Streetsweeper:\n"
                                                                    + "\n-Estrangulador Agency"
                                                                    + "\n-Cañon Forjado a Mano de 33.8 cm"
                                                                    + "\n-Laser Mira Laser de SWAT 5mW"
                                                                    + "\n-Culata Marathon"
                                                                    + "\n-Municion Stanag de 18 balas")

def striker(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Striker")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Striker 45:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Acero Inoxidable de 400 mm"
                                                                    + "\n-Culata FSS Guardian"
                                                                    + "\n-Acople Frontal de Comando"
                                                                    + "\n-Municion de 45 balas")

def svt(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SVT")
    context.bot.send_message(chat_id=update.effective_chat.id, text="SVT-40:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon ZAC de 730 mm de Precision"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Kovalevskaya S02 con Peso"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargadores de 7.62 x 54 mm con 20 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Perfeccionista"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def swiss(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Swiss")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Swiss K31:\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon 63.25 cm de Reconocimiento de Combate"
                                                                    + "\n-Laser Mira Laser de SWAT 5mW"
                                                                    + "\n-Municion Cargador Acelerado de 7 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def sykov(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Sykov")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sykov:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon Sorokin Automatica de 140mm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Municion Tambores de 80 balas"
                                                                    + "\n-Ventaja Totalmente Cargado"
                                                                    + "\n\nAlternativa: Reemplazar Ventaja Totalmente Cargado por Empuñadura Trasera VLK Prizrak")

def tec9(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por TEC9")
    context.bot.send_message(chat_id=update.effective_chat.id, text="TEC-9:\n"
                                                                    + "\n-Boca de Cañon Repetidor Automatico"
                                                                    + "\n-Cañon Fuerza Operativa de 12.5 cm"
                                                                    + "\n-Acople Empuñadura de Agente de Campo"
                                                                    + "\n-Municion Stanag de 48 balas"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def topbreak(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Topbreak")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Top Break:\n"
                                                                    + "\n-Silenciador M1929"
                                                                    + "\n-Cañon Wilkie W-4 Stub"
                                                                    + "\n-Mira G16 x 2.5"
                                                                    + "\n-Sistema del Gatillo Sensible"
                                                                    + "\n-Cargador 30 Russian Short"
                                                                    + "\n-Municion Cartucho de Escopeta M15"
                                                                    + "\n-Empuñadura con Brea de Pino"
                                                                    + "\n-Ventaja 1 Duales"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def treslineas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Treslineas")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fusil de Tres Lineas:\n"
                                                                    + "\n-Silenciador Mercury"
                                                                    + "\n-Cañon Empress de 514 mm F01"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Kovalevskaya S01"
                                                                    + "\n-Acople Armazon Mk. VI"
                                                                    + "\n-Cargador de Calibre 30-06 con 20 Proyectiles"
                                                                    + "\n-Municion Alargada"
                                                                    + "\n-Empuñadura Trasera de Cuero"
                                                                    + "\n-Ventaja 1 Velo"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def tundra(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Tundra")
    context.bot.send_message(chat_id=update.effective_chat.id, text="LW3 - Tundra:\n"
                                                                    + "\n-Silenciador Cubierto"
                                                                    + "\n-Cañon Combate de Reconocimiento de 73.9 cm"
                                                                    + "\n-Laser Mira Laser de SWAT 5mW"
                                                                    + "\n-Municion Cargador Acelerado de 7 balas"
                                                                    + "\n-Empuñadura Trasera de Serpiente")

def type100(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type100")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type 100:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon Warubachi de 134 mm Rapido"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Empuñadura Plegable de Warubachi"
                                                                    + "\n-Acople Armazon Mk. VI"
                                                                    + "\n-Cargadores del Calibre .30 Russian Corto con 36 Proyectiles"
                                                                    + "\n-Municion Subsonica"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Rapido")

def type11(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type11")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type 11:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Warubachi Tipo 33"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargador Tambores de 6.5 mm Sakura con 90 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Refuerzo"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def type63(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type63")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type 63:\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon Titanio de 41.7 cm"
                                                                    + "\n-Mira Axial Arms x3"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n-Municion Cargador Baquelita de 40 balas")

def type99(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type99")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type 99:\n"
                                                                    + "\n-Silenciador Mercury"
                                                                    + "\n-Cañon Shiraishi de 712 mm de Francotirador"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Sakura CVR Personalizada"
                                                                    + "\n-Acople Empuñadura Delantera Pesada"
                                                                    + "\n-Cargadores de 8 mm Klauser con 5 Proyectiles"
                                                                    + "\n-Municion Alargada"
                                                                    + "\n-Empuñadura Trasera de Cuero"
                                                                    + "\n-Ventaja 1 Observador"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def ugm8(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por UGM8")
    context.bot.send_message(chat_id=update.effective_chat.id, text="UGM-8:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Bernard XL214 de 736 mm"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Mercier WT Ancre"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargador Caja de Calibre 6.5 mm Sakura con 125 Proyectiles"
                                                                    + "\n-Municion Alargada"
                                                                    + "\n-Empuñadura Trasera Sombreada"
                                                                    + "\n-Ventaja 1 Empuñadura Segura"
                                                                    + "\n-Ventaja 2 Totalmente Cargado"
                                                                    + "\n\nAlternativa: reemplazar cañon por Romuald de 560 mm DA")

def ugr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por UGR")
    context.bot.send_message(chat_id=update.effective_chat.id, text="UGR:\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon Fuerza Operativa de 27.2 cm"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n-Cargador Dardos Explosivos"
                                                                    + "\n-Empuñadura Trasera Vendaje de Serpiente")

def uzi(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Uzi")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Uzi:\n"
                                                                    + "\n-Silenciador Monolitico"
                                                                    + "\n-Cañon FSS de Carabina Pro"
                                                                    + "\n-Culata Sin Culata"
                                                                    + "\n-Acople Frontal de Mercenario"
                                                                    + "\n-Municion de 50 balas")

def vargo52(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Vargo52")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Vargo 52:\n"
                                                                    + "\n-Silenciador GRU"
                                                                    + "\n-Cañon 47.2 cm de Fuerza Operativa"
                                                                    + "\n-Mira Axial x3"
                                                                    + "\n-Acople Empuñadura Spetsnaz"
                                                                    + "\n-Municion Spetsnaz de 60 Balas")

def vargos(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Vargos")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Vargo-S:\n"
                                                                    + "\n-Silenciador Mx"
                                                                    + "\n-Cañon Mirzoyan de 414 mm Personalizado"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Mirzoyan ANC"
                                                                    + "\n-Acople M1930 Guerrillero en Angulo"
                                                                    + "\n-Cargador Tambores de 7.62 x 54 mm R con 60 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera Sombreada"
                                                                    + "\n-Ventaja 1 Vital"
                                                                    + "\n-Ventaja 2 Totalmente Cargado"
                                                                    + "\n\nPara Vargo de Coldwar /Vargo52")

def vlk(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por VLK")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Rogue VLK:\n"
                                                                    + "\n-Boca de Cañon Forge TAC Merodeador"
                                                                    + "\n-Cañon Señor de la Guerra de 40.6 cm"
                                                                    + "\n-Laser Tactico"
                                                                    + "\n-Culata sin Culata"
                                                                    + "\n-Municion Aliento de Dragon de 8 Cartuchos")

def volks(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Volks")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Volkssturmgewehr:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Krausnick de 428 mm 05V"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata Krausnick S12V PS"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargadores de Calibre 30 Russian Short con 45 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Rapido"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def welgun(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Welgun")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welgun:\n"
                                                                    + "\n-Amplificador de Retroceso"
                                                                    + "\n-Cañon Gawain de 120 mm Corto"
                                                                    + "\n-Mira Reflector Slate"
                                                                    + "\n-Culata Eliminada"
                                                                    + "\n-Acople Armazon Mk. VI"
                                                                    + "\n-Cargadores 7.62 Gorenko con 40 Proyectiles"
                                                                    + "\n-Municion Subsonica"
                                                                    + "\n-Empuñadura Trasera con Cinta"
                                                                    + "\n-Ventaja 1 Acrobatico"
                                                                    + "\n-Ventaja 2 Rapido")

def whitley(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Whitley")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Whitley:\n"
                                                                    + "\n-Silenciador MX"
                                                                    + "\n-Cañon Ragdoll RE2 de 50.8 cm"
                                                                    + "\n-Mira PU para SVT-40 (x3-6)"
                                                                    + "\n-Culata CGC R4"
                                                                    + "\n-Acople Tope de Mano para el M1941"
                                                                    + "\n-Cargador Calibre 30-06 con 120 Proyectiles"
                                                                    + "\n-Municion Incendiaria"
                                                                    + "\n-Empuñadura Trasera de Goma"
                                                                    + "\n-Ventaja 1 Incansable"
                                                                    + "\n-Ventaja 2 Totalmente Cargado")

def x16(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por X16")
    context.bot.send_message(chat_id=update.effective_chat.id, text="X16:\n"
                                                                    + "\n-Cañon Singuard Arms Ventaja"
                                                                    + "\n-Laser de 5 mW"
                                                                    + "\n-Sistema de Gatillo Ligero"
                                                                    + "\n-Municion de 26 balas"
                                                                    + "\n-Ventaja Duales")

def xm4(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por XM4")
    context.bot.send_message(chat_id=update.effective_chat.id, text="XM4 (ColdWar):\n"
                                                                    + "\n-Silenciador Agency"
                                                                    + "\n-Cañon Fuerza Operativa de 34.3 cm"
                                                                    + "\n-Mira Axial x3"
                                                                    + "\n-Acople Empuñadura de Operador de Campo"
                                                                    + "\n-Municion Stanag de 60 balas"
                                                                    + "\n\nAlternativa Subfusil: reemplazar Silenciador Agency por Silenciador, mira por Mira LED Microflex o por Culata Almohadilla Raider y Municion de 45 balas"
                                                                    + "\n\nPara M4 de Modern Warfare preguntar por /M4A1")

def zrg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por ZRG")
    context.bot.send_message(chat_id=update.effective_chat.id, text="ZRG 20 mm:\n"
                                                                    + "\n-Silenciador Cubierto"
                                                                    + "\n-Cañon Combate de Reconocimiento de 111.5 cm"
                                                                    + "\n-Laser Mira Laser de SWAT 5mW"
                                                                    + "\n-Cargador 5 Proyectiles"
                                                                    + "\n-Empuñadura Trasera de la Jungla SASR")
"""
