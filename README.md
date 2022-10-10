# YottaDBvsMysql

Testing YottaDB against Mysql in a Python Flask framework using Postman/newman

This repo utilises separate repos for <a href="https://github.com/RamSailopal/flask-mysql-demo">Flasks/mysql</a> and <a href="https://github.com/RamSailopal/flask-yottadb-demo">Flask/YottaDB</a> 

# Provisioning


[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RamSailopal/YottaDBvsMysql)

Locally:

    git clone https://github.com/RamSailopal/YottaDBvsMysql.git
    cd YottaDBvsMysql
    docker-compose up
    
Once provisioning is fully completed, two newman html reports will be generated with API GET/POST request results (see below for more info).
    
# Testing

The results of the tests can be found here:

YottaDB - https://htmlpreview.github.io/?https://github.com/RamSailopal/YottaDBvsMysql/blob/main/newman/YottaDB-report.html

Mysql - https://htmlpreview.github.io/?https://github.com/RamSailopal/YottaDBvsMysql/blob/main/newman/Mysql-report.html

A complete (side by side) report - https://htmlpreview.github.io/?https://github.com/RamSailopal/YottaDBvsMysql/blob/main/newman/Complete-report.html

In **summary**, YottaDB **GET** requests are quicker than Mysql taking **5ms** against **10ms** for Mysql. Mysql is quicker with regards to **POST** requests though, registering **314ms** against **552ms** for YottaDB




