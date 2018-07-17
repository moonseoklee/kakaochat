# -*- coding: utf-8 -*-
import time
import os
from flask import Flask, request, jsonify
import request


# Retrieve HTTP meta-data

def urldown(content):
	app = Flask(__name__)
	now = time.localtime()
	print('urldown')
	# 파일 저장할 폴더 경로
	VOICE_PATH = os.path.join(os.path.dirname(__file__), "voice")

	# 폴더가 없으면 만들어준다
	if not os.path.exists(VOICE_PATH):
		os.makedirs(VOICE_PATH)

	url = content

	r = requests.get(url)

	rename = "%04d%02d%02d-%02d%02d%02d.flac" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

	with open(os.path.join(IMAGE_PATH, rename), 'wb') as f:
		f.write(r.content)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["대화하기", "도움말"]
    }
    return jsonify(dataSend)
 
@app.route('/message', methods=['POST'])
def Message():
	dataReceive = request.get_json()
	content = dataReceive['content']
	
	
	if content == u"대화하기":
		dataSend = {
			"message": {
				"text": "말을 해주세요!"
			}
		}
	elif content == u"도움말":
		dataSend = {
			"message": {
				"text": "..."
			}
		}
	else:
		dataSend = {
			"message": {
				"text": content
			}
		}
		urldown(content)
	
	return jsonify(dataSend)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000)


