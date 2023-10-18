import requests

word = ""
username = ""
password = ""
users = []

info = requests.get('http://127.0.0.1:5000/database/users').text

for i in info:
    if i != '\n':
        if i != '|':
            word += i
        else:
            if username == "":
                username = word
                word = ""
            else:
                password = word
                word = ""
    else:
        users.append({'username':username, 'password':password})
        word = ""
        username = ""
        password = ""

for user in users:
    print(user)
