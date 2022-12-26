from flask import Flask, session, redirect
from functools import wraps
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = pymongo.MongoClient("mongodb+srv://ahmednasser345:ahmednasser@cluster0.7xscsda.mongodb.net/?retryWrites=true&w=majority")
db = client.test



# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap
  
  



 