from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# About Us page route
@app.route('/about')
def about():
    return render_template('about.html')

# Membership page route
@app.route('/membership')
def membership():
    return render_template('membership.html')

if __name__ == '__main__':
    app.run(debug=True)
