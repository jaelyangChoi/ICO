from flask import Blueprint, request, jsonify, session, url_for
from DB.DAO.comment import CommentDAO
from DB.DAO.personal_keyword import PersonalKeywordDAO
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

    print("url: " + url_for('news'))
    print(request.url)
    print("id:" + user_info['id'])
    print(new_comment)
    # 댓글 적절성 판단
    properness_judge(new_comment)

    print(new_comment)
    # db에 댓글 insert -> 예외처리
    add_comment_to_DB(new_comment)

    # 전체 댓글 리로드 -> 함수화
    comment_objs = CommentDAO.select_comments_by_url(url_for('news'))
    comments = []
    for comment_obj in comment_objs:
        print(comment_obj)
        comments.append(comment_obj.get_data())
    print(comments)

    # 필터링 서비스
    if session['mode'] == 'on':
        comments = filtering(comments)

    return jsonify(comments)

def properness_judge(new_comment):
    result = runBlockComment(new_comment['comment'])
    new_comment['property'] = result

def add_comment_to_DB(new_comment):
    CommentDTO.set_insert_data(new_comment)
    CommentDAO.insert_comment(CommentDTO)
