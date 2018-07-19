FROM ubuntu:16.04
RUN apt-get update \ 
    && apt-get install python3 python3-pip -y 
RUN pip3 install flask
COPY flask* /
EXPOSE 5000
ENTRYPOINT python3 /flasktest.py

