from flask import Flask, render_template, request, redirect
from users import Users

app = Flask(__name__)

@app.route('/')
def index():

    users_info = Users.get_all()
    print(users_info)
    
    return render_template('read.html', all_users = users_info)

@app.route('/users')
def users():

    return render_template('create.html')

@app.route('/add_user', methods = ['POST'])
def add_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    Users.save(data)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)