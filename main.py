import requests

API_KEY = "47e771bec1039ca68e7e8bcdec3c1339"
## CIDADE = "rio de janeiro"
LINK = f"https://api.openweathermap.org/data/2.5/weather?lat={-13.1167}&lon={-41.9833}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(LINK)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] -273.15
print(descricao, f"{temperatura} ºC")