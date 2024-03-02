# Helsinki-NLP based English-Spanish Machine Translation App

This is a **Python Flask application** based on the [Huggingface](https://huggingface.co) transformer library with the "[Helsinki-NLP](https://huggingface.co/Helsinki-NLP)" model developed by the [Language Technology Research Group of the University of Helsinki](https://blogs.helsinki.fi/language-technology/) and CSS based on [Materialize](https://materializecss.com/), a modern responsive CSS framework based on Material Design by Google.

![Homescreen](/static/images/homescreen.png)

## Run the Application
### To run Locally

1. Clone the repository in your Local
```
git clone https://github.com/joakimvivas/machine-translation-service.git
```

2. Cd into the repo as such:
```
$ cd machine-translation-service
```

3. Install requirements:
```
$ pip install -r requirements.txt
```

4. Run the server using this one simple command:
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
docker run --name translate -p 5000:5000 -d machine-translation-service
```

The front end should then become available at ```http://localhost:5000```