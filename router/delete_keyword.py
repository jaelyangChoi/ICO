from flask import Blueprint, request, session, redirect, url_for

from DB.DAO.personalKeyword import PersonalKeywordDAO

delete_keyword_bp = Blueprint('delete_keyword', __name__)

# 키워드 db 클래스 생성
personal_keywordDB = PersonalKeywordDAO()


# 입력 받은 DB에 전송 후 키워드 리로드
@delete_keyword_bp.route('/delete_keyword', methods=['POST'])
def delete_keyword():
    user_info = session['info']

    # DB에 저장된 키워드 삭제 , parameter, return 값
    personal_keywordDB.delete_keyword(user_info['index'], request.form['keyword'])

    return redirect(url_for('news'))
