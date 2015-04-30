FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y git-core python-all-dev python-pip python-virtualenv \
    libpq-dev wget build-essential 

ADD . /src

WORKDIR /tmp
RUN wget http://nodejs.org/dist/latest/node-v0.12.2.tar.gz
RUN tar xvf node-v*
RUN cd node-v* && ./configure && make && make install
RUN rm -rf node-v* *.tar.gz

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
