from resources.api.codapi import info_Player, info_Player_kd
from resources.commands.commandsMenu import defineLogs


# Stats
def bolsonaro(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bolsonaro")
    update.message.reply_text(info_Player("psn", "agu_q1988", "El Peluca Milei"))


def bolsonarokd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bolsonaro KD")
    update.message.reply_text(info_Player_kd("psn", "agu_q1988", "El Peluca Milei"))


def elch000(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Elch000")
    update.message.reply_text(info_Player("psn", "Elch000", "Berisso1"))


def elch000kd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Elch000 KD")
    update.message.reply_text(info_Player_kd("psn", "Elch000", "Berisso1"))


def hormigator(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hormigator")
    update.message.reply_text(info_Player("psn", "Hormigator1", "Hormigator"))


def hormigatorkd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hormigator KD")
    update.message.reply_text(info_Player_kd("psn", "Hormigator1", "Hormigator"))


def leko(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Leko")
    update.message.reply_text(info_Player("psn", "Aleko22lp", "Leko"))


def lekokd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Leko KD")
    update.message.reply_text(info_Player_kd("psn", "Aleko22lp", "Leko"))


def luquitas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Luquitas")
    update.message.reply_text(info_Player("psn", "luquitasc70", "LuquitasC70"))


def luquitaskd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Luquitas KD")
    update.message.reply_text(info_Player_kd("psn", "luquitasc70", "LuquitasC70"))


def mandalorian(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mandalorian")
    update.message.reply_text(info_Player("battle", "Mandalorian%2311726", "MandaloriaN"))


def mandaloriankd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mandalorian KD")
    update.message.reply_text(info_Player_kd("battle", "Mandalorian%2311726", "ElFisgonMorboson"))


def pablo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Pablo")
    update.message.reply_text(info_Player("psn", "carripablin10", "Carripablin10"))


def pablokd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Pablo KD")
    update.message.reply_text(info_Player_kd("psn", "carripablin10", "Carripablin10"))


def rapax(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Rapax7")
    update.message.reply_text(info_Player("battle", "rapax7%231438", "Rapax7"))


def rapaxkd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Rapax7 KD")
    update.message.reply_text(info_Player_kd("battle", "rapax7%231438", "Rapax7"))
