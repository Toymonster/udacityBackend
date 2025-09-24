from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from markupsafe import escape

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost:5432/test'

db = SQLAlchemy(app)

# homepage
@app.route('/')
def index():
    return "Index page"

@app.route('/hello')
def hello():
    return "hello world"

@app.route('/drivers')
def drivers_list():
    drivers=db.session.execute(db.select(drivers)).scalars()
    

if __name__=='__main__':
    app.debug=True
    app.run(host="0.0.0.0")