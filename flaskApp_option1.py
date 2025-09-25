from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Reflect existing database inside application context
with app.app_context():
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)

    # Access the mapped table class
    Driver = Base.classes.drivers
    Vehicle=Base.classes.vehicles

@app.route('/')
def index():
    return "Hello World JONATHAN"

@app.route('/drivers')
def drivers_list():
    drivers = db.session.query(Driver).all()
    html = '<table border="1" style="border-color: blue;">'
    html += "<tr><th>ID</th><th>First Name</th><th>Last Name</th></tr>"
    for driver in drivers:
        html += f"<tr><td>{driver.id}</td><td>{driver.first_name}</td><td>{driver.last_name}</td></tr>"
    html += "</table>"
    return html


@app.route('/vehicles')
def vehicles_list():
    vehicles = db.session.query(Vehicle).all()
    html = "<table border='1'>"
    html += "<tr><th>ID</th><th>Make</th><th>Model</th><th>Driver ID</th></tr>"
    
    for vehicle in vehicles:
        html += f"<tr><td>{vehicle.id}</td><td>{vehicle.make}</td><td>{vehicle.model}</td><td>{vehicle.driver_id}</td></tr>"
    
    html += "</table>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
