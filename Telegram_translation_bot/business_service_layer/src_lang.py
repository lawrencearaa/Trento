from flask import Flask, Response, request
import json

app = Flask(__name__)


users_pref = {}


@app.route('/language', methods=['POST'])
def store_langauge():
	# let's take the source lanuage from the user
	user_id = request.form['user_id']
	src_lang = request.form['src_lang']
	users_pref[user_id] = src_lang
	return Response('{"status":"OK"}', status=200, mimetype='application/json')


@app.route('/language', methods=['GET'])
def retreive_langauge():
	# we retreive the selected source language by the user 
	user_id = request.args['user_id']
	src_lang = users_pref[user_id] 
	return Response('{"retreived":"' + src_lang + '"}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5004)

