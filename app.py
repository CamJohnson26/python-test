from flask import Flask

app = Flask(__name__)

def factorial(param: object):
    if param == 1:
        return 1
    else:
        return param * factorial(param - 1)


@app.route('/')
def hello_world():  # put application's code here
    """Return a friendly HTTP greeting.

Returns:
    str: A friendly HTTP greeting.
    """
    return factorial(5)  

if __name__ == '__main__':
    app.run()
