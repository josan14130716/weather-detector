from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=88dd8d2233356d5ca4ff79c1b6d17a17').read()
        json_data = json.loads(res)
        data = {
            "country_code":str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + '' +
            str(json_data['coord']['lat']),
            "temp":float(json_data['main']['temp'])-273.15,
            "pressure": str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data={}
    return render(request, 'index.html',{'city':city, 'data':data})
