from flask import Flask, redirect, render_template, request, session, url_for
import utility as util
import model as model
app = Flask(__name__)

app.secret_key = 'development key'


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        
        if(util.checkUser(email, password)):
            session['email']=email
            session['password']=password
            session['logged_in']=True
            return render_template('search.html')
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        if(util.addUser(email, password)):
            return render_template('login.html')    
        else:
            return render_template('signup.html')
    return render_template('signup.html')


@app.route('/user/search', methods=['GET'])
def search():
    if session['logged_in']:
        if request.method =='POST':
            search=request.form['search']
            search=model.get_recommendations(search)
            return render_template('search.html',recommendations=search)
        return render_template('search.html')
    


app.run(debug=True)