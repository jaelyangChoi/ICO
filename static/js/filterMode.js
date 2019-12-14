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

