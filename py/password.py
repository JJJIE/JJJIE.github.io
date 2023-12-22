from flask import Flask, request, jsonify, redirect, url_for
import json


app = Flask(__name__, static_folder='../', template_folder='../')

# 假设密码存储在环境变量或者安全的配置文件中
PASSWORD = 'qwertyuiop123'  # 这里设置你的密码，实际应用中应该使用加密密码

@app.route('/login', methods=['POST'])
def login():
    password = request.json.get('password')
    if password == PASSWORD:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401

# 日记页面路由
@app.route('/diaries.html')
def diaries_page():
    # 这里应该有验证用户已经登录的逻辑
    return '这是日记页面'

if __name__ == '__main__':
    app.run(debug=True)
