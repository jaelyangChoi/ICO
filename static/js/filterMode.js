//개인 필터링 mode에 대한 정보를 서버로 전송
function submitByPost(action, mode) {
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', action);
    document.charset = "utf-8";
    var hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', 'mode');
    hiddenField.setAttribute('value', mode);
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
}

//개인 필터 버튼을 클릭하면 버튼의 내용을 바꾸고 서버로 모드 정보 전송
function filterMode(self) {
    if (self.value === 'ICO Service off')
        mode = 'on';

    else
        mode = 'off';
    submitByPost("/filter_mode", mode);
}