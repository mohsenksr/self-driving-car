from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")
data = {}


@app.get("/")
async def get_sensor_data(request):
    print(data)
    result = ""
    for sensor_name, value in data.items():
        result += "\n" + f"Sensor {sensor_name}: {value}"
    return text(result)


@app.put("/")
async def report_sensor(request):
    sensor_name = request.json['sensor_name']
    value = request.json['value']
    data[sensor_name] = value
    return text("Set!")
