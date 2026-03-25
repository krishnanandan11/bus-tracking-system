import requests

url = "http://127.0.0.1:5000/update_location"

data = {
    "bus_id": 1,   # ✅ REQUIRED
    "latitude": 28.6200,
    "longitude": 77.2200
}
res = requests.post(url, json=data)
print(res.json())