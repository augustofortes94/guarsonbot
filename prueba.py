import datetime
import time
import requests
from operator import itemgetter
from collections import OrderedDict



def filterKD(kd):       ####Si el kd del jugador es por ejemplo 1.7 le agrego un 0 al final
    if len(kd) == 3:    
        return kd + "0"
    else:
        return kd

def filterKills(kills):     ##Si hace menos de 10 kills sumo un espacio para que quede el texto parejo
    if len(kills) == 1:
        return "| " + kills + "    "
    else:
        return "|" + kills + "   "

def filterLobbyMode(mode):     ##Filtro el modo del juego

    # BR
    if mode == 'br_brquads':
        return "BR CUARTETOS\n"

    elif mode == 'br_brtrios':
        return "BR TRIOS\n"

    elif mode == 'br_brduos':
        return "BR DUOS\n"

    elif mode == 'br_brsolo':
        return "BR SOLOS\n"

    # ISLA RENACIMIENTO
    elif mode == 'br_rebirth_rbrthquad':
        return "ISLA RENACIMIENTO CUARTETOS\n"

    elif mode == 'br_rebirth_rbrthtrios':
        return "ISLA RENACIMIENTO TRIOS\n"

    elif mode == 'br_rebirth_rbrthduos':
        return "ISLA RENACIMIENTO DUOS\n"

    elif mode == 'rbrthsolos':
        return "ISLA RENACIMIENTO SOLOS\n"

    elif mode == 'br_rebirth_rebirth_rex':
        return "ISLA RENACIMIENTO CUARTETOS EXTREMO\n"

    elif mode == 'br_mini_rebirth_mini_royale_trios':
        return "ISLA RENACIMIENTO MINI\n"

    # ISLA FORTUNES KEEP
    elif 'fortkeep_res_trios' in mode:
        return "FORTUNES KEEP TRIOS\n"

    # PLUNDER
    elif mode == 'br_dmz_plunquad':
        return "PLUNDER CUARTETOS\n"

    elif mode == 'br_dmz_plndtrios':
        return "PLUNDER TRIOS\n"

    elif mode == 'br_dmz_plnduo':
        return "PLUNDER DUOS\n"

    elif mode == 'br_dmz_plnbld':
        return "PLUNDER DINERO SUCIO\n"
    
    elif mode == 'br_dmz_vg_pln_trios':
        return "VANGUARD PLUNDER TRIOS\n"

    # IRON TRIALS
    elif mode == 'br_dbd_dbd':
        return "IRON TRIALS '84\n"

    elif mode == 'br_dbd_iron_trials_duos':
        return "IRON TRIALS '84 DUOS\n"

    elif mode == 'rbrthdbd_duos':
        return "REBIRTH IRON TRIALS DUOS\n"

    # VANGUARD ROYALE
    elif mode == 'br_vg_royale_quads':
        return "VANGUARD ROYALE CUARTETOS\n"

    elif mode == 'br_vg_royale_trios':
        return "VANGUARD ROYALE TRIOS\n"

    elif mode == 'br_vg_royale_duos':
        return "VANGUARD ROYALE DUOS\n"

    elif mode == 'br_vg_royale_solo':
        return "VANGUARD ROYALE SOLOS\n"
    
    # BR TRAER DE VUELTA
    elif mode == 'br_buy_back_quads':
        return "BR TRAER DE VUELTA CUARTETOS\n"
    
    elif mode == 'br_buy_back_trios':
        return "BR TRAER DE VUELTA TRIOS\n"

    elif mode == 'br_buy_back_duos':
        return "BR TRAER DE VUELTA DUOS\n"

    elif mode == 'br_buy_back_solo':
        return "BR TRAER DE VUELTA SOLOS\n"

    # OTROS
    elif mode == 'br_rebirth_resurgence_mini':
        return "VERDANSK RESURGIMIENTO MINI\n"

    elif mode == 'br_rebirth_vg_res_44':
        return "VANGUARD RESURGIMIENTO CUARTETOS\n"

    elif mode == 'br_kingslayer_kingsltrios':
        return "MATARREYES\n"

    elif mode == 'br_bodycount_pwergrb':
        return "PODERIO\n"

    elif mode == 'br_payload_payload':
        return "CARGA EXPLOSIVA\n"

    elif mode == 'br_rumble_clash_caldera':
        return "COMBATE\n"

    elif mode == 'br_rebirth_shsnp_name3':
        return "MIRAS Y ESCOPETAS RENACIMIENTO\n"
    
    elif mode == 'br_gxp_gov':
        return "FANTASMAS DE VERDANSK\n"

    elif mode == 'br_vov_op_flash':
        return "OPERACION: FLASHBACK\n"

    elif mode == 'br_lep_br_lep_event/ltm_gamemode':
        return "ULTIMAS HORAS DE VERDANSK\n"

    else:
        return "MODO DESCONOCIDO\n" + mode + "\n"

def filterPosition(pos):        ##Si es el que gano, lo marco como 1°
    if pos == 1:
            return "    1°\n"
    else:
        return "\n"

def lobbyColour(kdProm):    ##Segun el kd indico el color de la lobby
    if kdProm >= 1.14:
        return "Diamante 1"

    elif kdProm >= 1.113 and kdProm < 1.14:
        return "Diamante 2"

    elif kdProm >= 1.095 and kdProm < 1.113:
        return "Diamante 3"

    elif kdProm >= 1.078 and kdProm < 1.095:
        return "Diamante 4"

    elif kdProm >= 1.06 and kdProm < 1.078:
        return "Platino 1"

    elif kdProm >= 1.04 and kdProm < 1.06:
        return "Platino 2"

    elif kdProm >= 1.012 and kdProm < 1.04:
        return "Platino 3"

    elif kdProm >= 0.974 and kdProm < 1.012:
        return "Platino 4"

    elif kdProm >= 0.936 and kdProm < 0.974:
        return "Oro 1"

    elif kdProm >= 0.907 and kdProm < 0.936:
        return "Oro 2"

    elif kdProm >= 0.884 and kdProm < 0.907:
        return "Oro 3"

    elif kdProm >= 0.865 and kdProm < 0.884:
        return "Oro 4"

    elif kdProm >= 0.845 and kdProm < 0.865:
        return "Plata 1"

    elif kdProm >= 0.822 and kdProm < 0.845:
        return "Plata 2"

    elif kdProm >= 0.792 and kdProm < 0.822:
        return "Plata 3"

    elif kdProm >= 0.743 and kdProm < 0.792:
        return "Plata 4"

    elif kdProm >= 0.671 and kdProm < 0.743:
        return "Bronce 1"

    elif kdProm >= 0.619 and kdProm < 0.671:
        return "Bronce 2"

    elif kdProm >= 0.578 and kdProm < 0.619:
        return "Bronce 3"

    elif kdProm < 0.578:
        return "Bronce 4"
    
    else:
        return "ERROR"

def lobbyColourTable():     ##Indico los kd y porcentajes de cada color de lobby
    return "TABLA DE LOBBYS POR COLOR\n\n---COLOR--------RANK---RANGO KD-\n\n-DIAMANTE 1  |95%|   1.14 -> 1.19\n-DIAMANTE 2  |90%|   1.11 -> 1.14\n-DIAMANTE 3  |85%|   1.09 -> 1.11\n-DIAMANTE 4  |80%|   1.07 -> 1.09\n-PLATINO 1      |75%|   1.06 -> 1.07\n-PLATINO 2      |70%|   1.04 -> 1.06\n-PLATINO 3      |65%|   1.01 -> 1.04\n-PLATINO 4      |60%|   0.97 -> 1.01\n-ORO 1               |55%|   0.93 -> 0.97\n-ORO 2               |50%|   0.90 -> 0.93\n-ORO 3               |45%|   0.88 -> 0.90\n-ORO 4               |40%|   0.86 -> 0.88\n-PLATA 1           |35%|   0.84 -> 0.86\n-PLATA 2           |30%|   0.82 -> 0.84\n-PLATA 3           |25%|   0.79 -> 0.82\n-PLATA 4           |20%|   0.74 -> 0.79\n-BRONCE 1       |15%|   0.67 -> 0.74\n-BRONCE 2       |10%|   0.61 -> 0.67\n-BRONCE 3       |05%|   0.57 -> 0.61\n-BRONCE 4       |00%|   0.52 -> 0.57"

def verifyLarge(result):    ##Verifico el largo del mensaje ya que telegram solo permite mensajes hasta 4096 caracteres de largo
    if len(result) > 4096:
        return "ERROR: Mensaje demasiado largo > 4096"
    else:
        return result




def login():        # Login contra callofduty.com
    get_login = requests.get('https://profile.callofduty.com/cod/login')
    csrf_token = get_login.cookies['XSRF-TOKEN']

    params = {
        'username': "augustofortes94@gmail.com",
        'password': "Hormigator1.codapi",
        'remember_me': 'true',
        '_csrf': csrf_token
    }

    get_login = requests.post('https://profile.callofduty.com/do_login?new_SiteId=cod', params=params)

    return get_login.cookies

    """
    cookie = {"ACT_SSO_COOKIE":os.getenv('sso_token')}
    try:
        resp = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/psn/gamer/Hormigator1/profile/type/wz', cookies=cookie, timeout=30).json()
        if resp['status'] == "error" and resp['data']['message'] == "Not permitted: not authenticated":     ##Consulto si no se pudo logear
            return "ERROR: 'Not permitted: not authenticated'\nCertificado vencido"
        else:
            return cookie
    except requests.exceptions.Timeout as err:
        return "ERROR TIMEOUT: al hacer loggin en cod api"
    """

# Modularizacion
def getLobbyId(platform, user, cookie):  # Obtengo el ID de la ultima lobby
    try:
        # resp_lastMatches = requests.get('https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/'+platform+'/gamer/'+user+'/matches/wz/start/0/end/0/details', cookies=cookie, params= '1', timeout=30).json()
        resp_lastMatches = requests.get('https://app.wzstats.gg/v2/player/match/withPlayers/?username=' + user + '&platform=' + platform, timeout=30).json()
        # return resp_lastMatches["data"]["matches"][0]["matchID"]
        return resp_lastMatches["matches"][0]["id"]
    except requests.exceptions.Timeout as err:
        return "ERROR TIMEOUT: al obtener la lista de partidas en cod api"
    except:
        return "ERROR: no se pudo obtener el ID de la partida desde 'my.callofduty.com'"

def getLobbyInfo(lobbyId):  # Obtengo toda la informacion del lobby
    if lobbyId == "ERROR: no se pudo obtener el ID de la partida desde 'my.callofduty.com'":
        return lobbyId
    else:
        try:    ##intentar obtener la data de la ultima partida
            lobby = requests.get('https://app.wzstats.gg/v2/?matchId='+lobbyId, timeout=30).json()
        except requests.exceptions.Timeout as err:
            return "ERROR TIMEOUT: al obtener la partida en wzstats"
        except:     ##si no obtiene la data de la ultima partida arroja error
            return "ERROR: No se pudo conectar con wzstats.gg."
        
        jugadores = filterLobbyMode(lobby["data"]["mode"]) + time.strftime('%d/%m/%Y %H:%M', time.localtime(lobby["data"]["startedAt"] - 10800)) + "hs\n\n-KD---KILLS---NAME\n\n"    ##Obtengo la hora de la partida y le resto 3hs
        data = {}   ##estructura donde guardo la info de cada jugador. Dict
        prom = 0
        y = 0   ##contador
        sinkd = 0   ##contador de jugadores sin kd encontrados
        for _ in lobby["data"]["players"]:
            try:    ##intentar encontrar KD
                prom = prom + round(float(lobby["data"]["players"][y]["playerStat"]["lifetime"]["mode"]["br"]["properties"]["kdRatio"]), 2) ##sumo el kd a un general para despues sacar promedio
                data[y] = "-" + filterKD(str(round(float(lobby["data"]["players"][y]["playerStat"]["lifetime"]["mode"]["br"]["properties"]["kdRatio"]), 2))) + "   "  ##dejo el kd prolijo
            except:     ##si no encuentra el kd le pone como 0.00
                data[y]= "-0.00   "
                sinkd += 1
            
            try:    ##esto es por si es un plunder o blood money que no tiene teamplacement
                data[y]= data[y] + filterKills(str(lobby["data"]["players"][y]["playerMatchStat"]["playerStats"]["kills"])) + lobby["data"]["players"][y]["playerMatchStat"]["player"]["username"] + filterPosition(lobby["data"]["players"][y]["playerMatchStat"]["playerStats"]["teamPlacement"])
            except:
                data[y]= data[y] + filterKills(str(lobby["data"]["players"][y]["playerMatchStat"]["playerStats"]["kills"])) + lobby["data"]["players"][y]["playerMatchStat"]["player"]["username"] + "\n"
            y += 1

        for key, value in OrderedDict(sorted(data.items(), key=itemgetter(1), reverse=True)).items():   ##itero por todos los jugadores
            jugadores = jugadores + value   ##guardo su info en string

        return verifyLarge(jugadores + "\n" + str(y) +" Jugadores\n" + "Promedio KD Lobby: "+ filterKD(str(round((prom/(y-sinkd)), 2))) + "\n" + lobbyColour(round((prom/(y-sinkd)), 3))) ##saco el promedio de todos los que tienen kd

def getLobbyTotalInfo(platform, name):  # Al metodo que obtiene toda la informacion le paso el resultado del metodo que obtiene el ID de la lobby
    cookie = login()
    if cookie == "ERROR: 'Not permitted: not authenticated'\nCertificado vencido":
        return cookie
    else:
        matchid= getLobbyId(platform, name, cookie)
        print(matchid)
        return getLobbyInfo(matchid)


print(getLobbyTotalInfo("psn", "Hormigator1"))

#intento ordenar lobby
#lobby = sorted(lobby, key=lambda k: k["data"]["players"][0]["playerStat"]["lifetime"]["mode"]["br"]["properties"].get("kdRatio", 0), reverse=True)

##se podria hacer una funcion que sea obtener kd y que le pase el ID "uno" y consulte en el perfil del jugador el kd

## LINK LOGIN
# https://profile.callofduty.com/do_login?new_SiteId=cod

## LINK PERFIL
# https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/psn/gamer/Hormigator1/profile/type/wz

## LINK ULTIMAS PARTIDAS (obtengo el ID)
# https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/psn/gamer/Hormigator1/matches/wz/start/0/end/0/details

## LINK LOBBY (detalle)
# https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/fullMatch/wz/11940108540335301767/it

## LINK LOBBY sbmm
# https://app.wzstats.gg/v2/?matchId=11940108540335301767

## LINK LOBBY CODTRACKER
# https://api.tracker.gg/api/v2/warzone/standard/matches/5622551636149190222





