from flask import Flask, jsonify, request
import json
app = Flask(__name__)


@app.route('/<int:id>', methods=['POST', 'GET'])
def pessoas(id):
    return jsonify({'Id': id, 'nome': 'Rafael', 'profissao': 'desenvolvedor'})


@app.route('/soma/<int:valor1>/<int:valor2>')
def soma(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})


@app.route('/soma', methods=['POST'])
def testebody():
    dados = json.loads(request.data)
    print(dados)
    total = sum(dados['valores'])
    print(request)
    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)
