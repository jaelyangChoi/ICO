# from block import block
import json
import os

from flask import Flask, render_template, request, redirect, url_for
from flask import session

<<<<<<< HEAD
from DB.DAO.comment import CommentDAO
from DB.DAO.personalKeyword import PersonalKeywordDAO
=======
from DAO.comment import CommentDAO
from DB.DAO.personal_keyword import PersonalKeywordDAO
>>>>>>> 02cb37244403d70346eecb46bd7b8958d8896ede
from block.filtering import filtering
from router import test
from router.update_comment import update_comment_bp
from router.update_keyword import update_keyword_bp

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'

app.register_blueprint(update_comment_bp)
app.register_blueprint(update_keyword_bp)
app.register_blueprint(test.route_blue)

comments = [{'userID': 'cjl', 'comment': 'test data'}, ]
keywords = ['sibal', 'byungsin']
mode = 'ICO Service off'

# 키워드 db클래스 생성
personal_keywordDB = PersonalKeywordDAO()


@app.route('/googleCallback')
@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)

    data = json_data['web']
    return render_template('index1.html', cilent_id=data['client_id'])


# DB로부터 댓글과 키워드 받아옴 ->3차필터링 유무
@app.route('/news')
def news():
    user_info = session['info']
    keywords = personal_keywordDB.select_keywords(user_info['id'])
    keywords_str = ', '.join(keywords)

    # 전체 댓글 리로드
    comments = CommentDAO.select_comments_by_url('http://localhost:5000/news')
    # for comment in comments:
    #   print(comment.get_comment()) 반환 값 {'idx': 1, 'text': '왜구들이 미쳐 날뛰네', 'propriety': 0, 'ML_learning': 0, 'url': '', 'writer': '1', 'time': datetime.datetime(2019, 12, 2, 19, 5, 19)}

    # 필터링 서비스
    if session['mode'] == 'on':
        comments = filtering(comments)

    return render_template('news1.html', comments=comments, keywords=keywords_str, mode=session['mode'])


@app.route('/filter_mode', methods=['POST'])
def filter_mode():
    global mode
    mode = request.form['mode']
    return redirect(url_for('news'))


# redirect방식
# @app.route('/commentInput', methods=['POST'])
# def commentInput():
#     new_comment = {"userID": request.form['userID'], "comment": request.form['comment']}
#     comments.append(new_comment)
#     return redirect(url_for('news')) #, code=307 => 원래 전송 된대로 요청 유형을 보존


# form 요소:ImmutableMultiDict([('userID', 'userID'), ('comment', 'zzz\r\n')])


if __name__ == '__main__':
    app.run()
