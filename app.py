from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def singin():
    return render_template('signin.html')

if __name__=="__main__":
    app.run(debug=True)
