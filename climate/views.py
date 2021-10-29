from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
from time import time, ctime

KEY = "3683e2c67de2c392420fe6f627158a2a"

def index(request):
    is_private = request.POST.get('a', False)
    is_private2 = request.POST.get('b', False)
    context = {"pais": is_private, "pais2": is_private2}


    return render(request,'climate/index.html',context)

def weather(request, country):
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={country}&units=metric&appid=3683{KEY}')
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


def days(request, country):
    context={"hola":"alo"}
    days = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?q={country}&units=metric&cnt=16&appid={KEY}")
    da = days.json()
    print(da)
    return render(request, 'climate/days.html', context)