import requests


def callWebApi():

    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.patch(api_url)
    print("response from  " +api_url + " is : \n ")
    print(response.json())

