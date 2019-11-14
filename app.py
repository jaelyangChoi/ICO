from flask import Flask, render_template, Blueprint, request, redirect,url_for
from block import block
from dao import db_connection

app = Flask(__name__, template_folder="templates")
# app.register_blueprint(db_connection.db_blue)
# app.register_blueprint(block.block_blue)


@app.route('/')
def index():
    return render_template('index')


@app.route('/news')
def news():
    return render_template('news1.html')

@app.route('/commentInput', methods=['POST'])
def comment():
    if request.method == 'POST':
        form = request.form

    return redirect(url_for('news', form=form))


if __name__ == '__main__':
    app.run()
