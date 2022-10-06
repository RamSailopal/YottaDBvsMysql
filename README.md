# flask-yottadb-demo

A simple demo of the Python Flask framework using yottadb as a backend

Creates a simple api for adding users to a YottaDB database

![Alt text](flask.JPG?raw=true "view")

# Provisioning


[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RamSailopal/flask-yottadb-demo)

Locally:

    git clone https://github.com/RamSailopal/flask-yottadb-demo.git
    cd flask-yottadb-demo
    docker-compose up
    
# Backend
    
    
On completion of the provisioning of the environment, navigate to http://serveraddress:5000/user to GET and POST data

# YottaDB view

    ^PATIENTS(1,"age")=52
    ^PATIENTS(1,"name")="Bob Taylor"
    ^PATIENTS(1,"sex")="Male"


# Front-end

A crude front-end to demonstate the use of Jinja templates has been added.

To view the front-end, navigate to:

http://serveraddress:5001 - Locally

https://5001-gitpodaddress - Gitpod


# Mysql comparison

This implementation has also be done with mysql as opposed to YottaDB for comparison purposes.

The mysql implementation can be found here:

https://github.com/RamSailopal/flask-mysql-demo



