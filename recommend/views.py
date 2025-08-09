import requests
from django.shortcuts import render

def home(request):
    return render(request, 'recommend/home.html')  # Home page

def get_weather(request):
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "3ae53c0efbac0c87e382bfc82fad1a22"  
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:  # Valid city
            temp = data['main']['temp']
            weather = data['weather'][0]['main']

            # Song recommendations based on weather/temperature
            if weather == "Rain":
                advice = "Carry an umbrella ☔. Or dance in the rain."
                song_id = "7wtfhZwyrcc"  # Believer
            elif temp > 30:
                advice = "It’s hot! Shorts + cold drinks time."
                song_id = "9bZkp7q19f0"  # Gangnam Style
            elif weather == "Clouds":
                advice = "Perfect day for a hoodie and coffee."
                song_id = "kJQP7kiw5Fk"  # Despacito
            elif temp < 15:
                advice = "Wrap up warm! Maybe with a blanket burrito."
                song_id = "3JZ_D3ELwOQ"  # See You Again
            else:
                advice = "Weather’s fine — wear what you like."
                song_id = "fRh_vgS2dFE"  # Sorry

            context = {
                'city': city,
                'temp': temp,
                'weather': weather,
                'advice': advice,
                'song_id': song_id
            }
        else:
            context = {'error': 'City not found. Try again!'}

        return render(request, 'recommend/result.html', context)

    # If accessed directly without POST
    return render(request, 'recommend/home.html')
