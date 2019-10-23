from flask import Flask, render_template
import requests, json
from pprint import pprint
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

payload = {
    'country' : 'US'

}

endpoint = 'https://api.openaq.org/v1/cities'
@app.route('/')
def main():
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()

    except:
        print('please try again')
    return data
