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
    return "Index page"

@app.route('/drivers')
def drivers_list():
    # This route is already inside app context, so it's safe
    drivers = db.session.query(Driver).all()
    return "<br>".join(driver.first_name for driver in drivers)

@app.route('/vehicles')
def vehicles_list():
    # This route is already inside app context, so it's safe
    vehicles = db.session.query(Vehicle).all()
    html = "<table border='1'>"
    html += "<tr><th>ID</th><th>Make</th><th>Model</th><th>Driver ID</th></tr>"
    
    for vehicle in vehicles:
        html += f"<tr><td>{vehicle.id}</td><td>{vehicle.make}</td><td>{vehicle.model}</td><td>{vehicle.driver_id}</td></tr>"
    
    html += "</table>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
