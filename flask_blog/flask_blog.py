from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm , LoginForm

app = Flask(__name__)

# the secret_key will protect against modifying cookies and cross
# site forgery attacks...etc. 
# idealy the secret key should be random char
# good way to get reandom char in python > start command portal > import secrests > secrets.token_hex(16)
app.config['SECRET_KEY'] = 'c05e46876d3de7e22d6752a8dc5f681e'

posts = [
    {
        'author': 'Yasir O',
        'title': 'Blog 1',
        'content': 'first yasir blog',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'abu S',
        'title': 'Blog 3',
        'content': '3rd Abu blog',
        'date_posted': 'March 23, 2021'   
    }
]

title = 'about page'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts) 
    #the posts on the left of the = is a variable. 
    #the second posts, on the left of the =, is the list of dicts
    #by passing it as an argument to teh render_template function we will
    # have access to this variable in our home.html template

@app.route('/about')
def about():
    return render_template('about.html', title = title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    #creates a from instance. this will create the form 
    form = RegistrationForm() 
    if form.validate_on_submit(): #this checks that the form was validated before it is submitted 
        flash(f'Account created for {form.username.data}!', 'success') #after importing flash from flask you can careate these one time flash messages
        return redirect(url_for('home')) #url_for() is a url function. in this case we are redirecting to the home function that is in the home route
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm() # login instance form 
    return render_template('login.html', title='login', form=form)

if __name__=='__main__':
    app.run(debug=True)