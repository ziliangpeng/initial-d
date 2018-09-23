from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Dark\n"


@app.route('/run', methods=['POST'])
def run():
    return request.get_data()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=922)
