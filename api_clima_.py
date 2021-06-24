
import requests
import json
import datetime 

print("Consultara una localizacion por: ")

metodo = input("Cordenadas o Ciudad? " )
if(metodo == "ciudad"):
    ciudad =  input("Nombre de la Ciudad? " )
    consulta = {"q": ciudad,"appid":"bf360c66d83082e79a08c9622169a5c8","units":"metric","lang":"sp, es"}
    print(consulta)
elif(metodo == "cordenadas"):
    latitud =  float(input("latitud "))
    longitud =  float(input("longitud "))
    consulta = {"lat": latitud, "lon": longitud,"appid":"bf360c66d83082e79a08c9622169a5c8","units":"metric","lang":"sp, es"}
    print(consulta)
else:
    print("No se reconose metodo")

url = "https://api.openweathermap.org/data/2.5/weather"

busqueda = requests.request("GET", url, params=consulta)
info = json.loads(busqueda.content)

hora = datetime.datetime.fromtimestamp(info['dt'])
amanecer = datetime.datetime.fromtimestamp(info['sys']["sunrise"])
atardecer = datetime.datetime.fromtimestamp(info['sys']["sunset"])

print(busqueda.text)

print('Ciudad:', info['name'])
print('Fecha y Hora:', hora.strftime("%d-%m-%Y, %H:%M:%S"))
print('Población:', info['id'])
print('Latitud:', info['coord']['lat'])
print('Longitud:', info['coord']['lon'])
print('Condiciones climatologicas')
print('Temperatura:', info['main']['temp'])
print('Sensación termica:', info['main']['feels_like'])
print('Temperatura minima:', info['main']['temp_min'])
print('Temperatura máxima:', info['main']['temp_max'])
print('Presión atmosferica:', info['main']['pressure'])
print('Humedad:', info['main']['humidity'])
print('Visibilidad:', info['visibility'])
print('Velocidad del viento', info['wind']['speed'])
print('Dirección del viento:', info['wind']['deg'])
print('Abundancia de nubes:', str(info['clouds']['all']) + ' %')
print('Código país:', info['sys']['country'])
print('Hora amanecer:', amanecer.strftime('%H:%M:%S'))
print('Hora atardecer:', atardecer.strftime('%H:%M:%S'))

