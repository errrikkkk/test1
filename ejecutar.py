import requests
import subprocess
from colorama import init, Fore

# Inicializar Colorama
init(autoreset=True)

def show_title():
    print(Fore.RED + r'''
`7MMF'  `7MMF'  .g8""8q.   `7MM"""Mq.  `7MMF'   `7MF' .M"""bgd 
  MM      MM  .dP'    `YM.   MM   `MM.   MM       M  ,MI    "Y 
  MM      MM  dM'      `MM   MM   ,M9    MM       M  `MMb.     
  MMmmmmmmMM  MM        MM   MMmmdM9     MM       M    `YMMNq. 
  MM      MM  MM.      ,MP   MM  YM.     MM       M  .     `MM 
  MM      MM  `Mb.    ,dP'   MM   `Mb.   YM.     ,M  Mb     dM 
.JMML.  .JMML.  `"bmmd"'   .JMML. .JMM.   `bmmmmd"'  P"Ybmmd"  
         
          
          
De errriiiiikkk

    ''')

def get_geo_info(ip):
    try:
        url = f"https://ipinfo.io/{ip}?token=TU_TOKEN_DE_ACCESO_AQUI"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                'IP': data['ip'],
                'País': data['country'],
                'Región': data['region'],
                'Ciudad': data['city'],
                'Código Postal': data['postal'],
                'Coordenadas': data['loc'].split(',')
            }
        else:
            return "Error al obtener información de geolocalización."
    except Exception as e:
        return f"Error: {e}"

def send_notification(ip):
    try:
        subprocess.run(['termux-notification', '--title', 'Geolocalización IP', '--content', f'IP: {ip} haciendo geolocalización'])
        print("Notificación enviada al dispositivo móvil.")
    except Exception as e:
        print(f"Error al enviar la notificación: {e}")

def main():
    show_title()
    print("Seleccione una opción:")
    print("1. Obtener información de geolocalización de una dirección IP.")
    print("0. Salir")

    choice = input("\nIngrese el número de opción deseada: ")

    if choice == '1':
        ip = input("Ingrese una dirección IP: ")
        print("\nInformación de la IP:")
        geo_info = get_geo_info(ip)
        print(geo_info)
        send_notification(ip)
    elif choice == '0':
        print("Saliendo del programa...")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()
