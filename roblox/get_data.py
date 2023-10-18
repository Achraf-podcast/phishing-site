import requests

word = ""
username = ""
password = ""
users = []

info = requests.get('http://earnforfree.pythonanywhere.com/database/users').text

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
