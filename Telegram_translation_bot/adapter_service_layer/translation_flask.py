from flask import Flask, Response, request
from googletrans import Translator
import json

app = Flask(__name__)
translator = Translator()


@app.route('/translate', methods=['POST'])
def translate():
	# let's take the text to translate from the parameters from english to another language
	text = request.form['text']
	dest_lang = request.form['dest_lang']
	output = translator.translate(text, src=src_lang, dest=dest_lang)
	return Response('{"response":"' + output.text + '"}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
