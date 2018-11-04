from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__) ##__name__ pega nome do diretorio atual


@app.route('/')
def index():
    return render_template('index.html')
   # return 'hello world'

@app.route('/api')
def minha_api():
    mensagem = {"mensagem": "api rest"}
    return jsonify(mensagem)

@app.route('/cep/<string:busca>')
def buscar_cep(busca):
    data = requests.get('https://viacep.com.br/ws/{}/json/'.format(busca))
    return jsonify(data.json())

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)