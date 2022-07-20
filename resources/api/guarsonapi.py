import os
import requests

url = 'https://apiguarson.herokuapp.com/'


def login():        # Login contra apiguarson en heroku
    params = {
        'username': os.getenv('apiusername'),
        'password': os.getenv('apipswd'),
    }
    response = requests.post(url + 'api/login/', data=params)
    return response.cookies


def setString(data):
    cadena = data['name'] + ':\n\n'
    if data['muzzle'] is not None:
        cadena = cadena + '-' + data['muzzle'] + '\n'
    if data['barrel'] is not None:
        cadena = cadena + '-' + data['barrel'] + '\n'
    if data['laser'] is not None:
        cadena = cadena + '-' + data['laser'] + '\n'
    if data['optic'] is not None:
        cadena = cadena + '-' + data['optic'] + '\n'
    if data['stock'] is not None:
        cadena = cadena + '-' + data['stock'] + '\n'
    if data['underbarrel'] is not None:
        cadena = cadena + '-' + data['underbarrel'] + '\n'
    if data['magazine'] is not None:
        cadena = cadena + '-' + data['magazine'] + '\n'
    if data['ammunition'] is not None:
        cadena = cadena + '-' + data['ammunition'] + '\n'
    if data['reargrip'] is not None:
        cadena = cadena + '-' + data['reargrip'] + '\n'
    if data['perk'] is not None:
        cadena = cadena + '-' + data['perk'] + '\n'
    if data['perk2'] is not None:
        cadena = cadena + '-' + data['perk2'] + '\n'
    if data['alternative'] is not None:
        cadena = cadena + '\n' + data['alternative'] + '\n'
    if data['alternative2'] is not None:
        cadena = cadena + '\n' + data['alternative2']
    return cadena


def getListCommands(category):  # Return list commands of a category
    cookie = login()
    data = requests.get(url + 'api/weapons/?category=' + category, cookies=cookie).json()
    list_commands = ''
    for command in data['weapons']:
        list_commands = list_commands + '\n-/' + command[0]
    return list_commands


def getLobbyFromApi(mode):
    cookie = login()
    data = requests.get(url + 'api/mode/' + mode[mode.find('/')+1:] + '/', cookies=cookie).json()   # Quito / si el nombre esta compuesto en 2
    try:
        return data['mode'][0]['name'] + '\n'
    except:
        return 'MODO DESCONOCIDO\n'


def getWeaponFromApi(command):
    cookie = login()
    data = requests.get(url + 'api/weapons/?command=' + command, cookies=cookie).json()
    try:
        return setString(data['weapons'][0])
    except:
        return 'Arma no encontrada'
