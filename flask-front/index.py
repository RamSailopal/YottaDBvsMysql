from flask import Flask, render_template, request, redirect
import os, requests
app = Flask(__name__)

@app.route('/newuser')
def newuser():
    return render_template('newuser.html')

@app.route('/amenduser')
def amenduser():
    id = request.args.get('id',type=str)
    r = requests.get('http://flask_flask-back-yotta:5000/user?id=' + id)
    users=r.json()
    for user in users:
       jsonsend=user
    return render_template('amenduser.html', user=jsonsend)

@app.route('/')
def home():
    r = requests.get('http://flask_flask-back-yotta:5000/users')
    return render_template('home.html', users=r.json())

@app.route('/deluser')
def deluser():
    id = request.args.get('id',type=str)
    r = requests.delete('http://flask_flask-back-yotta:5000/user?id=' + id)
    return redirect('/')


@app.route('/user', methods=['GET'])
def user():
    id = request.args.get('id',type=str)
    r = requests.get('http://flask_flask-back-yotta:5000/user?id=' + id)
    users=r.json()
    for user in users:
       jsonsend=user
    return render_template('user.html', user=jsonsend)

@app.route('/procnewuser', methods=['POST'])
def procnewuser():
   if request.method  == 'POST':
      name = request.form.get("name")
      age = request.form.get("age")
      sex = request.form.get("sex")
      jsonstr = { 'name': name, 'age': age, 'sex': sex }
      x = requests.post('http://flask_flask-back-yotta:5000/adduser', json = jsonstr)
      return redirect('/')
   else:
      return render_template('newuser.html') 

@app.route('/procamenduser', methods=['POST'])
def procamenduser():
   if request.method  == 'POST':
      name = request.form.get("name")
      age = request.form.get("age")
      sex = request.form.get("sex")
      id = request.form.get("id")
      jsonstr = { 'id': id, 'name': name, 'age': age, 'sex': sex }
      x = requests.post('http://flask_flask-back-yotta:5000/user', json = jsonstr)
      return redirect('/')
   else:
      return render_template('newuser.html')



