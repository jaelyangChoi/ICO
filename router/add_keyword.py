from flask import Blueprint, request, jsonify, session
from DB.DAO.personalKeyword import PersonalKeywordDAO

add_keyword_bp = Blueprint('add_keyword', __name__)

# 키워드 db 클래스 생성
personal_keywordDB = PersonalKeywordDAO()


# 입력 받은 DB에 전송 후 키워드 리로드
@add_keyword_bp.route('/add_keyword', methods=['POST'])
def add_keyword():
    user_info = session['info']

    # DB에 키워드 입력
    personal_keywordDB.insert_keyword(user_info['id'], request.form['keyword'])

    # 키워드 전부 출력
    keywords = get_keywords_by_id(user_info['id'])

    return jsonify(keywords)


def get_keywords_by_id(id):
    keywords = personal_keywordDB.select_keywords(id) #리스트 반환
    print(keywords)
    keywords_str = ', '.join(keywords)
    print(keywords_str)
    return keywords
