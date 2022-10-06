#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y npm apache2
curl -sL https://deb.nodesource.com/setup_14.x | bash -
apt-get install -y nodejs
cd /home/node
npm install newman
npm install newman-reporter-html
sleep 300
./node_modules/.bin/newman run -r html --reporter-html-export Mysql-report.html Mysql_postman
./node_modules/.bin/newman run -r html --reporter-html-export YottaDB-report.html YottaDB-postman
tail -f /dev/null 