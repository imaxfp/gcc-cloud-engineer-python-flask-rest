FROM python:3.7
MAINTAINER "imaxfp"
RUN mkdir gcc-demo
COPY . /gcc-demo
WORKDIR /gcc-demo
RUN pip install -r requirements.txt
RUN ls -la
WORKDIR /gcc-demo/src
RUN ls -la
ENTRYPOINT ["python"]
EXPOSE 5005
CMD ["app.py"]