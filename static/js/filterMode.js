//개인 필터 버튼을 클릭하면 버튼의 내용을 바꾸고 서버로 모드 정보 전송
function filterMode(self) {
    var mode = ChangeMode(self);
    submitByPost("/filter_mode", 'mode', mode);
}

/**
 * @return {string}
 */
function ChangeMode(self) {
    if (self.value === 'ICO Service 켜기') {
        self.value = 'ICO Service 끄기';
        return 'on';
    }
    else{
        self.value = 'ICO Service 켜기';
        return 'off';
    }
}

// //data를 서버로 전송
// function submitModeInfo(action, data) {
//     var form = document.createElement('form');
//     form.setAttribute('method', 'post');
//     form.setAttribute('action', action);
//     document.charset = "utf-8";
//     var hiddenField = document.createElement('input');
//     hiddenField.setAttribute('type', 'hidden');
//     hiddenField.setAttribute('name', 'mode');
//     hiddenField.setAttribute('value', data);
//     form.appendChild(hiddenField);
//     document.body.appendChild(form);
//     form.submit();
// }
