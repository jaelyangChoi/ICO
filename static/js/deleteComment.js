function deleteComment(commentIndex) {
    // alert(commentIndex);
    $.ajax({
        type: 'POST',
        url: '/delete_comment',
        header: {
            "Content-Type": "application/json"
        },
        data: {
            'comment_index': commentIndex
        }, //서버로 댓글 index 전송
        dataType: 'JSON', //서버에서 데이터 전송시
        "success": function reloadComments(data) { //dict list 넘어옴
            let comments = commentToHTML(data);
            $('#cmOutputWindow').html(comments); //html로 전송
        }
    });
}
