from flask import Blueprint

from DB.DAO.comment import CommentDAO
from DB.DAO.personalKeyword import PersonalKeywordDAO
from DB.DTO.comment import Comment
from block.block import Block

update_comment_bp = Blueprint('update_comment', __name__)

personal_keywordDB = PersonalKeywordDAO()
CommentDTO = Comment()
CommentDAO = CommentDAO()

# 댓글 적절성 판단
def properness_judge(new_comment):
    block = Block()
    result = block.runBlockComment(new_comment['comment'])
    print("적절성 : " + result)
    new_comment['property'] = result

# 댓글 필터링
def filtering(comments, keywords):
    block = Block()

    # 개인 키워드 기반 적절성 유무 판단
    block = Block()
    if keywords:
        comments = block.privateKeywordMatch(comments, keywords)  # 딕셔너리 리스트 받음
    # 부적절한 댓글 가리기
    conceal_bad_comment(comments)
    return comments


# 부적절한 댓글 가리기
def conceal_bad_comment(comments):
    # 딕셔너리 리스트
    for comment in comments:
        if comment['property'] == '-':
            comment['comment'] = '부적절한 댓글입니다.'
