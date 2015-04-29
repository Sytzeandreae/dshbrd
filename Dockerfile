FROM ubuntu:14.04

RUN apt-get update -y
RUN apt-get install -y git-core python-all-dev python-pip python-virtualenv nodejs \
    libpq-dev npm

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
