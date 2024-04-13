from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    # todo show headers + ip + data information
    return 'Ahoj!'

