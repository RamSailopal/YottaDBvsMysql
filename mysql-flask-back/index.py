from flask import Flask, request, jsonify
import mysql.connector, json, os
app = Flask(__name__)

@app.route('/user', methods=['POST', 'DELETE', 'GET'])
def user():

    mydb = mysql.connector.connect(
      host=os.environ.get('MYSQLHOST'),
      user=os.environ.get('FLASKUSER'),
      password=os.environ.get('FLASKPASS'),
      database=os.environ.get('FLASKDAT')
    )

    mycursor = mydb.cursor()

    if request.method == 'GET':
       id = request.args.get('id',type=str)
       mycursor.execute("SELECT * FROM Users WHERE id = " + id + ";")
       myresult = mycursor.fetchall()
       json_data = []
       content = {}
       for res in myresult:
          content = {'id': res[0], 'name': res[1], 'sex': res[3], 'age': res[2]}
          json_data.append(content)
          content = {}
       return(jsonify(json_data))


    elif request.method == 'DELETE':
       id = request.args.get('id',type=str)
       mycursor.execute("DELETE FROM Users WHERE id = " + id + ";")
       mydb.commit()
       return('{ "id":"' + id + '","status":"deleted"}')

    elif request.method == 'POST':
       request_data = request.get_json()
       name = request_data['name']
       sex = request_data['sex']
       age = request_data['age']
       id = request_data['id']
       mycursor.execute("UPDATE Users SET name = '" + str(name) + "', sex  = '" +  str(sex)  + "', age = " + str(age) + " WHERE id = " + str(id) + ";")
       mydb.commit()
       return('{ "id":"' + str(id) + '","status":"updated"}')

    else:
       return('{ "status":"error"}')


@app.route('/adduser', methods=['POST'])
def adduser():

    mydb = mysql.connector.connect(
      host=os.environ.get('MYSQLHOST'),
      user=os.environ.get('FLASKUSER'),
      password=os.environ.get('FLASKPASS'),
      database=os.environ.get('FLASKDAT')
    )

    mycursor = mydb.cursor()

    if request.method == 'POST':
       request_data = request.get_json()
       name = request_data['name']
       sex = request_data['sex']
       age = request_data['age']
       print("INSERT INTO Users(name,sex,age) VALUES ('" + str(name) + "','" + str(sex) + "'," + str(age) + ");")
       mycursor.execute("INSERT INTO Users (name,sex,age)  VALUES ('" + str(name) + "','" + str(sex) + "'," + str(age) + ");")
       mydb.commit()
       return('{ "name":"' + str(name) + '","status":"added"}')

    else:
       return('{ "status":"error"}')


@app.route('/users', methods=['GET'])
def users():

    mydb = mysql.connector.connect(
      host=os.environ.get('MYSQLHOST'),
      user=os.environ.get('FLASKUSER'),
      password=os.environ.get('FLASKPASS'),
      database=os.environ.get('FLASKDAT')
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Users")
    myresult = mycursor.fetchall()
    json_data = []
    content = {}
    for res in myresult:
       content = {'id': res[0], 'name': res[1], 'sex': res[3], 'age': res[2]}
       json_data.append(content)
       content = {} 
    return(jsonify(json_data))

