from flask import Flask, request, jsonify, redirect, url_for
import json


app = Flask(__name__, static_folder='../', template_folder='../')

PASSWORD = 'qwertyuiop123'

@app.route('/login', methods=['POST'])
def login():
    password = request.json.get('password')
    if password == PASSWORD:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401

@app.route('/diaries.html')
def diaries_page():

    return '------'

if __name__ == '__main__':
    app.run(debug=True)
