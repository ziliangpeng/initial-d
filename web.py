from flask import Flask, request
from interpreter import interpret

app = Flask(__name__)


@app.route('/')
def hello():
    return "Dark\n"


@app.route('/run', methods=['POST'])
def run():
    program = request.get_data().decode('utf-8')
    return interpret(program)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=922)
