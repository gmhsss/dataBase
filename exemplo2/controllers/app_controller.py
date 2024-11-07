#app_controller.py
from flask import Flask, render_template, request
from models.db import db, instance
from controllers.sensors_controller import sensor_
from controllers.actuators_controller import actuator_

def create_app():
    app = Flask(__name__,
                template_folder="./views/",
                static_folder="./static/",
                root_path="./")
    
    
    app.register_blueprint(sensor_, url_prefix='/')
    app.register_blueprint(actuator_, url_prefix='/')
    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)
    
    @app.route('/')
    def index():
        return render_template("home.html")
    
    return app
