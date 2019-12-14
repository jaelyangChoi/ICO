var modal = document.getElementById('Modal');

// 모달창 여는 버튼
var btn = document.getElementById("MDbtn");

// 모달창 닫는 버튼
var close = document.getElementsByClassName("close")[0];

// 모달 열기
btn.onclick = function () {
    modal.style.display = "block";
}

// 모달 닫기
close.onclick = function () {
    modal.style.display = "none";
}

// 모달창 외부 클릭하면 창 닫힘
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
