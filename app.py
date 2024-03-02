from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask import Flask, request, render_template,jsonify
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")
tokenizer_es = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
model_es = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")
tokenizer_fr = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-es")
model_fr = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-es")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/english-to-spanish')
def english():
    return render_template('index.html')

@app.route('/spanish-to-english')
def spanish():
    return render_template('spanish.html')

@app.route('/french-to-spanish')
def french():
    return render_template('french.html')

@app.route('/translate_en_es', methods=['GET','POST'])
def english_form():
    input = request.form['input']
    input_ids = tokenizer(input, return_tensors="pt").input_ids
    outputs = model.generate(input_ids=input_ids, num_beams=1, num_return_sequences=1)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return jsonify(result=result)

@app.route('/translate_es_en', methods=['GET','POST'])
def spanish_form():
    input = request.form['input']
    input_ids = tokenizer_es(input, return_tensors="pt").input_ids
    outputs = model_es.generate(input_ids=input_ids, num_beams=1, num_return_sequences=1)
    result = tokenizer_es.batch_decode(outputs, skip_special_tokens=True)
    return jsonify(result=result)

@app.route('/translate_fr_es', methods=['GET','POST'])
def french_form():
    input = request.form['input']
    input_ids = tokenizer_fr(input, return_tensors="pt").input_ids
    outputs = model_fr.generate(input_ids=input_ids, num_beams=1, num_return_sequences=1)
    result = tokenizer_fr.batch_decode(outputs, skip_special_tokens=True)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)