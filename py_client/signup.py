import requests

endpoint = 'http://localhost:8000/api/signup/'
registration_data = {
    'username': '1234567890',
    'password': 'securepassword',  
}

response = requests.post(endpoint, json=registration_data)

if response.status_code == 201:
    print('User registered successfully!')
elif response.status_code == 400:
    print('User registration failed. Validation error.')
else:
    print('User registration failed. An error occurred.')

print('Response Content:')
print(response.text)
