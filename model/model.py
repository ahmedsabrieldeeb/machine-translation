import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.utils import pad_sequences
import regex as re
import numpy as np
import logging
import pickle

class Translate:

    def __init__(self, model_path):
        logging.info("Translate class initialized")
        self.model = load_model(model_path, compile=False)
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
        logging.info("Model is loaded!")
        

    def prepare_eng_sentence(self, eng_sentence):
        # remove punctuation
        eng_sentence = re.sub(r'[.!?:;,]', '', eng_sentence)

        # english tokenization
        with open('english_tokenizer.pickle', 'rb') as tokenizer_file:
            english_tokenizer = pickle.load(tokenizer_file)
        eng_tokenized = english_tokenizer.texts_to_sequences([eng_sentence])

        # padding the sentence
        eng_padded = pad_sequences(eng_tokenized, maxlen = 15, padding='post')

        return eng_padded

    def translate(self, eng_sentence):
        # getting the sentence
        eng = self.prepare_eng_sentence(eng_sentence)

        # feed into the model
        out = self.model.predict(eng, verbose=0)

        # french tokenization
        with open('french_tokenizer.pickle', 'rb') as tokenizer_file:
            french_tokenizer = pickle.load(tokenizer_file)

        # converting the out to french sentence
        out = np.argmax(out, axis=-1)
        reverse_fr_dict = {v: k for k, v in french_tokenizer.word_index.items()}
        french = [reverse_fr_dict[i] if i != 0 else '' for i in out[0]]
        french = [word for word in french if word != '']
        french_sentence = ' '.join(french)
        
        return french_sentence