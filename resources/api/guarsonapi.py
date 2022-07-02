import os
import requests

def login():        ##Login contra apiguarson en heroku
    params = {
        'username': os.getenv('apiusername'),
        'password': os.getenv('apipswd'),
    }
    response = requests.post('https://apiguarson.herokuapp.com/api/login/', data=params)
    return response.cookies

def setString(data):
    cadena = data['name'] + ':\n\n'
    if data['muzzle'] != None:
        cadena = cadena + '-' + data['muzzle'] + '\n'
    if data['barrel'] != None:
        cadena = cadena + '-' + data['barrel'] + '\n'
    if data['laser'] != None:
        cadena = cadena + '-' + data['laser'] + '\n'
    if data['optic'] != None:
        cadena = cadena + '-' + data['optic'] + '\n'
    if data['stock'] != None:
        cadena = cadena + '-' + data['stock'] + '\n'
    if data['underbarrel'] != None:
        cadena = cadena + '-' + data['underbarrel'] + '\n'
    if data['magazine'] != None:
        cadena = cadena + '-' + data['magazine'] + '\n'
    if data['ammunition'] != None:
        cadena = cadena + '-' + data['ammunition'] + '\n'
    if data['reargrip'] != None:
        cadena = cadena + '-' + data['reargrip'] + '\n'
    if data['perk'] != None:
        cadena = cadena + '-' + data['perk'] + '\n'
    if data['perk2'] != None:
        cadena = cadena + '-' + data['perk2'] + '\n'
    if data['alternative'] != None:
        cadena = cadena + '\n' + data['alternative'] + '\n'
    if data['alternative2'] != None:
        cadena = cadena + '\n' + data['alternative2']
    return cadena

def getLobbyFromApi(mode):
    cookie = login()
    data = requests.get('https://apiguarson.herokuapp.com/api/mode/' + mode + '/', cookies=cookie).json()
    if data['message'] == 'Success':
        return setString(data['mode'][0]['name']) + '\n'
    return 'MODO DESCONOCIDO\n'

def getWeaponFromApi(command):
    cookie = login()
    data = requests.get('https://apiguarson.herokuapp.com/api/weapons/' + command, cookies=cookie).json()
    if data['message'] == 'Success':
        return setString(data['weapons'][0])
    return 'Arma no encontrada'
    