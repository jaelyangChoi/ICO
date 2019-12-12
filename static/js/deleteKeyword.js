//선택 키워드 삭제하여 리로드
function deleteKeyword(keyword) {
    console.log(keyword);
    submitByPost("/delete_keyword", 'keyword', keyword);
}

//data를 서버로 전송
function submitByPost(action, name, data) {
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', action);
    document.charset = "utf-8";
    var hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', name);
    hiddenField.setAttribute('value', data);
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
}
