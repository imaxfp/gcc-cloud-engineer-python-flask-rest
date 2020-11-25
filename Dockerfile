FROM python:3.8
MAINTAINER "imaxfp"
RUN mkdir gcc-demo
COPY . /gcc-demo
WORKDIR /gcc-demo

RUN pip install -r requirements.txt

ENV APP_HOME /gcc-demo/src
WORKDIR $APP_HOME
RUN ls -la
#ENTRYPOINT ["/bin/sh"]

# Install production dependencies
#RUN pip install Flask gunicorn
EXPOSE 8080
CMD ["gunicorn" ,"--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "4", "--timeout", "0", "app:app"]
#CMD ['exec', 'gunicorn', '--bind', '0.0.0.0:8080', 'app:app']
#CMD exec gunicorn --bind :PORT --workers 1 --threads 4 --timeout 0 app:app