# Google Cloud Certified Associate Cloud Engineer
### Python Flask Dockerized Application with scripts for Google Cloud Platform installation.    

Build the image using the following command

```bash
docker build -t simple-flask-app:latest .
```

```bash
docker run -p 8080:8080 simple-flask-app
```

Remove all containers
```bash
docker rm $(docker ps -aq)
```