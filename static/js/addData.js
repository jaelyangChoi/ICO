//새로운 키워드를 반영하여 리로드
function addkeyword() {
    $.ajax({
        type: 'POST',
        url: '/add_keyword',
        data: $('#keywordForm .data'), //서버로 데이터 전송시
        success: function reloadKeywords(data) {  // 키워드 리스트 넘어옴
            $('#kwInputWindow').val(''); //입력창 초기화
            let keywords = keywordToHTML(data);
            $('#kwOutputWindow').html(keywords); //html로 전송
        }
    })
}

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


function keywordToHTML(keywordList) {
    var keywords = '';
    var i = 0;
    while (i < keywordList.length) {
        keywords = keywords + '<input type="text" value="' + keywordList[i] + '"><input type="button" value="삭제" onclick=""><br>';
        i++;
    }
    return keywords
}


function commentToHTML(commentList) {
    var comments = '';
    var i = 0;
    while (i < commentList.length) {
        comments = comments + '<h3>' + commentList[i].userID + '</h3><textarea rows="4" cols="109">' + commentList[i].comment + '</textarea>';
        i++;
    }
    return comments;
}