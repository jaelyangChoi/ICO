from flask import Flask, render_template
from router import test

app = Flask(__name__, template_folder="templates")

app.register_blueprint(test.route_blue)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
