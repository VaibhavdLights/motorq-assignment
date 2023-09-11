import requests

endpoint = 'http://localhost:8000/api/login/'

login_data = {
    'username': '1234567890', 
    'password': 'securepassword',
}

# Send a POST request to the user login endpoint
response = requests.post(endpoint, json=login_data)

# Check the response
if response.status_code == 200:
    print('User logged in successfully!')
elif response.status_code == 401:
    print('Invalid login credentials.')
else:
    print('User login failed. An error occurred.')


print('Response Content:')
print(response.text)
