import requests

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-key': "ef0a41e6f7mshbf20b2533dac2f8p16fc68jsn3fd54161d813",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)