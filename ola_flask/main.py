from flask import Flask

app = Flask(__name__)


@app.route("/<numero>", methods=['POST'])
def ola(numero):
    return 'Olá Mundo {numero}'.format(numero=numero)


if __name__ == "__main__":

    app.run()
