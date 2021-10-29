from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
from time import time, ctime

KEY = "3683e2c67de2c392420fe6f627158a2a"

def index(request):
    is_private = request.POST.get('a', False)
    is_private2 = request.POST.get('b', False)
    is_private3 = request.POST.get('c', False)

    pol = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat=19&lon=-99&appid={KEY}")
    polu = pol.json()
    co = polu["list"][0]["components"]["co"]
    no = polu["list"][0]["components"]["no"]
    no2 = polu["list"][0]["components"]["no2"]
    o3 = polu["list"][0]["components"]["o3"]
    so2 = polu["list"][0]["components"]["so2"]
    pm2_5 = polu["list"][0]["components"]["pm2_5"]
    pm10 = polu["list"][0]["components"]["pm10"]
    context = {"pais": is_private, "latitud": is_private2, "longitud": is_private3,"co":co,"no":no,"no2":no2,"o3":o3,"so2":so2,"pm2_5":pm2_5,"pm10":pm10}
    

    return render(request,'climate/index.html',context)

def weather(request, country):
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={country}&units=metric&appid={KEY}')
    weatherL = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=MEXICO&units=metric&appid={KEY}')
    weatherLocal = weatherL.json()
    weatherMain = (weather.json())
    print(weatherMain)
    main = weatherMain["weather"][0]["main"]
    desc = weatherMain["weather"][0]["description"]
    temp = weatherMain["main"]["temp"]
    feels = weatherMain["main"]["feels_like"]
    mini = weatherMain["main"]["temp_min"]
    maxi = weatherMain["main"]["temp_max"]
    pressure = weatherMain["main"]["pressure"]
    hum = weatherMain["main"]["humidity"]
    speed = weatherMain["wind"]["speed"]
    degr = weatherMain["wind"]["deg"]
    clouds = weatherMain["clouds"]["all"]
    timezone = ctime(weatherMain["timezone"])
    timezoneLocal = ctime(weatherLocal["timezone"])
    context = {"country": country, "main":main,"desc":desc,"temp":temp,"feels":feels,"mini":mini,"maxi":maxi,"pressure":pressure,"hum":hum,"speed":speed,"degr":degr,"clouds":clouds,"timezone":timezone, "timezoneLocal":timezoneLocal}
    return render(request, 'climate/weather.html', context)


def days(request, latitud, longitud):
    
    days = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={KEY}")
    da = days.json()
    print(da)
    lon = da["coord"]["lon"]
    lat = da["coord"]["lat"]
    main = da["weather"][0]["main"]
    desc = da["weather"][0]["description"]
    temp = da["main"]["temp"]
    feels = da["main"]["feels_like"]
    mini = da["main"]["temp_min"]
    maxi = da["main"]["temp_max"]
    pressure = da["main"]["pressure"]
    hum = da["main"]["humidity"]
    speed = da["wind"]["speed"]
    degr = da["wind"]["deg"]
    clouds = da["clouds"]["all"]
    timezone = ctime(da["timezone"])
    timezoneLocal = ctime(da["timezone"])

    try:
        sea = da["main"]["sea_level"]
        ground= da["main"]["grnd_level"]
        code = da["sys"]["country"]
    except:
        sea = ""
        ground = ""
        code = ""

    context={"code":code,"ground":ground,"sea":sea,"timezoneLocal":timezoneLocal,"timezone":timezone,"clouds":clouds,"degr":degr,"speed":speed,"lon":lon,"lat":lat,"main":main,"desc":desc,"temp":temp,"feels":feels,"mini":mini,"maxi":maxi,"pressure":pressure,"hum":hum}
    return render(request, 'climate/days.html', context)