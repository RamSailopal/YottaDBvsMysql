#!/bin/bash
apt-get update
apt-get install -y python3 python3-pip 
pip3 install flask requests 
cd /home/flask-front
export FLASK_APP=index
export FLASK_ENV=development
flask run --host=0.0.0.0
