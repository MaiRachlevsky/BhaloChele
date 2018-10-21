import os

from flask import Flask, render_template, redirect, session, flash, request, url_for
app = Flask(__name__)

app.secret_key = os.urandom(32) #generate random key to use session for cookies

users = {'sh':'hi'}

@app.route("/")
def home():
    if 'sh' in session: #if a user is logged in
        return render_template("homepage.html", user = 'sh')#send to welcome page
    else:
        return render_template("login.html")#login page

@app.route("/auth", methods = ['POST'])
def login():
    if request.form['username'] in users and request.form['password'] == users[request.form['username']]:
        session['sh'] = 'hi' #logs in user
        return render_template('homepage.html')#send to welcome page
    else:
        flash("Invalid username/password. Please try again. If you do not have an account please register")
        return render_template("login.html")

@app.route("/logout", methods = ["POST", "GET"])
def gohome():
	session.pop('sh',None)#logs out user. None used if no users are logged in
	return redirect(url_for('home'))#Send to login page
#Send to login page


    
@app.route("/register", methods = ['POST'])
def register():
	if request.form['rusername'] in users: #checks is username is taken
		flash("username is taken, please try again")
		return render_template('login.html')#back to login page
	users[request.form['rusername']] = request.form['rpassword']#adds userame/password to dictionary
	flash("registration complete. Please log in")
	return render_template('login.html')#sends back to login page

if __name__ == "__main__":
    app.debug = True
    app.run()

