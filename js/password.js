function login() {
    var password = document.getElementById('password').value;
    // �������뵽������������֤...
    // ������֤ʧ��
    clearAndShake();
}

function clearAndShake() {
    // ������������
    var passwordInput = document.getElementById('password');
    passwordInput.value = '';

    // ��Ӷ���Ч��
    passwordInput.classList.add('shake');

    // ����Ч����ɺ��Ƴ���
    passwordInput.addEventListener('animationend', function () {
        passwordInput.classList.remove('shake');
    }, { once: true });
}

document.getElementById('password').addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        login();
    }
});
