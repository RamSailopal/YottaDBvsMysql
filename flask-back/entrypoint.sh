#!/bin/bash
apt-get update
apt-get install -y python3 python3-pip python3-dev python3-setuptools libffi-dev 
pip3 install flask mysql-connector-python
source /opt/yottadb/current/ydb_env_set
/opt/yottadb/current/ydb <<< 'S ^PATIENTS=""'
pip install yottadb
cd /home/flask-back
export FLASK_APP=index
export FLASK_ENV=development
source /opt/yottadb/current/ydb_env_set
flask run --host=0.0.0.0
