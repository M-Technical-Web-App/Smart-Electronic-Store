from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import numpy as np
import json
from tensorflow import keras
import tensorflow as tf
from spellchecker import SpellChecker
import nltk
from googletrans import Translator
import re
from keras.utils import pad_sequences
from nltk.corpus import stopwords
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
en_stopwords = stopwords.words('english')

app = Flask(__name__)
CORS(app)

translator = Translator()
new_model = keras.models.load_model('multiClass_lstmmodel.h5')
MAX_SEQUENCE_LENGTH = 250

with open('tokenizer.json') as json_file:
    json_string2 = json.load(json_file)
tokenizer_new = tf.keras.preprocessing.text.tokenizer_from_json(json_string2)


def sentiment(text):
    new_review = [text]
    seq = tokenizer_new.texts_to_sequences(new_review)
    padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
    pred = new_model.predict(padded)
    labels = ['negative', 'neutral', 'positive']
    ans = {
        "negative_val": float(pred[0][0]),
        "neutral_val": float(pred[0][1]),
        "positive_val": float(pred[0][2]),
        "prediction": labels[np.argmax(pred)]
    }
    print(ans)
    return ans


class TextProcessing:
    def __init__(self, text):
        self.text = text

    def getter(self):
        return self.text

    def translate(self):
        out = translator.translate(self.text, dest="en")
        self.text = out.text

    def to_lowerCase(self):
        out = self.text
        self.text = out.lower()

    def remove_whitespace(self):
        self.text = " ".join(self.text.split())

    def remove_punct(self):
        res = re.sub(r'[^\w\s]', '', self.text)
        self.text = res

    def spell_check(self):
        outText = self.text
        outText = outText.split()
        result = []
        spell = SpellChecker()
        for word in outText:
            correct_word = spell.correction(word)
            result.append(correct_word)
        str1 = " "
        self.text = str1.join(result)

    def remove_urls(self):
        outText = self.text
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        self.text = url_pattern.sub(r'', outText)


# test = TextProcessing("overall its fine but the charger is not working properly very very bad and poor color combination  great product nice quality")
# test.remove_urls()
# test.translate()
# test.to_lowerCase()
# test.remove_whitespace()
# test.remove_punct()
# test.spell_check()
# final_preprocessed_review = test.getter()
# sentiment(final_preprocessed_review)

def execute(text):
    test = TextProcessing(text)
    test.remove_urls()
    test.translate()
    test.to_lowerCase()
    test.remove_whitespace()
    test.remove_punct()
    # test.spell_check()
    final_preprocessed_review = test.getter()
    return sentiment(final_preprocessed_review)


@app.route('/predict', methods=["POST"])
def predict():
    new_data = request.get_json(request.data)
    fin_review_data = new_data["comment"]
    return (execute(fin_review_data))


if __name__ == "__main__":
    app.run(debug=True)
