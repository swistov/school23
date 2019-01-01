from flask import Flask

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_key'
)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'DFA'


if __name__ == '__main__':
    app.run()
