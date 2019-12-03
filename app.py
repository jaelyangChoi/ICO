import json
import os

from flask import Flask, render_template, request, redirect, url_for
from router import test
from block import block

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'

app.register_blueprint(test.route_blue)


@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)

    data = json_data['web']
    return render_template('index1.html', cilent_id=data['client_id'])


@app.route('/news', methods=["GET", "POST"])
def news():
    keywords = ['sibal', 'byungsin']
    keywordList = ', '.join(keywords)
    # posts = Post.query.all()
    comments = [{'userID': 'cjl', 'comment': 'aaaaaa\n'}]
    if request.method == 'POST':
        new_comment = request.form
        comments.append(new_comment)
    # if request.form['keyword']:
    #     new_keyword = request.form['keywords']
    #     keywords.append(new_keyword)

    return render_template('news1.html', comments=comments, keywords=keywordList)


@app.route('/commentInput', methods=['POST'])
def comment():
    if request.method == 'POST':
        return redirect(url_for('news'), code=307)  # 307은 원래 전송 된대로 요청 유형을 보존


@app.route('/keyword', methods=['POST'])
def keyword():
    # keywords = {'userID': 'cjl', 'keyword': ('sipal', 'pig')}
    keywords = ['sibal', 'byungsin']
    keywords.append(request.form['keyword'])
    keywordList = ', '.join(keywords)
    return render_template('news1.html', keywords=keywordList)


if __name__ == '__main__':
    app.run()
