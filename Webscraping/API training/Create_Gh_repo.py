import requests
import json

header = {
    "Authorization": "token 717de05f024565cdb89cf48746b557466dbca055"
}
params = json.dumps({
    "name": "New"
})
URL = 'https://api.github.com/user/repos'
page = requests.post(URL, headers=header, data=params)
print(page)