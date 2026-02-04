import httpx

login_payload = {
    "email":"test@example.com",
    "password":"string"
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login",json=login_payload)
login_response_data=login_response.json()

print(f"login response: {login_response}")
print(f"login response_data: {login_response_data}")

refresh_payload = {"refreshToken":login_response_data["token"]["refreshToken"]}
refresh_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/refresh",json=refresh_payload)
refresh_response_data=refresh_response.json()

print(f"refresh response: {refresh_response_data}")
print(f"status code: {refresh_response.status_code}")