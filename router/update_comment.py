from flask import Flask, Blueprint, render_template, request, jsonify
from block import block
#from app import mode
update_comment_bp = Blueprint('update_comment', __name__)


#댓글 받아서 필터링 함수 호출->return값을 DB에 전달하고 웹에 전달

#임시 db
comments = [{'userID': 'cjl', 'comment': 'test data'}]

def print_cm(str):
    print(str)

@update_comment_bp.route('/update_comment', methods=['POST'])
def update_comment():
    #입력된 댓글 추출
    new_comment = {"userID": request.form['userID'], "comment": request.form['comment']}

    # 임시 테스트
    #print_cm(new_comment)


    ##댓글을 필터링
    filtered_str = block.runBlockComment(new_comment['comment'])
    new_comment['comment']=filtered_str
    comments.insert(0, new_comment)  # 이 과정 대신에 DB에 댓글 입력
    #받은 리턴값을 DB에 보냄

    #DB에서 댓글 전체 가져옴

    #만약 개인 필터링 모드가 on 이라면
    #global mode
    #print(mode)
      #개인 키워드를 DB에서 가져오고
      #3차 필터링 함수 호출하여 comments에 담음

    return jsonify(comments)


