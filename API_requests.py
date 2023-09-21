import requests

response = requests.get("https://pypi.org/project/requestsj/")
jsonData= response.json()
print(jsonData[0])

print(response)
