from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<p> Mi primera pagina web'
if __name__ == '__main__':
    app.run(deebug=true)