from flask import Flask, request
from interpreter import interpret
from errors import *

app = Flask(__name__)


@app.route('/')
def hello():
    return "Dark\n"


@app.route('/run', methods=['POST'])
def run():
    program = request.get_data().decode('utf-8')
    try:
        return str(interpret(program)), 200
    except InvalidStatementException:
        return "Invalid statements", 400
    except NoReturnExceptioon:
        return "Should contain at least 1 return statements", 400
    except VariableNotDefined:
        return "Invalid variable", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=922)
