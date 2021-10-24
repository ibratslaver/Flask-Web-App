#from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from flask_sqlalchemy import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from flask_sqlalchemy import get_debug_queries
from sqlalchemy.orm import Session
from sqlalchemy.orm import create_session
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc

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


base = declarative_base()

engine = create_engine(connect_url)
#base.metadata.create_all(bind = engine)
connection = engine.connect()
metadata = MetaData()


# Map Tables to classes
class Professors(base):
    __table__ = Table('professors', metadata, autoload=True, autoload_with=engine)

class Reviews(base):
    __table__ = Table('reviews', metadata, autoload=True, autoload_with=engine)

class Review_Sentences(base):
     __table__ = Table('review_sentences', metadata, autoload=True, autoload_with=engine)

class Review_Tags(base):
    __table__ = Table('review_tags', metadata, autoload=True, autoload_with=engine)

class Schools(base):
    __table__ = Table('schools', metadata, autoload=True, autoload_with=engine)


# Create session 
Session = sessionmaker(bind = engine)

session = Session()





