//새로운 키워드를 추가하여 리로드
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

//선택 키워드 삭제하여 리로드
function deleteKeyword(keyword) {
    //parameter로 받은 keyword를 ajax에 인자로 줘서 data로 전송해야 합니다..
    $.ajax({
        type: 'POST',
        url: '/delete_keyword',
        data: keyword, //서버로 데이터 전송시
        success: reloadKeywords(data)
    })
    // submitByPost("/delete_keyword", keyword); ajax 안 쓸경우
}

function keywordToHTML(keywordList) {
    var keywords = '';
    var i = 0;
    while (i < keywordList.length) {
        keywords = keywords + '<input type="text" class="data" value="' + keywordList[i] +
            '"><input type="button" value="삭제" onclick="deleteKeyword(\'' + keywordList[i] + '\')"> <br>';
        i++;
    }
    return keywords
}


function reloadKeywords(data) {  // 키워드 리스트 넘어옴
    $('#kwInputWindow').val(''); //입력창 초기화
    let keywords = keywordToHTML(data);
    $('#kwOutputWindow').html(keywords); //html로 전송
}