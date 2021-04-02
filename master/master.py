from flask import Flask
import requests


PORT = "8080"
app = Flask(__name__)


@app.route('/myapi/<name>')
def get_data(name):
    requests.get(f'http://127.0.0.1:8000/api/{name}')
    return f"{requests.get(f'http://127.0.0.1:5000/api/info/{name}').text}"


app.run(port=PORT)
