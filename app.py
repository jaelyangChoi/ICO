from flask import Flask, render_template, request, redirect, url_for, session
from DB.DAO.comment import CommentDAO
from DB.DAO.personalKeyword import PersonalKeywordDAO
from filtering.filtering import filtering
from filtering.filter_mode import mode_info,filter_mode_bp
from router import login, test
from router.add_comment import add_comment_bp, load_comments_from_DB
from router.add_keyword import add_keyword_bp, get_keywords_by_id
import json
import os

from router.delete_keyword import delete_keyword_bp

app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'
app.register_blueprint(delete_keyword_bp)
app.register_blueprint(filter_mode_bp)
app.register_blueprint(add_comment_bp)
app.register_blueprint(add_keyword_bp)
app.register_blueprint(login.login_blue)
app.register_blueprint(test.test_blue)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# 댓글, 키워드 db 클래스 생성
CommentDAO = CommentDAO()
personal_keywordDB = PersonalKeywordDAO()


@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)
    data = json_data['web']

    return render_template('index.html', client_id=data['client_id'])


@app.route('/news')
def news():
    # mode = mode_info()
    user_info = session['info']

    # DB 에서 키워드 get
    keywords = get_keywords_by_id(user_info['index'])

    # 전체 댓글 리로드
    comments = load_comments_from_DB(url_for('news'))

    # 필터링 서비스
    if session['mode'] != 'off':
        comments = filtering(comments, keywords)

    return render_template('news1.html', comments=comments, keywords=keywords, mode=mode_info())

if __name__ == '__main__':
    app.run()
