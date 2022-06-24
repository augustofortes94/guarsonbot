from telegram import *
from resources.api.codapi import *
from resources.commands.commandsMenu import defineLogs

#####   Lobbys  #####
def lobbyBolsonaro(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Bolsonaro")
    update.message.reply_text(getLobbyTotalInfo("psn", "agu_q1988"))

def lobbyElch000(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Elch000")
    update.message.reply_text(getLobbyTotalInfo("psn", "Elch000"))

def lobbyHormigator(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Hormigator")
    update.message.reply_text(getLobbyTotalInfo("psn", "Hormigator1"))

def lobbyLeko(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Leko")
    update.message.reply_text(getLobbyTotalInfo("psn", "Aleko22lp"))

def lobbyLuquitas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Luquitas")
    update.message.reply_text(getLobbyTotalInfo("psn", "luquitasc70"))

def lobbyMandalorian(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Mandalorian")
    update.message.reply_text(getLobbyTotalInfo("battle", "Mandalorian%2311726"))

def lobbyPablo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Pablo")
    update.message.reply_text(getLobbyTotalInfo("psn", "carripablin10"))

def lobbyRapax(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Rapax7")
    update.message.reply_text(getLobbyTotalInfo("battle", "rapax7%231438"))

def matchmaking(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Matchmaking")
    update.message.reply_text("Explicacion del Matchmaking SBMM y EOMM:\n\nhttps://www.reddit.com/r/CODWarzone/comments/m16nl2/debunking_the_myths_testing_sbmm_and_eomm_in/")

def tableColour(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Colour Table")
    update.message.reply_text(lobbyColourTable())
