import random

from sanic import Sanic
from sanic.response import text
from sanic_ext import render

app = Sanic("MyHelloWorldApp")

data = {
    "Light": "on",
    "Front": 24.3333 + random.random() * 5,
    "Right": 64.3333 + random.random() * 5,
    "Left": 214.3333 + random.random() * 5,
    "LightSensor": random.random() * 60 + 40,
    "DCMotor": "on"
}


@app.get("/")
async def get_sensor_data(request):
    print(data)
    result = ""
    for sensor_name, value in data.items():
        result += "<br>" + f"{sensor_name}: {value}"
    return await render(
        "live-demo.html", context={
            **data,
            "text": result,
            "max_sensor": 300,
            "min_sensor": 1,

        }, status=200
    )
    # return text(result)


@app.put("/")
async def report_sensor(request):
    sensor_name = request.json['sensor_name']
    value = request.json['value']
    data[sensor_name] = value
    return text("Set!")
