# Translation flask API for the Helsinki NLP

This is the language translation API based on transformers and MarianMT model for language translation (based on huggingface). This provides easy pretrained Language models that can be used to do machine translation in any 2 desired languages. There is one webpage as well that works on MyMemory API to provide translation that can also store recent translations.  

## API
There are 2 versions of the  REST API
version 0 that exposes only supported language and other as webapp
version 1 that exposes 4 endpoints to the internet.

**V0 API CONTRACTS**

```txt
GET /
GET v0/supported_langs
```
**V1 API CONTRACTS**
```txt
GET v1/health
GET v1/lang_routes
GET v1/supported_languages
POST v1/translate
```
**Inputs**
'source' : Source Language 
'target' : Target Language
'text' : Text to be transferred

**OUTPUTS**
'translation' : Translated Text
'supported languages' : Languages Supported 
'language routes' : routes to languages

## Run the Application
### To run Locally

0. After this, ensure you have installed virtualenv globally as well. If not, run this:
```
$ pip install virtualenv
```
1. Cd into your repo as such:
```
$ cd machine-translation-service
```

2. Create and fire up your virtual environment in python3:
```
$ virtualenv -p python3 venv
$ pip install autoenv
```
```
(venv)$ pip install -r requirements.txt
```

3. Run the server using this one simple command:
```
(venv)$ flask run
```
You can now access the app on your local browser by using
```
http://localhost:5000/
```
Or test using  Postman

## To run with docker

```
docker build -t machine-translation-service .
docker run -p 5000:5000 -v $(pwd)/data:/app/data -d machine-translation-service
```

The front end should then become available at http://localhost:5000.