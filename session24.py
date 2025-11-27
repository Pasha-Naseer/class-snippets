import requests
city = input("enter city name: ")

api = f'https://wttr.in/{city}?format=j1'
resp_code =  requests.get(api)
# print(resp_code)
data = resp_code.json()
print(data)
# print(data['current_condition'][0])
print(data['current_condition'][0]['temp_C'])
print(data['current_condition'][0]['observation_time'])
