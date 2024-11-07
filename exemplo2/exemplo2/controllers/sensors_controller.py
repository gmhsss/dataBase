#sensors_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors import Sensor
from models.iot.devices import Device
from models.db import db


sensor_ = Blueprint("sensor_",__name__, template_folder="views")


@sensor_.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")


@sensor_.route('/edit_sensor')
def edit_sensor():
    id = request.args.get('id', None)
    sensor = Sensor.get_single_sensor(id)
    return render_template("update_sensor.html", sensor = sensor)

@sensor_.route('/sensors')
def sensors():
    sensors = Sensor.get_sensors()
    return render_template("sensors.html", sensors = sensors)


@sensor_.route('/add_sensor', methods=['POST'])
def add_sensor():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    topic = request.form.get("topic")
    unit = request.form.get("unit")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, topic, unit, is_active)

    sensors = Sensor.get_sensors()
    return render_template("sensors.html", sensors = sensors)

def update_sensor(id,name, brand, model, topic, unit, is_active):
    device = Device.query.filter(Device.id == id).first()
    sensor = Sensor.query.filter(Sensor.devices_id == id).first()
    if device is not None:
        device.name = name
    device.brand = brand
    device.model = model
    sensor.topic = topic
    sensor.unit = unit
    device.is_active = is_active
    db.session.commit()
    return Sensor.get_sensors()


@sensor_.route('/del_sensor', methods=['GET'])
def del_sensor():
    id = request.args.get('id', None)
    sensors = Sensor.delete_sensor(id)
    return render_template("sensors.html", sensors = sensors)

