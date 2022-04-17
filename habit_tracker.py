from datetime import datetime

import requests

# pixela endpoint stores the url for pixela
pixela_ENDPOINT = "https://pixe.la/v1/users"

# User Creation and Credentials
USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "graph12"

# creation of a dictionary
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response=requests.post(url=pixela_ENDPOINT,json=user_params)
# response.raise_for_status()
# print(response.text)
# now we have created a user with the above profile details

# Graph Creation for the User
graph_END_POINT = f"{pixela_ENDPOINT}/{USERNAME}/graphs"
# creation of graph_params dictionary to build a graph which keeps track of progress of the users

graph_params = {
    "id": "graph12",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# headers dictionary is created for authentication purposes(here it stores X-USER-TOKEN)

headers = {
    "X-USER-TOKEN": TOKEN
}
# response=requests.post(url=graph_END_POINT,json=graph_params,headers=headers)
# print(response.text)
# response.raise_for_status()

# Pixel Creation to Track the Progress of the Respective Users

pixel_creation_END_POINT = f"{pixela_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2022, month=4, day=1)
pixel_creation_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.90",
}
# response=requests.post(url=pixel_creation_END_POINT,json=pixel_creation_params,headers=headers)
# print(response.text)

# Updating the Pixel details with HTTP PUT Request
update_pixel_ENDPOINT = f"{pixela_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
updated_pixel_data = {
    "quantity": "10.0"
}
response = requests.put(url=update_pixel_ENDPOINT, json=updated_pixel_data, headers=headers)
print(response.text)
