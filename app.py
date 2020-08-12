from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def main():
    return 'Hello with flask!'

@app.route('/')
def menu():
    response = "PyApp Demo \n"
    response += "1. Seu numero\n"
    response += "2. Dica do dia\n"
    response += "3. Sair\n"
    return response


if __name__ == "__main__":
    app.run()