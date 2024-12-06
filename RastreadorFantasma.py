#!/usr/bin/python

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'



def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


@is_option
def IP_Track():
    ip = input(f"{Wh}\n INGRESAR IP : {Gr}")  
    print()
    print(f' {Wh}============={Gr} SE HA RASTREADO LA IP {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP                  :{Gr}", ip)
    print(f"{Wh} TIPO DE IP            :{Gr}", ip_data["type"])
    print(f"{Wh} PAIS                  :{Gr}", ip_data["country"])
    print(f"{Wh} CODIGO DE PAIS        :{Gr}", ip_data["country_code"])
    print(f"{Wh} CIUDAD                :{Gr}", ip_data["city"])
    print(f"{Wh} CONTINENTE            :{Gr}", ip_data["continent"])
    print(f"{Wh} CODIGO DE CONTINENTE  :{Gr}", ip_data["continent_code"])
    print(f"{Wh} REGION                :{Gr}", ip_data["region"])
    print(f"{Wh} CODIGO DE REGION      :{Gr}", ip_data["region_code"])
    print(f"{Wh} LATITUD               :{Gr}", ip_data["latitude"])
    print(f"{Wh} LONGITUD              :{Gr}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} MAPA                  :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU                    :{Gr}", ip_data["is_eu"])
    print(f"{Wh} POSTAL                :{Gr}", ip_data["postal"])
    print(f"{Wh} CODIGO DE LLAMADA     :{Gr}", ip_data["calling_code"])
    print(f"{Wh} CAPITAL               :{Gr}", ip_data["capital"])
    print(f"{Wh} FRONTERAS             :{Gr}", ip_data["borders"])
    print(f"{Wh} BANDERA DE PAIS       :{Gr}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN                   :{Gr}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG                   :{Gr}", ip_data["connection"]["org"])
    print(f"{Wh} ISP                   :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} DOMINIO               :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID                    :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR                  :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST                   :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} OFFSET                :{Gr}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC                   :{Gr}", ip_data["timezone"]["utc"])
    print(f"{Wh} TIEMPO                :{Gr}", ip_data["timezone"]["current_time"])


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}INGRESE NUMERO OBJETIVO : {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")
    default_region = "ID"

    parsed_number = phonenumbers.parse(User_phone, default_region)
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}=========={Gr} SE HA RASTREADO EL NUMERO {Wh}==========")
    print(f"\n {Wh}LOCALIZACION        :{Gr} {location}")
    print(f" {Wh}CODIGO DE REGION      :{Gr} {region_code}")
    print(f" {Wh}TIEMPO                :{Gr} {timezoneF}")
    print(f" {Wh}OPERADOR              :{Gr} {jenis_provider}")
    print(f" {Wh}NUMERO VALIDO         :{Gr} {is_valid_number}")
    print(f" {Wh}POSIBLE NUMERO        :{Gr} {is_possible_number}")
    print(f" {Wh}FORMATO INTERNACIONAL :{Gr} {formatted_number}")
    print(f" {Wh}FORMATO MOVIL         :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}NUMERO ORIGINAL       :{Gr} {parsed_number.national_number}")
    print(f" {Wh}E.164 FORMATO         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}CODIGO DE PAIS        :{Gr} {parsed_number.country_code}")
    print(f" {Wh}NUMERO DE PAIS        :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}TIPO                 :{Gr} ESTE ES UN NUMERO MOVIL")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}TIPO                 :{Gr} ESTA ES UNA LINEA FIJA DE NUMERO")
    else:
        print(f" {Wh}TIPO                 :{Gr} ESTE ES OTRO TIPO DE NUMERO")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}INGRESE USUARIO : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "X"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}USUARIO NO ENCONTRADO{Ye}!")
    except Exception as e:
        print(f"{Re}ERROR : {e}")
        return

    print(f"\n {Wh}=========={Gr} SE HA RASTREADO EL USUARIO {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {SITIOS} : {Gr}{url}")


@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"TU IP:{Show_IP}")

options = [
    {
        'num': 1,
        'text': 'RASTREAR IP',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'VER TU IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'RASTREAR POR NUMERO MOVIL',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'RASTREAR USUARIO',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'SALIR',
        'func': exit
    }
]


def clear():

    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('OPCION NO ENCONTRADA')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('NO ENCONTRADO')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ + ] ENTER PA CONTINUAR  [ + ]')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}SALIR')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():

    clear()
    stderr.writelines(f"""{Wh}[ + ] RASTREADOR FANTASMA [ + ]""")

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}[ + ] RASTREADOR FANTASMA [ + ]""")
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}SELECCIONE OPCION : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}INGRESE EL NUMERO :')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}SALIR')
        time.sleep(2)
        exit()
