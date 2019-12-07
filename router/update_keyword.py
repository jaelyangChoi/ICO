from flask import Blueprint, request, jsonify, session

from DB.DAO.personalKeyword import PersonalKeywordDAO

update_keyword_bp = Blueprint('update_keyword', __name__)

# 키워드db클래스 생성
personal_keywordDB = PersonalKeywordDAO()


# 입력 받은 DB에 전송 후 키워드 리로드
@update_keyword_bp.route('/update_keyword', methods=['POST'])
def update_keyword():
    user_info = session['info']

    # db에 추출한 keyword, id 넣기
    personal_keywordDB.insert_keyword(user_info['id'], request.form['keyword'])

    # id가 cjl0701인 키워드 전부 출력
    keywords = personal_keywordDB.select_keywords(user_info['id'])

    # 키워드를 string으로
    keywords_str = ', '.join(keywords)

    return jsonify(keywords_str)
