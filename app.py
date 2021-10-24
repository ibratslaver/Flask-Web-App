from flask import Flask, render_template, request
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import sqlalchemy
from flask_wtf import FlaskForm
from wtforms import SelectField
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, create_engine, engine
import pyodbc
from sqlalchemy.orm import sessionmaker

SECRET_KEY = 'Igor12345'

credentials = {
    'username': 'Igor',
    'password': 'NA',
    'host': 'NA',
    'database': 'ratemyprofessor',
    'port': '1433'}

connect_url = sqlalchemy.engine.url.URL(
    'mssql+pyodbc',
    username=credentials['username'],
    password=credentials['password'],
    host=credentials['host'],
   	port=credentials['port'],
    database=credentials['database'],
    query=dict(driver='SQL Server'))	

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = connect_url
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
metadata = MetaData()

#Map Tables to classes
class Professors(db.Model):
    __table__ = Table('professors', metadata, autoload=True, autoload_with=db.engine)

class Reviews(db.Model):
    __table__ = Table('reviews', metadata, autoload=True, autoload_with=db.engine)

class Schools(db.Model):
    __table__ = Table('schools', metadata, autoload=True, autoload_with=db.engine)

class SalesTable(db.Model):
    __table__ = Table('sales_table', metadata, autoload=True, autoload_with=db.engine)

class Form(FlaskForm):
	region = SelectField('Region', choices = ['North', 'South'])


@app.route("/")
def home():
	departments = db.session.query(Professors.department).distinct().limit(10)
	departments = [department[0] for department in departments]
	department = request.args.get('department')
	print(department)
	result_set = db.session.query(Professors.professor_id, Professors.professor_name, Professors.department).filter(Professors.department == department).limit(20)
	#print(department)
	return render_template("about.html", title = 'About', departments = departments, result_set = result_set)
if __name__ == '__main__':
	app.run(debug = True)
