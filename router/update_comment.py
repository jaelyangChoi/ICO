from flask import Blueprint, request, jsonify, session, url_for
from DB.DAO.comment import CommentDAO
from DB.DAO.personal_keyword import PersonalKeywordDAO
from DB.DTO.comment import Comment
from block.block import runBlockComment
from block.filtering import filtering

update_comment_bp = Blueprint('update_comment', __name__)

personal_keywordDB = PersonalKeywordDAO()
CommentDTO = Comment()
CommentDAO = CommentDAO()


# 입력받은 댓글 db에 업로드 후 리로드
@update_comment_bp.route('/update_comment', methods=['POST'])
def update_comment():
    user_info = session['info']

    # 입력된 댓글 추출
    new_comment = {'userID': user_info['id'],
                   'comment': request.form['comment'],
                   'property': '+',
                   'url': url_for('news')}

    # 댓글 적절성 판단
    result = runBlockComment(new_comment['comment'])
    new_comment['property'] = result

    # db에 댓글 insert
    CommentDTO.set_insert_comment(new_comment)
    CommentDAO.insert_comment(CommentDTO)

    # 전체 댓글 리로드
    comments = CommentDAO.select_comments_by_url(url_for('news'))

    # 필터링 서비스
    if session['mode'] == 'on':
        comments = filtering(comments)

    return jsonify(comments)
