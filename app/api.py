from flask import Flask

app = Flask(__name__)

# TODO: load env variables

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def hello_world():
    """
    Firt things first...
    """
    return "Hello World!"