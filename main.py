from flask import Flask, render_template, request, redirect, url_for, flash
# import pymysql.cursors
import pymysql

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Required for flash messaging

# Establish connection to MySQL database
db = pymysql.connect(host="localhost", 
                   port = 8889,
                   user="root", 
                   password="root", 
                   database="Air_Ticket_Reservation_System", 
                   charset="utf8mb4", 
                   cursorclass=pymysql.cursors.DictCursor
)

# cursor = db.cursor()
# @app.before_first_request
# def init_db():
#     db.ping(reconnect=True)


# Fix this later
# Function used to authenticate the user
def authenticate_user(username, password):
    cursor = db.cursor()
    query = "SELECT password FROM Customer WHERE email_address = %s"
    
    try:
        cursor.execute(query)
        output = cursor.fetchone() # use .fetchone() becauause the query should only return one row, and not multipe rows
        cursor.close()
        if output["password"] == output: # if the password matches
            return True # return true
        else: # username exists, but password does not match what's stored in the database
            flash("Incorrect Password") # displays a temporary message for the user to see
            return False
    
    except Exception:
        flash("Incorrect Email")
        flash("Incorrect Password")
        return False # return False

@app.route('/')
def index_page():
    fetch()
    return render_template('/index.html')

@app.route('/customer_login_page.html')
def customer_login_page():
    if request.method == "GET":
        return render_template('/customer_login_page.html')
    
    # Retrieve username and password from the form
    email = request.form['email_address']
    password = request.form['password']
    
    if (authenticate_user(email, password)):
        return redirect(url_for('/customer_board.html')) # successful login, change url to load the customer page
    
    # Authentication failed
    # Redirect back to the login page with an error message
    return render_template('/customer_login_page.html', error=True)

@app.route('/airline_staff_login_page.html')
def airline_staff_login_page():
    fetch()
    print('hl')
    return render_template('/airline_staff_login_page.html', error=True)


@app.route('/customer_board.html')
def customer():
    return redirect(url_for('/customer_dashboard'))

@app.route('/airline_staff_board.html')
def airline_staff():
    return redirect(url_for('/airline_staff_dashboard'))


def fetch():
    query = "SELECT * FROM Flight"
    cur = db.cursor()
    try:
        cur.execute(query)
        output = cur.fetchall()
        cur.close()
        print("output:", output)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug = True)
    
    
    
    