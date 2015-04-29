FROM ubuntu:14.04

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y git-core python-all-dev python-pip python-virtualenv \
    libpq-dev wget build-essential openssl libssl-dev pkg-config

RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get -y install nodejs

ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt
RUN npm install
RUN npm install bower
RUN bower install
RUN browserify react/app.js | uglifyjs > dshbrd/static/js/bundle.min.js
RUN grunt sass
#RUN python app.py db upgrade


EXPOSE 80
CMD gunicorn app:app -b 0.0.0.0:80 
