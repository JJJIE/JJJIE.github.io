function login() {
    var password = document.getElementById('password').value;
    // 发送密码到服务器进行验证...
    // 假设验证失败
    clearAndShake();
}

function clearAndShake() {
    // 清除密码输入框
    var passwordInput = document.getElementById('password');
    passwordInput.value = '';

    // 添加抖动效果
    passwordInput.classList.add('shake');

    // 抖动效果完成后移除类
    passwordInput.addEventListener('animationend', function () {
        passwordInput.classList.remove('shake');
    }, { once: true });
}

document.getElementById('password').addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        login();
    }
});
