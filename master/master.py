from flask import Flask
import requests


PORT = "8080"
app = Flask(__name__)


@app.route('/master_api/<name>')
def get_data(name):
    requests.get(f'http://reaper:8000/api/{name}')
    return f"{requests.get(f'http://keeper:5000/api/info/{name}').text}"


app.run(host='0.0.0.0', port=PORT)
