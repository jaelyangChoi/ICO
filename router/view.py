
from flask import Flask, Blueprint, render_template

view_blueprint = Blueprint('view', __name__ )
@view_blueprint.route('/googleCallback')
@view_blueprint.route('/')
def index():
   return render_template('index.html')


@view_blueprint.route('/news')
def news():
    #posts = Post.query.all()
    #return render_template('news1.html')
    return "hello"
