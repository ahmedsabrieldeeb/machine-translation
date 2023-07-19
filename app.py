import os
import logging

from flask import Flask, render_template, request

from model.model import Translate


# prepare the objects and paths
app = Flask(__name__, template_folder='templates')
html_page_path = "templates/index.html"
model_path = "model/model.h5"
translator = Translate(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['GET','POST'])
def translate():
    # get the input sentence
    english_sentence = request.form['english_sentence']
    logging.info("input is: {}".format(english_sentence))

    # call the translator methods 
    french_sentence = translator.translate(english_sentence)
    # logging the result
    logging.info("translation is: {}".format(french_sentence))
    return render_template('index.html', french_sentence = french_sentence)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
