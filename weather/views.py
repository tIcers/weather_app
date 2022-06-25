from django.shortcuts import render

import requests
import datetime #user need time when they search



# Create your views here.
def index(request):

	if 'city' in request.POST:
		city = request.POST['city']
	else:
		city = 'tokyo'

	
	URL = 'https://api.openweathermap.org/data/2.5/weather'
	PARAMS = {'q':city,'appid':appid,'units':'metric'}

	req = requests.get(url = URL,params = PARAMS)
	req_json = req.json()
	description = req_json['weather'][0]['description']
	icon = req_json['weather'][0]['icon']
	temp = req_json['main']['temp']
	humid = req_json['main']['humidity']
	dt = datetime.datetime.today()
	month = dt.strftime("%B")
	day = dt.day

	if request.method =="POST":
		city = request.POST['city']
		

	return render(request, 'weather/index.html',{'description':description,'icon':icon,'temp':temp,
					'humid':humid,'day':day,'city':city,'month':month})
