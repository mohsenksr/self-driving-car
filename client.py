import json

import requests


def send_report(sensor_name: str, value):
    resp = requests.put(
        "http://localhost:8000",
        data=json.dumps({
            "sensor_name": sensor_name,
            "value": value
        }))
    print(f"Report: {resp.status_code}")
    print(resp.text)
