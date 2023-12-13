from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def weather_app(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=8f2eb46093f168125c1440abfeb7cf13').read()
        list_of_data = json.loads(source)
        
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'city_name': str(list_of_data['name']),
            'temp': str(list_of_data['main']['temp']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
    return render(request,'index.html',data)
        