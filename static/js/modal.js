// 모달창 요소
var modal = document.getElementById('Modal');

// 모달창을 여는 버튼 요소
var btn = document.getElementById("MDbtn");

// 모달창 닫는 요소
var close = document.getElementsByClassName("close")[0];

//모달창 여는 버튼 클릭했을 때
btn.onclick = function () {
    modal.style.display = "block";
}

//모달창 닫는 버튼 클릭했을 때
close.onclick = function () {
    modal.style.display = "none";
}

//모달창 밖을 클릭 했을때 모달창 닫는 함수
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
