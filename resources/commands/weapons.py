from resources.commands.commandsMenu import defineLogs
from ..api.guarsonapi import getWeaponFromApi


def weaponRegex(update, context):
    mssg = getWeaponFromApi(update['message']['text'][1:])
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por " + update['message']['text'][1:])
    update.message.reply_text(mssg)


# ARMAS
def ak47(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK-47")
    update.message.reply_text("AK-47:\n\n-Para AK-47 de ColdWar /AK47CW\n-Para AK-47 de Modern Warfare /AK47MW")


def ak47cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK-47 CW")
    update.message.reply_text(getWeaponFromApi('AK47CW'))


def ak47mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK-47 MW")
    update.message.reply_text(getWeaponFromApi('AK47MW'))


def ak74u(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AK-74u")
    update.message.reply_text(getWeaponFromApi('AK74U'))


def ametralladora(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Pistola Ametralladora")
    update.message.reply_text(getWeaponFromApi('Ametralladora'))


def amp(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AMP 63")
    update.message.reply_text(getWeaponFromApi('AMP'))


def an94(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AN94")
    update.message.reply_text(getWeaponFromApi('AN94'))


def antitanque(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Fusil Antitanque Gorer")
    update.message.reply_text(getWeaponFromApi('Antitanque'))


def armaguerra(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Armaguerra 43")
    update.message.reply_text(getWeaponFromApi('Armaguerra'))


def as44(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AS44")
    update.message.reply_text(getWeaponFromApi('AS44'))


def asval(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AS-VAL")
    update.message.reply_text(getWeaponFromApi('ASVAL'))


def aug(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AUG")
    update.message.reply_text("AUG:\n\n-Para AUG de ColdWar /AUGCW\n-Para AUG de Modern Warfare /AUGMW")


def augcw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AUG CW")
    update.message.reply_text(getWeaponFromApi('AUGCW'))


def augmw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AUG MW")
    update.message.reply_text(getWeaponFromApi('AUGMW'))


def automata(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Automata")
    update.message.reply_text(getWeaponFromApi('Automata'))


def ax50(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por AX-50")
    update.message.reply_text(getWeaponFromApi('AX50'))


def ballesta(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Ballesta")
    update.message.reply_text(getWeaponFromApi('Ballesta'))


def bar(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por BAR")
    update.message.reply_text(getWeaponFromApi('BAR'))


def bizon(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bizon")
    update.message.reply_text(getWeaponFromApi('Bizon'))


def blixen(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por H4 Blixen")
    update.message.reply_text(getWeaponFromApi('Blixen'))


def bren(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bren")
    update.message.reply_text(getWeaponFromApi('Bren'))


def bruen(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bruen MK9")
    update.message.reply_text(getWeaponFromApi('Bruen'))


def bullfrog(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bullfrog")
    update.message.reply_text(getWeaponFromApi('Bullfrog'))


def c58(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por C58")
    update.message.reply_text(getWeaponFromApi('C58'))


def carv2(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Carv.2")
    update.message.reply_text(getWeaponFromApi('Carv2'))


def combate(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Escopeta de Combate")
    update.message.reply_text(getWeaponFromApi('Combate'))


def cooper(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Carabina Cooper")
    update.message.reply_text(getWeaponFromApi('Cooper'))


def cr56(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por CR-56")
    update.message.reply_text(getWeaponFromApi('CR56'))


def cx9(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por CX-9")
    update.message.reply_text(getWeaponFromApi('CX9'))


def diamatti(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Diamatti")
    update.message.reply_text(getWeaponFromApi('Diamatti'))


def dmr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por DMR")
    update.message.reply_text(getWeaponFromApi('DMR'))


def doble(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Doble Cañon")
    update.message.reply_text(getWeaponFromApi('Doble'))


def dp27(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por DP27")
    update.message.reply_text(getWeaponFromApi('DP27'))


def dragunov(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Dragunov")
    update.message.reply_text(getWeaponFromApi('Dragunov'))


def e725(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por E725")
    update.message.reply_text(getWeaponFromApi('E725'))


def ebr14(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por EBR-14")
    update.message.reply_text(getWeaponFromApi('EBR14'))


def einhorn(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Einhorn Rotativa")
    update.message.reply_text(getWeaponFromApi('Einhorn'))


def em2(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por EM2")
    update.message.reply_text(getWeaponFromApi('EM2'))


def fal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FAL")
    update.message.reply_text(getWeaponFromApi('FAL'))


def famas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FAMAS")
    update.message.reply_text("FAMAS:\n\n-Para FAMAS de ColdWar /FFAR\n-Para FAMAS de Modern Warfare /FR556")


def fara(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FARA 83")
    update.message.reply_text(getWeaponFromApi('FARA'))


def fennec(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Fennec")
    update.message.reply_text(getWeaponFromApi('Fennec'))


def ffar(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FFAR1")
    update.message.reply_text(getWeaponFromApi('FFAR'))


def finn(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FINN LMG")
    update.message.reply_text(getWeaponFromApi('FINN'))


def fr556(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por FR 5.56")
    update.message.reply_text(getWeaponFromApi('FR556'))


def g43(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por G-43")
    update.message.reply_text(getWeaponFromApi('G43'))


def gallo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Gallo")
    update.message.reply_text(getWeaponFromApi('Gallo'))


def gracey(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Gracey Automatica")
    update.message.reply_text(getWeaponFromApi('Gracey'))


def grau(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Grau")
    update.message.reply_text(getWeaponFromApi('Grau'))


def grav(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Grav")
    update.message.reply_text(getWeaponFromApi('Grav'))


def groza(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Groza")
    update.message.reply_text(getWeaponFromApi('Groza'))


def hauer(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hauer 77")
    update.message.reply_text(getWeaponFromApi('Hauer'))


def hdr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por HDR")
    update.message.reply_text(getWeaponFromApi('HDR'))


def holger(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Holger-26")
    update.message.reply_text(getWeaponFromApi('Holger'))


def ironhide(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por .410 Ironhide")
    update.message.reply_text(getWeaponFromApi('Ironhide'))


def iso(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por ISO")
    update.message.reply_text(getWeaponFromApi('ISO'))


def itra(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por ITRA")
    update.message.reply_text(getWeaponFromApi('ITRA'))


def jak12(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por JAK12")
    update.message.reply_text(getWeaponFromApi('JAK12'))


def kar98(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kar98")
    update.message.reply_text("Kar98k:\n\n-Para Kar98k de Modern Warfare /Kar98MW\n-Para Kar98k de Vanguard /Kar98VG")


def kar98mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kar98k MW")
    update.message.reply_text(getWeaponFromApi('Kar98MW'))


def kar98vg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kar98k Vanguard")
    update.message.reply_text(getWeaponFromApi('Kar98VG'))


def kgm40(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por KG M40")
    update.message.reply_text(getWeaponFromApi('KGM40'))


def kilo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kilo")
    update.message.reply_text(getWeaponFromApi('Kilo'))


def krig(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Krig 6")
    update.message.reply_text(getWeaponFromApi('Krig'))


def klauser(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Klauser")
    update.message.reply_text(getWeaponFromApi('Klauser'))


def ksp(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por KSP 45")
    update.message.reply_text(getWeaponFromApi('KSP'))


def lapa(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por LAPA")
    update.message.reply_text(getWeaponFromApi('LAPA'))


def lc10(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por LC-10")
    update.message.reply_text(getWeaponFromApi('LC10'))


def m1(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M1 Garand")
    update.message.reply_text(getWeaponFromApi('M1Garand'))


def m13(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M13")
    update.message.reply_text(getWeaponFromApi('M13'))


def m16(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M16")
    update.message.reply_text(getWeaponFromApi('M16'))


def m19(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M19")
    update.message.reply_text(getWeaponFromApi('M19'))


def m1912(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M1912")
    update.message.reply_text(getWeaponFromApi('M1912'))


def m1916(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M1916")
    update.message.reply_text(getWeaponFromApi('M1916'))


def m4(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M4")
    update.message.reply_text("M4:\n\n-Para M4 de ColdWar /XM4\n-Para M4 de Modern Warfare /M4A1")


def m4a1(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M4A1")
    update.message.reply_text(getWeaponFromApi('M4A1'))


def m60(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M60")
    update.message.reply_text(getWeaponFromApi('M60'))


def m82(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M82")
    update.message.reply_text(getWeaponFromApi('M82'))


def m91(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por M91")
    update.message.reply_text(getWeaponFromApi('M91'))


def mac(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MAC-10")
    update.message.reply_text(getWeaponFromApi('MAC'))


def magnum(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Magnum")
    update.message.reply_text(getWeaponFromApi('Magnum'))


def marco(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Marco 5")
    update.message.reply_text(getWeaponFromApi('Marco'))


def marshal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Marshal")
    update.message.reply_text(getWeaponFromApi('Marshal'))


def mg34(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MG34")
    update.message.reply_text(getWeaponFromApi('MG34'))


def mg42(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MG 42")
    update.message.reply_text(getWeaponFromApi('MG42'))


def mg82(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MG 82")
    update.message.reply_text(getWeaponFromApi('MG82'))


def milano(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Milano")
    update.message.reply_text(getWeaponFromApi('Milano'))


def mk2(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MK2 Carabina")
    update.message.reply_text(getWeaponFromApi('MK2'))


def modelo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Modelo 680")
    update.message.reply_text(getWeaponFromApi('Modelo'))


def mp40(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP-40")
    update.message.reply_text(getWeaponFromApi('MP40'))


def mp5(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP5")
    update.message.reply_text("MP5:\n\n-Para MP5 de ColdWar /MP5CW\n-Para MP5 de Modern Warfare /MP5MW")


def mp5cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP5 CW")
    update.message.reply_text(getWeaponFromApi('MP5CW'))


def mp5mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP5 MW")
    update.message.reply_text(getWeaponFromApi('MP5MW'))


def mp7(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por MP7")
    update.message.reply_text(getWeaponFromApi('MP7'))


def nikita(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Nikita AVT")
    update.message.reply_text(getWeaponFromApi('Nikita'))


def nz41(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por NZ-41")
    update.message.reply_text(getWeaponFromApi('NZ41'))


def oden(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Oden")
    update.message.reply_text(getWeaponFromApi('Oden'))


def origin(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Origin")
    update.message.reply_text(getWeaponFromApi('Origin'))


def ots9(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por OTs 9")
    update.message.reply_text(getWeaponFromApi('OTS9'))


def owen(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Subfusil Owen")
    update.message.reply_text(getWeaponFromApi('Owen'))


def p1911(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por 1911")
    update.message.reply_text("1911:\n\n-Para 1911 de ColdWar /1911CW\n-Para 1911 de Modern Warfare /1911MW\n-Para 1911 de Vanguard /1911VG")


def p1911cw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por 1911 CW")
    update.message.reply_text(getWeaponFromApi('1911CW'))


def p1911mw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por 1911 MW")
    update.message.reply_text(getWeaponFromApi('1911MW'))


def p1911vg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por 1911 VG")
    update.message.reply_text(getWeaponFromApi('1911VG'))


def p357(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por .357")
    update.message.reply_text(getWeaponFromApi('P357'))


def p50gs(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por .50 GS")
    update.message.reply_text(getWeaponFromApi('50GS'))


def p90(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por P90")
    update.message.reply_text(getWeaponFromApi('P90'))


def pelington(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Pelington")
    update.message.reply_text(getWeaponFromApi('Pelington'))


def pkm(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PKM")
    update.message.reply_text(getWeaponFromApi('PKM'))


def ppsh(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PPSH")
    update.message.reply_text("PPSH-41:\n\n-Para PPSH-41 de ColdWar /PPSHCW\n-Para PPSH-41 de Vanguard /PPSHVG")


def ppshcw(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PPSH-41 CW")
    update.message.reply_text(getWeaponFromApi('PPSHCW'))


def ppshvg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por PPSH-41 VG")
    update.message.reply_text(getWeaponFromApi('PPSHVG'))


def qbz(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por QBZ-83")
    update.message.reply_text(getWeaponFromApi('QBZ'))


def r1shadowhunter(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por R1 Shadowhunter")
    update.message.reply_text(getWeaponFromApi('R1'))


def r9(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por R9")
    update.message.reply_text(getWeaponFromApi('R9'))


def raal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RAAL")
    update.message.reply_text(getWeaponFromApi('RAAL'))


def ram(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RAM-7")
    update.message.reply_text(getWeaponFromApi('RAM'))


def ratt(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RATT")
    update.message.reply_text(getWeaponFromApi('RATT'))


def renetti(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Renetti")
    update.message.reply_text(getWeaponFromApi('Renetti'))


def rpd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por RPD")
    update.message.reply_text(getWeaponFromApi('RPD'))


def rytec(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Rytec")
    update.message.reply_text(getWeaponFromApi('Rytec'))


def sa87(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SA87")
    update.message.reply_text(getWeaponFromApi('SA87'))


def scar(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Scar-H")
    update.message.reply_text(getWeaponFromApi('SCAR'))


def sks(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SKS")
    update.message.reply_text(getWeaponFromApi('SKS'))


def spr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SP-R")
    update.message.reply_text(getWeaponFromApi('SPR'))


def sten(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Sten")
    update.message.reply_text(getWeaponFromApi('Sten'))


def stg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por STG44")
    update.message.reply_text(getWeaponFromApi('STG'))


def stoner(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Stoner 63")
    update.message.reply_text(getWeaponFromApi('Stoner'))


def streetsweeper(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Streetsweeper")
    update.message.reply_text(getWeaponFromApi('Street'))


def striker(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Striker 45")
    update.message.reply_text(getWeaponFromApi('Striker'))


def svt(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por SVT-40")
    update.message.reply_text(getWeaponFromApi('SVT'))


def swiss(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Swiss K31")
    update.message.reply_text(getWeaponFromApi('Swiss'))


def sykov(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Sykov")
    update.message.reply_text(getWeaponFromApi('Sykov'))


def tec9(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por TEC-9")
    update.message.reply_text(getWeaponFromApi('TEC9'))


def topbreak(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Top Break")
    update.message.reply_text(getWeaponFromApi('Topbreak'))


def treslineas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Fusil de Tres Lineas")
    update.message.reply_text(getWeaponFromApi('Treslineas'))


def tundra(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por LW3 - Tundra")
    update.message.reply_text(getWeaponFromApi('Tundra'))


def type(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type")
    update.message.reply_text("Type:\n\n-Para Type 11 de Vanguard /type11\n-Para Type 63 de ColdWar /type63\n-Para Type 99 de Vanguard /type99\n-Para Type 100 de Vanguard /type100")


def type100(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type 100")
    update.message.reply_text(getWeaponFromApi('Type100'))


def type11(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type 11")
    update.message.reply_text(getWeaponFromApi('Type11'))


def type63(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type 63")
    update.message.reply_text(getWeaponFromApi('Type63'))


def type99(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Type 99")
    update.message.reply_text(getWeaponFromApi('Type99'))


def ugm8(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por UGM-8")
    update.message.reply_text(getWeaponFromApi('UGM8'))


def ugr(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por UGR")
    update.message.reply_text(getWeaponFromApi('UGR'))


def uzi(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Uzi")
    update.message.reply_text(getWeaponFromApi('Uzi'))


def vargo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Vargo 52")
    update.message.reply_text(getWeaponFromApi('Vargo'))


def vlk(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Rogue VLK")
    update.message.reply_text(getWeaponFromApi('VLK'))


def volks(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Volkssturmgewehr")
    update.message.reply_text(getWeaponFromApi('Volks'))


def welgun(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Welgun")
    update.message.reply_text(getWeaponFromApi('Welgun'))


def whitley(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Whitley")
    update.message.reply_text(getWeaponFromApi('Whitley'))


def x16(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por X16")
    update.message.reply_text(getWeaponFromApi('X16'))


def xm4(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por XM4")
    update.message.reply_text(getWeaponFromApi('XM4'))


def zrg(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por ZRG 20 mm")
    update.message.reply_text(getWeaponFromApi('ZRG'))
