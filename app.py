
from flask import Flask, request
from indictrans import Transliterator
from flask_cors import CORS
from flask_cors import cross_origin
from translation import TranslationLookup

app = Flask(__name__)
CORS(app)
lookup_object = TranslationLookup()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@cross_origin()
@app.route('/trans')
def transliterate():
    word = request.args.get('word', default="congress", type=str)
    trn = Transliterator(source='eng', target='hin', build_lookup=True, decode='beamsearch')
    best_transliterated_list = trn.transform(word, k_best=5)
    return {"transliteration": best_transliterated_list}


@cross_origin()
@app.route('/lookup')
def lookup():
    word = request.args.get('word', default='congress', type=str)
    return {"translation": lookup_object.lookup_from_glossory(word)}


if __name__ == "__main__":
    app.run()


