from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

# all these routes will lead to the same page (GET is the default method)
@app.route("/home_page")
@app.route("/home")
@app.route("/")
def home_func():
    # DB
    found = False
    if found: # theoretically - if a user was found, return the HTML with the following parameters
        return render_template('index.html',
                               name='Mirit',
                               last_name='Zelichonok')
    else:
        return render_template('index.html')


@app.route("/about", methods=['GET'])
def about_func():
    if session['username'] == '': # if the user didn't log in yet / logged out
        return render_template('about.html')
    else: # else - return the page "tailored" according to the user details
        return render_template('about.html',
                               uni='BGU',
                               profile={'name': 'Mirit',
                                        'last_name': 'Zelichonok'},
                               degrees=['BSc.', 'Msc.'],
                               hobbies=('art', 'programming', 'teaching')
                               )

# in this page there is a GET form, that after you fill it and submit it returns to the same page
@app.route("/catalog", methods=['GET'])
def catalog_func():
    color = 'green'
    if 'product_type' in request.args: # after filling the form, a request.arg object is created
        product_type = request.args['product_type']
        size = request.args['size']
        return render_template('catalog.html', p_type=product_type, p_size=size, color=color)
    return render_template('catalog.html', color=color) # else

# the HTML of this page is an example for how to use the base.html as the base of other pages
@app.route("/catalog_2", methods=['GET'])
def catalog2_func():
    return render_template('catalog_2.html')

# example for form with POST method (hides the query parameters in the URL)
@app.route("/login", methods=['GET', 'POST'])
def login_func():
    if request.method == "POST":
        username = request.form['username']  # when we use POST we'll use request.form, not request.args
        password = request.form['password']
        # DB
        session['username'] = username # global variable - across all pages
    return render_template('login.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout_func():
    session['username'] = '' # removing the global variable
    return render_template('login.html') # returns to the log in page


@app.route("/try_request")
def try_request_func():
    return request.method  # this way we can see which method a page uses


if __name__ == '__main__':
    app.secret_key = '123' # we need a secret key when we import and use flask session
    app.run(debug=True)
