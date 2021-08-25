import requests as req
import json

API_KEY = '8bf29d04be249c169416af300176d94c9'

def get_weather(city='Seoul'):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&lang=kr'
    print(URL)
    weather = {} #결과
    res = req.get(URL)
    if res.status_code == 200:
        result = res.json()
        weather['main']=result['weather'][0]['main']
        weather['description'] = result['weather'][0]['description']
        print(result['weather'][0]['description'])
        icon=result['weather'][0]['icon']
        weather['icon']=f'http://openweathermap.org/img/w/{icon}.png'
        weather['etc'] = result['main']
         
    else:
        print('error', res.status_code)

    return weather

def download(url, file_name):
    with open(file_name,"wb") as file:
        response = req.get(url)
        file.write(response.content)

weather = get_weather()
print(json.dumps(weather, indent=4, ensure_ascii=False))
print(json.dumps(weather))
print('섭씨', weather['etc']['temp']-273.15)


download(weather['icon'],
                weather['icon'].split('/')[-1]) #url에서 파일명 추출
