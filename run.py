from flask import render_template, redirect, url_for, request
from flaskapp import app, login_required
from flaskapp.user.routes import *
from werkzeug.utils import secure_filename
import pandas as pd
import json

# for annotation
import urllib.request
from inscriptis import get_annotated_text, ParserConfig
from inscriptis.annotation.output.html import HtmlExtractor

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/login')
def login_page():
  return render_template('login.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')

@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/scrapped')
def scrapped_page():
  data = pd.read_csv('scraped_tweets.csv')
  return render_template('index.html', tables=[data.to_html()], titles=[''])

@app.route('/collect')
def collect_page():
  return render_template('collect.html')

@app.route('/search')
def search_page():
  return render_template('search.html')

# @app.route('/annotate')
# def annotate_page():
#   with open('test.html', 'r') as f:
#     html_string = f.read()
#   with open('annotation-profile.json', 'r') as f:
#     rules = json.load(f) 
#   output = get_annotated_text(html_string, ParserConfig(annotation_rules=rules))
#   # HtmlExtractor.__call__(HtmlExtractor, output)
#   # HtmlExtractor._get_label_colors('heading', 'red')
#   return render_template('annotate.html', output=[output])


@app.route('/annotate')
def annotate_page():
  try:
    data = pd.read_csv('scraped_tweets.csv')
    data.rename( columns={'Unnamed: 0':'ID'}, inplace=True ) 
  except:
    return redirect(url_for('dashboard'))
  tweets:list = data.to_dict('list')
  return render_template('annotate.html', tweets=tweets)


@app.route('/annotate/upload', methods = ['POST','GET'])
def annotate_upload():
  if request.method == 'POST':
    tweets: list = []
    upload_file = request.files['upload_file']

    if upload_file.filename != '':
      upload_file.save(secure_filename('uploaded_tweets.csv'))
      
      try:
        data = pd.read_csv('uploaded_tweets.csv')
        data.rename( columns={'Unnamed: 0':'ID'}, inplace=True )     
        tweets = data.to_dict('list')
      except:
        return render_template('annotate.html', error='Unsupported file format! Try again.')

    return render_template('annotate.html', tweets=tweets)
  

if __name__ == '__main__':
  app.run(host = "0.0.0.0",port = 3000, debug=True)