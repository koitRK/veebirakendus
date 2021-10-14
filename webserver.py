from os import SCHED_RESET_ON_FORK
from typing import Counter
from flask import Flask, request, render_template
app = Flask(__name__)

python_data = {"sensor1_value": 0, "sensor2_value": 0, "counter": 0, "open": 1}


def sensor_value_updated():
    global python_data

    if python_data["sensor1_value"] > python_data['sensor2_value']:
        python_data["open"] = 1
    else:
        python_data["open"] = 0


@app.route('/main', methods=['GET', 'POST'])
def main():

    return render_template('index.html', data=python_data)


@app.route('/sensor1/<int:value>')
def sensor1(value):
    global python_data

    python_data['sensor1_value'] = value
    python_data['counter'] += 1

    sensor_value_updated()

    return 'OK! Sensor1 value: ' + str(value), 200


@app.route('/sensor2/<int:value>')
def sensor2(value):
    global python_data

    python_data['sensor2_value'] = value
    python_data['counter'] += 1

    sensor_value_updated()

    return 'OK! Sensor2 value: ' + str(value), 200


@app.route('/actuator')
def actuator():

    if python_data["open"]:
        return "Window OPEN", 200
    return "Window CLOSE", 200