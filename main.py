import requests




#disclaimer : this is only for educational purposes... do not use this because it will violate the TOS of discord.
url = 'https://discord.com/api/v9/users/@me/profile'

# Define the Authorization token and the payload
authorization_token = 'ur token'
payload = {
    'bio': 'the bio u want to change to'
}


headers = {
    'Authorization': authorization_token,
    'Content-Type': 'application/json'
}


response = requests.patch(url, headers=headers, json=payload)


print(response.text)
