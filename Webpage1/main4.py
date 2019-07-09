from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("template.html")
@app.route('/home')
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)