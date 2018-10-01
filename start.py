from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return input('dfsd: ')


if __name__ == '__main__':
    app.run()
