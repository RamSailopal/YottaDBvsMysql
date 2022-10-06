from flask import Flask, request, jsonify
import json, os, yottadb, time
app = Flask(__name__)

@app.route('/user', methods=['POST', 'DELETE', 'GET'])
def user():

    if request.method == 'GET':
       id = request.args.get('id',type=str)
       key=yottadb.Key("^PATIENTS")[id]["age"]
       age = key.get().decode()
       key=yottadb.Key("^PATIENTS")[id]["sex"]
       sex = key.get().decode()
       key=yottadb.Key("^PATIENTS")[id]["name"]
       name = key.get().decode()
       json_data = []
       content = {}
       content = {'id': id, 'name': name, 'sex': sex, 'age': age}
       json_data.append(content)
       return(jsonify(json_data))


    elif request.method == 'DELETE':
       id = request.args.get('id',type=str)
       key=yottadb.Key("^PATIENTS")[id]
       key.delete_tree()
       return('{ "id":"' + id + '","status":"deleted"}')

    elif request.method == 'POST':
       request_data = request.get_json()
       name = request_data['name']
       sex = request_data['sex']
       age = request_data['age']
       id = request_data['id']
       yottadb.set("^PATIENTS",(str(id), "name"), str(name))
       yottadb.set("^PATIENTS",(str(id), "sex"), str(sex))
       yottadb.set("^PATIENTS",(str(id), "age"), str(age))
       return('{ "id":"' + str(id) + '","status":"updated"}')

    else:
       return('{ "status":"error"}')


@app.route('/adduser', methods=['POST'])
def adduser():

    if request.method == 'POST':
       request_data = request.get_json()
       name = request_data['name']
       sex = request_data['sex']
       age = request_data['age']
       try:
          id = yottadb.subscript_previous("^PATIENTS", ("",)).decode()
       except yottadb.YDBNodeEnd:
          id=0
       id = int(id) + 1
       yottadb.set("^PATIENTS",(str(id), "name"), str(name))
       yottadb.set("^PATIENTS",(str(id), "sex"), str(sex))
       yottadb.set("^PATIENTS",(str(id), "age"), str(age))
       return('{ "name":"' + str(name) + '","status":"added"}')

    else:
       return('{ "status":"error"}')


@app.route('/users', methods=['GET'])
def users():
    json_data = []
    content = {}
    try:
       id = yottadb.subscript_next("^PATIENTS", ("",)).decode()
    except yottadb.YDBNodeEnd:
       content = {}
       content = {'id': "", 'name': "", 'sex': "", 'age': ""}
       json_data.append(content)
       return(jsonify(json_data))
    while True:
       try:
          key=yottadb.Key("^PATIENTS")[id]["age"]
          print(key)
          age = key.get().decode()
          key=yottadb.Key("^PATIENTS")[id]["sex"]
          sex = key.get().decode()
          key=yottadb.Key("^PATIENTS")[id]["name"]
          name = key.get().decode()
          content = {'id': str(id), 'name': str(name), 'sex': str(sex), 'age': str(age)}
          json_data.append(content)
          content = {} 
          id = yottadb.subscript_next("^PATIENTS", (id,)).decode()
       except yottadb.YDBNodeEnd:
          break
    return(jsonify(json_data))
