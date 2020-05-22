// @ts-nocheck

function validate() {
    const password = document.getElementById("password").value;
    if (password == "123") {
        document.getElementById("entirePage").style.display = "inline";
        document.getElementById("validdd").style.display = "none";
        // location.reload();

    } else {
        alert("비밀번호를 물어보세여 ㅎㅎ");
    }
}