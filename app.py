from flask import Flask, render_template
from block import block
from dao import db_connection


app = Flask(__name__, template_folder="templates")
app.register_blueprint(block.block_print)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
