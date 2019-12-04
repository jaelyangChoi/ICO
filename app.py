from flask import Flask, render_template, request, redirect, url_for, session
from DB.DAO.comment import CommentDAO
from DB.DAO.personal_keyword import PersonalKeywordDAO
from block.filtering import filtering
from router import test
from router.update_comment import update_comment_bp
from router.update_keyword import update_keyword_bp
import json
import os
app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'

app.register_blueprint(update_comment_bp)
app.register_blueprint(update_keyword_bp)
app.register_blueprint(test.route_blue)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'



# 댓글, 키워드 db클래스 생성
CommentDAO = CommentDAO()
personal_keywordDB = PersonalKeywordDAO()


@app.route('/googleCallback')
@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)
    data = json_data['web']
    return render_template('index.html', cilent_id=data['client_id'])


@app.route('/news')
def news():
    mode =True
    keywords = personal_keywordDB.select_keywords('cjl0701')
    keywords_str = ', '.join(keywords)
    print(keywords_str)
    # 전체 댓글 리로드
    comments = CommentDAO.select_comments_by_url('http://localhost:5000/news')
    # for comment in comments:
    #   print(comment.get_comment()) 반환 값 {'idx': 1, 'text': '왜구들이 미쳐 날뛰네', 'propriety': 0, 'ML_learning': 0, 'url': '', 'writer': '1', 'time': datetime.datetime(2019, 12, 2, 19, 5, 19)}

    # 필터링 서비스
    if session['mode'] == 'on':
        comments = filtering(comments)

    return render_template('news1.html', comments=comments, keywords=keywords_str, mode='on')


@app.route('/filter_mode', methods=['POST'])
def filter_mode():
    session['mode'] = request.form['mode']
    return redirect(url_for('news'))

if __name__ == '__main__':
    app.run()
