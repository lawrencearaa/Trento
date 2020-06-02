import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "489e1bce82msh12e327e6d198ae2p1af2bdjsn1431242951c6",
    'accept-encoding': "application/gzip"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)