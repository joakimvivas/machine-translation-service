from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask import Flask, request, render_template,jsonify
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")

app = Flask(__name__)

#inp = "Hi! My name is Joakim, nice to meet you!"
#input_ids = tokenizer(inp, return_tensors="pt").input_ids
#outputs = model.generate(input_ids=input_ids, num_beams=1, num_return_sequences=1)
#print("Generated:", tokenizer.batch_decode(outputs, skip_special_tokens=True))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['GET','POST'])
def my_form_post():
    input = request.form['input']
    input_ids = tokenizer(input, return_tensors="pt").input_ids
    outputs = model.generate(input_ids=input_ids, num_beams=1, num_return_sequences=1)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)