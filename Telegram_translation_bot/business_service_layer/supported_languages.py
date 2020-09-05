from flask import Flask, Response, request
import json

app = Flask(__name__)


supported_languages = {}


@app.route('/list', methods=['GET'])
def retreive_langauge():
	# we retreive the selected destination language by the user 
	supported_languages = json.load(open("languages.json"))
	user_id = request.args['user_id']
	#list_lang = supported_languages[user_id] 
	list_lang = json.dumps(supported_languages)
	return Response('{"retreived":"' + list_lang + '"}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5005)
