from resources.api.codapi import getLobbyTotalInfo
from resources.commands.commandsMenu import defineLogs


# Streamers
def aydan(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Aydan")
    update.message.reply_text("Armas de Aydan:\n\nhttps://docs.google.com/spreadsheets/u/0/d/1uAU48i0XY0n_bwLaNLE5yJEBN_qn9ufb9b7oYX6ZNFE/htmlview")


def mutex(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mutex")
    update.message.reply_text("Armas de Mutex:\n\nhttps://docs.google.com/spreadsheets/u/0/d/1noCHj28dM6GArYcaGyN5DcJmVtwireoBRlBP7E4UTUo/htmlview")


def lobbyAmir(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Amir")
    update.message.reply_text(getLobbyTotalInfo("battle", "deusamir%231557"))


def lobbyAydan(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Aydan")
    update.message.reply_text(getLobbyTotalInfo("battle", "aydan%2311691"))


def lobbyFlexz(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Flexz")
    update.message.reply_text(getLobbyTotalInfo("battle", "flexz%232541"))


def lobbyIron(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Flexz")
    update.message.reply_text(getLobbyTotalInfo("battle", "Iron%2311745"))


def lobbyMirrey(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Mirrey")
    update.message.reply_text(getLobbyTotalInfo("battle", "xmirrey%231293"))


def lobbySoki(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Soki")
    update.message.reply_text(getLobbyTotalInfo("battle", "soki%2321161"))


def lobbyTaison(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Taison")
    update.message.reply_text(getLobbyTotalInfo("battle", "TaisonTV%232260"))
