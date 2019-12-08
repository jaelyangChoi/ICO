from flask import Flask, render_template, request, redirect, url_for, session
from DB.DAO.comment import CommentDAO
from DB.DAO.personalKeyword import PersonalKeywordDAO
from block.filtering import filtering
from router import test
from router.add_comment import add_comment_bp
from router.add_keyword import add_keyword_bp, get_keywords_by_id
import json
import os

app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'

app.register_blueprint(add_comment_bp)
app.register_blueprint(add_keyword_bp)
app.register_blueprint(test.route_blue)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# 댓글, 키워드 db클래스 생성
CommentDAO = CommentDAO()
personal_keywordDB = PersonalKeywordDAO()


@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)
    data = json_data['web']

    return render_template('index.html', cilent_id=data['client_id'])


@app.route('/news')
def news():
    mode = mode_info()
    user_info = session['info']

    # DB에서 키워드 get
    keywords = get_keywords_by_id(user_info['id'])

    # 전체 댓글 리로드 -> 함수화
    comment_objs = CommentDAO.select_comments_by_url(url_for('news'))
    comments = []
    for comment_obj in comment_objs: #객체 리스트
        print(comment_obj) #객체
        comments.append(comment_obj.to_json())
    print(comments)

    # 필터링 서비스
    if session['mode'] == 'on':
        comments = filtering(comments)

    return render_template('news1.html', comments=comments, keywords=keywords, mode=mode)


@app.route('/filter_mode', methods=['POST'])
def filter_mode():
    session['mode'] = request.form['mode']
    return redirect(url_for('news'))

def mode_info():
    if session['mode'] == 'off':
        return 'ICO Service off'
    else:
        return 'ICO Service on'

if __name__ == '__main__':
    app.run()
