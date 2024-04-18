from flask import Flask, render_template, request, redirect, url_for
# import pymysql.cursors
import pymysql

app = Flask(__name__)

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
    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        stored_password = result['password']
        if hashlib.sha256(password.encode()).hexdigest() == stored_password:
            return True
    return False


@app.route('/')
def index_page():
    fetch()
    return render_template('index.html')

@app.route('/customer_login_page', methods=['POST'])
def customer_login_page():
    # Retrieve username and password from the form
    username = request.form['username']
    password = request.form['password']
    
    if (authenticate_user(username, password)):
        return redirect(url_for('customer_board')) # successful login, change url to load the customer page
    
    # Authentication failed
    # Redirect back to the login page with an error message
    return render_template('customer_login_page.html', error=True)

@app.route('/airline_staff_login_page')
def airline_staff_login_page():
    fetch()
    print('hl')
    # Retrieve username and password from the form
    # username = request.form['username']
    # password = request.form['password']
    
    # if (authenticate_user(username, password)):
    #     return redirect(url_for('airline_staff_dashboard')) # successful login, change url to load the airline staff page
    
    # # Authentication failed
    # # Redirect back to the login page with an error message
    return render_template('airline_staff_login_page.html', error=True)


@app.route('/customer_board')
def customer():
    return redirect(url_for('customer_dashboard'))

@app.route('/airline_staff_board')
def airline_staff():
    return redirect(url_for('airline_staff_dashboard'))


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
    
    
    
    