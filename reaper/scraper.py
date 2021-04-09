import requests
from flask import Flask

PORT = "8000"
app = Flask(__name__)


@app.route('/api/<name>')
def get_info_btc(name):
    req = requests.get(f'https://api.coingecko.com/api/v3/coins/{name}').json()
    price_usd = req['market_data']['current_price']['usd']
    requests.get(f'http://keeper:5000/api/update/{name}/{price_usd}')
    return f'{name}: {price_usd}'


app.run(host='0.0.0.0', port=PORT)
