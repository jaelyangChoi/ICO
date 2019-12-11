//새로운 댓글을 반영하여 리로드
function addComment() {
    $.ajax({
        type: 'POST',
        url: '/add_comment',
        data: $('#commentForm .data'), //서버로 데이터 전송시
        dataType: 'JSON', //서버에서 데이터 전송시
        "success": function reloadComments(data) { //dict list 넘어옴
            $('#cmInputWindow').val(''); //입력창 초기화
            let comments = commentToHTML(data);
            $('#cmOutputWindow').html(comments); //html로 전송
        }
    })
}

function deleteComment(commentindex) {
    alert(commentindex);
    $.ajax({
        type: 'POST',
        url: '/delete_comment',
        header:{
            "Content-Type": "application/json"
        },
        data: {
            'comment_index' : commentindex
        }, //서버로 댓글 딕셔너리 전송
        dataType: 'JSON', //서버에서 데이터 전송시
        "success": function reloadComments(data) { //dict list 넘어옴
            let comments = commentToHTML(data);
            $('#cmOutputWindow').html(comments); //html로 전송
        }
    });
}


function commentToHTML(commentList) {
    var comments = '';
    var i = 0;
    while (i < commentList.length) {
        comments = comments + '<strong>' + commentList[i].userID + '</strong><button onclick="deleteComment(\'' + commentList[i] + '\')">삭제</button><br><textarea rows="4" cols="109">' + commentList[i].comment + '</textarea><br>';
        i++;
    }
    return comments;
}
