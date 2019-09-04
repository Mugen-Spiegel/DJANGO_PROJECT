FROM ubuntu:18.04

MAINTAINER jophat <tamay06131993@gmail.com>

LABEL version="1.1"
LABEL description="Test Image for cheat-sheet"

# ENV set env directory tree
ENV ROOT_DIR=/var/www/html
ENV PYTHONUSERBASE=$ROOT_DIR/venv
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=
ENV PATH=$PATH:~/.local/bin/
# ENV DEBIAN_FRONTEND noninteractive
ENV DJANGO_SETTINGS_MODULE=inventory.settings

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils debconf
RUN apt-get install -y --no-install-recommends libmysqlclient-dev
RUN apt-get install -y --no-install-recommends unixodbc-dev
# RUN apt-get install -y --no-install-recommends git nginx
RUN apt-get install -y --no-install-recommends gnupg
RUN apt-get install -y  python3 python3-setuptools python3-venv python3-pip python3-dev
RUN pip3 install django
RUN pip3 install djangorestframework
COPY requirements.txt $ROOT_DIR/requirements.txt
# RUN apt-get install -y telnet supervisor
# RUN apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/Asia/Manila /etc/localtime
# RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN export PYTHONUSERBASE
RUN python3 -m venv $ROOT_DIR/venv
RUN $ROOT_DIR/venv/bin/pip3 install --upgrade --user pip
RUN $ROOT_DIR/venv/bin/pip3 install -r $ROOT_DIR/requirements.txt --user
# RUN $ROOT_DIR/venv/bin/pip3 install crossbar
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# RUN echo "NGINX on Ubuntu 18.04" > $ROOT_DIR/index.nginx-debian.html

# add vhost config file
# ADD ./config/nginx/conf.d/billing.conf /etc/nginx/sites-available/
# RUN ln -sf /etc/nginx/sites-available/billing.conf /etc/nginx/sites-enabled/billing.conf
# RUN rm /etc/nginx/sites-enabled/default

# set up uwsgi & celery
# RUN pip3 install --upgrade pip uwsgi celery daphne
# RUN mkdir -p /etc/uwsgi/sites/

# supervisor
# COPY ./config/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# ADD ./config/uwsgi/billing.ini $ROOT_DIR/
# ADD ./config/uwsgi/uwsgi.service /etc/systemd/system/ # not needed to register in services
# ADD ./config/uwsgi/uwsgi_params $ROOT_DIR/
# RUN ln -sf $ROOT_DIR/billing.ini /etc/uwsgi/sites/billing.ini

# Install project requirements & create venv for Uwsgi
# ADD ./billing/requirements.txt $ROOT_DIR/requirements.txt


#remove packages that are no longer needed
# RUN apt-get -y autoremove

# RUN echo ">> Done Building Image"
# This way both interactive and non-interactive modes get set.
# ENV DEBIAN_FRONTEND teletype
EXPOSE 80

ENTRYPOINT ["/bin/bash"]
# ENTRYPOINT ["/usr/bin/supervisord"]
