from resources.api.codapi import hormigator_friends
from resources.commands.commandsMenu import defineLogs


# BONUS
def alla(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por alla")
    update.message.reply_text("Ella")


def api(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Api")
    update.message.reply_text("Aplicacion para las armas:\n\nhttps://apiguarson.herokuapp.com/")


def botrapido(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por botrapido")
    update.message.reply_text("Tranquilo a mi no me apures que no soy tu sirviente, pelotudo")


def botconchatumadre(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por botconchatumadre")
    update.message.reply_text("Que te pasa boludo?")


def codsignal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por COD")
    update.message.bot.send_photo(update.message.chat.id, photo='https://drive.google.com/file/d/1EZYtZdUJqdGddTEX_H7SdrrgMpimgZ8j/view?usp=sharing', caption="Vamo a juga?")


def conectados(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Conectados")
    update.message.reply_text(hormigator_friends())


# Documentacion https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot
def fortnite(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Fortnite")
    update.message.bot.send_animation(update.message.chat.id, animation='https://c.tenor.com/4gPD1ccxrVgAAAAC/rick-ashley-dance.gif', caption="Sale ese Fortnite?")


def guarson(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Guarson")
    update.message.reply_text("Mas vale que si pa")


def manco(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Manco")
    update.message.reply_text("No le digan asi, se llama mandalorian")


def mancolorian(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mancolorian")
    update.message.reply_text("Alla va, rusheando solo")


def quaqua(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Quaqua")
    update.message.reply_text("El buen socio vitalicio de FonoGay, si llamas al 515-3232 seguro lo encontras")
