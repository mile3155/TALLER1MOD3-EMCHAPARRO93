from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from db import db, init_db
from models import Perro, Cuidador
from controllers.controller import user_blueprint

app = Flask(__name__,template_folder="views")
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root:@localhost:3306/'

db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def index():
    lassie = Perro.query.filter_by(nombre='Lassie').count()
    mario = Perro.query.filter_by(id=2).all()
    return render_template('index.html',lassie=lassie, mario=mario)

if __name__=='__main__':
    app.run(debug=True)