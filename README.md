# AI Translation flask API for the Helsinki NLP

This is a **Python Flask application** based on the [Huggingface](https://huggingface.co) transformer library with the "[Helsinki-NLP/opus-mt-en-en-es](https://huggingface.co/Helsinki-NLP/opus-mt-en-es)" model developed by the [Language Technology Research Group of the University of Helsinki](https://blogs.helsinki.fi/language-technology/).

## Run the Application
### To run Locally

1. Cd into your repo as such:
```
$ cd machine-translation-service
```

2. Install requirements:
```
$ pip install -r requirements.txt
```

3. Run the server using this one simple command:
```
$ flask run
```
You can now access the app on your local browser by using
```
http://localhost:5000/
```

### To run with docker

```
docker build -t machine-translation-service .
docker run -p 5000:5000 -d machine-translation-service
```

The front end should then become available at ```http://localhost:5000```