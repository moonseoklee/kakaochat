# -*- coding: utf-8 -*-
 
#---------------------------------
# pangpang2.py
#---------------------------------
 
import os
from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["팡팡이와 대화하기!", "도움말"]
    }
    return jsonify(dataSend)
 
@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"팡팡이와 대화하기!":
        dataSend = {
            "message": {
                "text": "팡팡이 명령어 목록!\n1. 도움말\n2. 안녕!\n3. 저기요~"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "이제 곧 정식 버전이 출시될거야. 조금만 기다려~~~"
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message": {
                "text": "안녕~~ 반가워 ㅎㅎ"
            }
        }
    elif u"저기" in content:
        dataSend = {
            "message": {
                "text": "볼일 끝났으면 썩 꺼져!"
            }
        }
    else:
        dataSend = {
            "message": {
                "text": content
            }
        }
    return jsonify(dataSend)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000)


