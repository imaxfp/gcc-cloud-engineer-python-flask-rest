# Google Cloud Certified Associate Cloud Engineer
### Python Flask Dockerized Application with scripts for Google Cloud Platform installation.    

### Steps for google cloud setup: 
1. login to the google console
2. git clone https://github.com/imaxfp/gcp-python-rest-demo.git
3. 


Build the image using the following command

```bash
docker build -t simple-flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
docker run -p 5001:5001 simple-flask-app
```

The application will be accessible at http:127.0.0.1:5001 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`

Remove all containers
```bash
docker rm $(docker ps -aq)
```