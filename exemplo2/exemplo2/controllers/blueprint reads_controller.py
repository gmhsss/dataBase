#reads_controller.py
from flask import Blueprint, request
from models.iot.read import Read
read = Blueprint("read",__name__, template_folder="views")