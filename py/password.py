from flask import Flask, request, jsonify, redirect, url_for
import json


app = Flask(__name__, static_folder='../', template_folder='../')

# ��������洢�ڻ����������߰�ȫ�������ļ���
PASSWORD = 'qwertyuiop123'  # ��������������룬ʵ��Ӧ����Ӧ��ʹ�ü�������

@app.route('/login', methods=['POST'])
def login():
    password = request.json.get('password')
    if password == PASSWORD:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401

# �ռ�ҳ��·��
@app.route('/diaries.html')
def diaries_page():
    # ����Ӧ������֤�û��Ѿ���¼���߼�
    return '�����ռ�ҳ��'

if __name__ == '__main__':
    app.run(debug=True)
