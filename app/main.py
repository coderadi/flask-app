from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')


@app.route('/')
def index():
    return 'Hello World'


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8002, threaded=True)
