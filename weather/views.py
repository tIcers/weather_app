from django.shortcuts import render

import requests



# Create your views here.
def index(request):
	URL = 'https://api.openweathermap.org/data/2.5/weather'
	PARAMS = {'q':'tokyo','appid':appid,'units':'metric'}

	req = requests.get(url = URL,params = PARAMS)
	req_json = req.json()
	description = req_json['weather'][0]['description']
	icon = req_json['weather'][0]['icon']
	temp = req_json['main']['temp']
	humid = req_json['main']['humidity']

	return render(request, 'weather/index.html',{'description':description,'icon':icon,'temp':temp,'humid':humid})
