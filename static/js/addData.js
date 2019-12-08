//새로운 키워드를 반영하여 리로드
function addkeyword() {
    $.ajax({
        type: 'POST',
        url: '/add_keyword',
        data: $('#keywordForm .data'), //서버로 데이터 전송시
        dataType: 'JSON',// 서버에서 데이터 전송시
        "success": function reloadKeywords (data) {//list 넘어옴
            // $('#kwOutputWindow').val(data);
             $('#kwInputWindow').val('');
            var keywordsHTML = '';
            var i = 0;
            while (i < data.length) { //js에서 배열길이는 length로
                keywordsHTML = keywordsHTML + '<input type="text" value="' + data[i] + '"><input type="button" value="삭제"><br>';
                i++;
                console.log(keywordsHTML)
            }
            $('#kwOutputWindow').html(keywordsHTML);
        }
    })
}

//새로운 댓글을 반영하여 리로드
function addComment() {
    $.ajax({
        type: 'POST',
        url: '/add_comment',
        data: $('#commentForm .data'), //서버로 데이터 전송시
        dataType: 'JSON',// 서버에서 데이터 전송시
        "success": function reloadComments (data) {//dict list 넘어옴
            $('#cmInputWindow').val('');
            var comments = '';
            var i = 0;
            while (i < data.length) {
                comments = comments + '<h3>' + data[i].userID + '</h3><textarea rows="4" cols="109">' + data[i].comment + '</textarea>';
                i++;
            }
            $('#cmOutputWindow').html(comments);
        }
    })
}