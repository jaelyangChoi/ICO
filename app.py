import json
import os

from flask import Flask, render_template, url_for, session

from router import login
from router.comment.add_comment import add_comment_bp, load_comments_from_DB
from router.comment.delete_comment import delete_comment_bp
from router.filtering.filter_mode import mode_info, filter_mode_bp
from router.filtering.filtering import filtering
from router.keyword.add_keyword import add_keyword_bp, get_keywords_by_id
from router.keyword.delete_keyword import delete_keyword_bp
from router.test import test_blue

app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'

app.register_blueprint(delete_comment_bp)
app.register_blueprint(delete_keyword_bp)
app.register_blueprint(filter_mode_bp)
app.register_blueprint(add_comment_bp)
app.register_blueprint(add_keyword_bp)
app.register_blueprint(login.login_blue)

# 테스트를 위한 router
app.register_blueprint(test_blue)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)

    data = json_data['web']
    return render_template('index.html', client_id=data['client_id'])


# news page rendering
@app.route('/news')
def news():
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
