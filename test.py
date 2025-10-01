dict = {
    "aenstein": {
        "first_name": "albert",
        "last_name": "einstein"
    }
}

for username, user_info in dict.items():
    print(f"{username}")

    for key, value in user_info.items():
        print(f"{key}: {value}")