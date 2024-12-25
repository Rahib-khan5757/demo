from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# About Us page route
@app.route('/about')
def about():
    return render_template('about.html')

# Membership page route
@app.route('/contact')  # Added the leading slash
def contact():
    return render_template('contact.html')

# Gallery page route
@app.route('/gallery')  # Added the leading slash
def gallery():
    return render_template('gallery.html')

# Login page route
@app.route('/login')  # Added the leading slash
def login():
    return render_template('login.html')

# Register page route
@app.route('/register')  # Added the leading slash
def register():
    return render_template('register.html')

# Services page route
@app.route('/services')  # Added the leading slash
def services():
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True)
