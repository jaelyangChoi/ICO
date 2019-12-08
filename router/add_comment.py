from flask import Blueprint, request, jsonify, session, url_for
from DB.DAO.comment import CommentDAO
from DB.DAO.personalKeyword import PersonalKeywordDAO
from DB.DTO.comment import Comment
from block.block import runBlockComment
from block.filtering import filtering

add_comment_bp = Blueprint('add_comment', __name__)

personal_keywordDB = PersonalKeywordDAO()
CommentDTO = Comment()
CommentDAO = CommentDAO()


# 입력받은 댓글 db에 업로드 후 리로드
@add_comment_bp.route('/add_comment', methods=['POST'])
def add_comment():
    # 유저 정보 추출
    user_info = session['info']

    # 입력된 댓글 추출
    new_comment = {'userID': user_info['id'],
                   'comment': request.form['comment'],
                   'property': '+',
                   'url': url_for('news')}

    # 댓글 적절성 판단 (level_1)
    properness_judge(new_comment)

    # db에 댓글 insert -> 예외처리
    add_comment_to_DB(new_comment)

    # 전체 댓글 리로드
    comments = load_comments_from_DB(url_for('news'))

    # 필터링 서비스(level_2,3)
    if session['mode'] != 'off':
        comments = filtering(comments)

    return jsonify(comments)


def properness_judge(new_comment):
    result = runBlockComment(new_comment['comment'])  # level에 따른 필터링, mode값 인자로 전달할 것.
    new_comment['property'] = result


def add_comment_to_DB(new_comment):
    CommentDTO.set_insert_data(new_comment)
    try:
        CommentDAO.insert_comment(CommentDTO)
    except Exception:
        return 'DB에 댓글 입력 오류'


def load_comments_from_DB(url):
    comment_objs = CommentDAO.select_comments_by_url(url)
    comments = []
    for comment_obj in comment_objs:  # 객체 리스트
        comments.append(comment_obj.to_json())  # 딕셔너리화
    return comments
