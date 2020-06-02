import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = "q=English%20is%20hard%2C%20but%20detectably%20so"
headers = {
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "489e1bce82msh12e327e6d198ae2p1af2bdjsn1431242951c6",
    'accept-encoding': "application/gzip",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)