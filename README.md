# Helsinki-NLP based English-Spanish-French Machine Translation App

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

1. **Pre-requirements:** You need to have installed Docker ([Guide to install it](https://docs.docker.com/engine/install/))

2. Run the Docker build
```
docker build -t machine-translation-service .
```

3. Run and Start the Docker container
```
docker run --name translate -p 5000:5000 -d machine-translation-service
```

The front end should then become available at ```http://localhost:5000```

**Important:** The first time, the time to load could be higher because the application will download the AI models from its original data source.