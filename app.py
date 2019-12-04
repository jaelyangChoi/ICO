from flask import Flask, render_template, request, redirect, url_for, session
from router.update_comment import update_comment_bp
from router.update_keyword import update_keyword_bp
from DB.DAO.comment import CommentDAO
from DB.DAO.personal_keyword import PersonalKeywordDAO
from block.filtering import filtering
import json
import os

app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'
app.register_blueprint(update_comment_bp)
app.register_blueprint(update_keyword_bp)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# 임시 댓글, 키워드
# comments = [{'userID': session['id'], 'comment': 'test data'},]
# keywords = ['sibal', 'byungsin']

# 댓글, 키워드 DB 클래스 생성
CommentDAO = CommentDAO()
personal_keywordDB = PersonalKeywordDAO()


@app.route('/googleCallback')
@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)
    data = json_data['web']
    return render_template('index.html', cilent_id=data['client_id'])


# DB 로부터 댓글과 키워드 받아와 필터링해 반환
@app.route('/news')
def news():
    # if session['mode'] == True:
    #     mode = 'ICO Service on'
    # else:
    #     mode = 'ICO Service off'

    keywords = personal_keywordDB.select_keywords(session['id'])
    keywords_str = ', '.join(keywords)
    print(keywords_str)

    # 전체 댓글 리로드
    comments = CommentDAO.select_comments_by_url(url_for('news'))
    # for comment in comments:
    #   print(comment.get_comment()) 반환 값 {'idx': 1, 'text': '왜구들이 미쳐 날뛰네', 'propriety': 0, 'ML_learning': 0, 'url': '', 'writer': '1', 'time': datetime.datetime(2019, 12, 2, 19, 5, 19)}

    # 필터링 서비스
    if session['mode'] == True:
        comments = filtering(comments)

    return render_template('news1_pre.html', comments=comments, keywords=keywords_str, mode=mode)

#ICO Service on/off 여부를 받는 함수
@app.route('/filter_mode', methods=['POST'])
def filter_mode():
    if request.form['mode'] == 'ICO Service on':
        session['mode'] = True
    else:
        session['mode'] = False
    return redirect(url_for('news'))


if __name__ == '__main__':
    app.run()
