from DB.DAO.personalKeyword import PersonalKeywordDAO
from flask import Blueprint, request, jsonify

update_keyword_bp = Blueprint('update_keyword', __name__)

# 키워드db클래스 생성
personal_keywordDB = PersonalKeywordDAO()

keywords = ['sibal', 'byungsin']


# 이런 형식으로 함수 호출
def print_kw(str):
    print(str)


# 입력 받은 DB에 전송 후 키워드 리로드
@update_keyword_bp.route('/update_keyword', methods=['POST'])
def update_keyword():
    # db에 추출한 keyword, id 넣기
    personal_keywordDB.insert_keyword('abc', request.form['keyword'])
    keywords = personal_keywordDB.select_keywords('abc')

    keywords_str = ', '.join(keywords)

    print_kw(keywords_str)

    return jsonify(keywords_str)
