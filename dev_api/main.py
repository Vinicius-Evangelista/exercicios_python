from flask import Flask, jsonify, request
import json
app = Flask(__name__)


desevolvedores = [
    {'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']},
    {'nome': 'Vinicius',
     'habilidades': ['Flutter', 'Python']}
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def desevolvedor(id):
    if request.method == 'GET':
        desevolvedor = desevolvedores[id]
        return jsonify(desevolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desevolvedores[id] = dados
        return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True)
