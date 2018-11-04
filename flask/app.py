from flask import Flask, jsonify, render_template


app = Flask(__name__) ##__name__ pega nome do diretorio atual


@app.route('/')
def index():
    return 'hello world'

@app.route('/api')
def minha_api():
    mensagem = {"mensagem": "api rest"}
    return jsonify(mensagem)


if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)