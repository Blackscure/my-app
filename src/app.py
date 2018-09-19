from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
     return render_template("home.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/addprofileform')
def addprofileform():
    return render_template("profileform.html")

@app.route('/addprofile')
def addprofile():
    myname = request.args.get('myname')
    state_of_residence = request.args.get('state_of_residence')
    return render_template('profile.html', myname=myname, state_of_residence=state_of_residence)

if __name__ == '__main__':
    app.run(debug=True)