from flask import Flask, render_template, Blueprint, request, redirect,url_for, jsonify

from router.update import update_bp
from router import test
# from block import block
# from router import test

app = Flask(__name__, template_folder="templates")

app.register_blueprint(update_bp)
app.register_blueprint(test.route_blue)
# app.register_blueprint(db_connection.db_blue)
# app.register_blueprint(block.block_blue)

comments = [{'userID': 'cjl', 'comment': 'test data'},]
keywords = ['sibal', 'byungsin']


@app.route('/googleCallback')
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/news', methods=["GET", "POST"])
def news():
    # posts = Post.query.all()
    keywordStr = ', '.join(keywords)
    return render_template('news1.html', comments=comments, keywords=keywordStr)

#redirect방식
# @app.route('/commentInput', methods=['POST'])
# def commentInput():
#     new_comment = {"userID": request.form['userID'], "comment": request.form['comment']}
#     comments.append(new_comment)
#     return redirect(url_for('news')) #, code=307 => 원래 전송 된대로 요청 유형을 보존



#form 요소:ImmutableMultiDict([('userID', 'userID'), ('comment', 'zzz\r\n')])

if __name__ == '__main__':
    app.run()
