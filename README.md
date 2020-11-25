# Google Cloud Certified Associate Cloud Engineer
### Python Flask Dockerized Application with scripts for Google Cloud Platform installation.    

### Containerization process into GCP
1. Container build 
2. Container registry
3. Container deploy & run  


Build the image using the following command

```bash
docker build -t simple-flask-app:latest .
```

```bash
docker run -it -p 8080:8080 simple-flask-app
```

Remove all containers
```bash
docker rm $(docker ps -aq)
```