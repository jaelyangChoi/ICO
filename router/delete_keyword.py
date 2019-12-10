from flask import Blueprint, request, jsonify, session, redirect, url_for
from DB.DAO.personalKeyword import PersonalKeywordDAO
from router.add_keyword import get_keywords_by_id

delete_keyword_bp = Blueprint('delete_keyword', __name__)

# 키워드 db 클래스 생성
personal_keywordDB = PersonalKeywordDAO()


# 입력 받은 DB에 전송 후 키워드 리로드
@delete_keyword_bp.route('/delete_keyword', methods=['POST'])
def delete_keyword():
    print('키워드 삭제 url')
    user_info = session['info']
    print(request.form)
    # DB에 저장된 키워드 삭제 , parameter, return 값
    personal_keywordDB.delete_keyword(user_info['index'], request.form)

    # 키워드 전부 출력
    keywords = get_keywords_by_id(user_info['index'])

    #return redirect(url_for('news')) ajax 안쓰고 리다이렉트 할 경우
    return jsonify(keywords)


