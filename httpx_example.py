import httpx

base_url = "https://jsonplaceholder.typicode.com/todos/1"

# response = httpx.get(base_url)
# print(response.status_code)
# print(response.json())

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.status_code)
# print(response.json())

data = {
    "username":"test_user",
    "password":"123456"
}
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.status_code)
# print(response.json())

headers = {
    "Authorization": "Bearer my_token"
}
# response = httpx.get("https://httpbin.org/get", headers=headers)
# print(response.headers)
# print(response.json())

# params = {"userId":1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1",params=params)
# print(response.url)
# print(response.json())

files = {"file":("example.txt",open("example.txt","rb"))}
response = httpx.post("https://httpbin.org/get",files=files)
print(response.json())
