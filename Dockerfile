FROM python:3.9

WORKDIR /var/www

COPY requirements.txt /var/www/

RUN pip install -r requirements.txt

COPY . /var/www/