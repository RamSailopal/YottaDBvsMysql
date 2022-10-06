#!/bin/bash
apt-get update
apt-get install -y python3 python3-pip mysql-client
pip3 install flask mysql-connector-python
cd /home/flask-back
mysql --user="root" --password="example" -h testmysql -e 'create database test;'
mysql --user="root" --password="example" -h testmysql test < setup.sql
export FLASK_APP=index
export FLASK_ENV=development
flask run --host=0.0.0.0
