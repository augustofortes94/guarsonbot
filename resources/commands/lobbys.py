from resources.api.filters import lobbyColourTable
from resources.commands.commandsMenu import defineLogs


# Lobbys
def tableColour(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Colour Table")
    update.message.reply_text(lobbyColourTable())
