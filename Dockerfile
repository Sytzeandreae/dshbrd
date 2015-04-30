FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y git-core python-all-dev python-pip python-virtualenv \
    libpq-dev wget build-essential ruby ruby-dev ruby-bundler

ADD . /src

WORKDIR /tmp
RUN wget http://nodejs.org/dist/latest/node-v0.12.2.tar.gz
RUN tar xvf node-v*
RUN cd node-v* && ./configure && make && make install
RUN rm -rf node-v* *.tar.gz

WORKDIR /src
RUN pip install -r requirements.txt
RUN npm install -g bower
RUN npm install -g grunt
RUN gem install sass -v 3.4.4
RUN gem install compass -v 1.0.1
RUN gem install zurb-foundation -v 4.3.2 
RUN gem install foundation -v 1.0.4
RUN npm install
RUN bower install
RUN browserify react/app.js | uglifyjs > dshbrd/static/js/bundle.min.js
RUN grunt sass
#RUN python app.py db upgrade

EXPOSE 80
CMD gunicorn app:app -b 0.0.0.0:80 
