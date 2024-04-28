from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
# import pymysql.cursors
import pymysql

'''

Make sure to check whether each one is a post or get method:
    
Checking whether the request method is POST or GET is a common practice in web development, especially when handling form submissions. Here's why it's important:

GET Request: This method is typically used for fetching data from the server. When a user initially loads a page or follows a link, the browser sends a GET request
to the server. In your Flask route, when the method is GET, you might want to render the login form for the user to fill out.
POST Request: This method is used when the user submits a form or sends data to the server to be processed. When the user fills out the login form and clicks the
submit button, the browser sends a POST request to the server with the form data. In your Flask route, when the method is POST, you need to process the form 
data submitted by the user.

'''

app = Flask(__name__)

app.secret_key = 'my_secret_key'
# app.config['SECRET_KEY'] = 'my_secret_key'

# Establish connection to MySQL database
db = pymysql.connect(host="localhost", 
                   port = 8889,
                   user="root", 
                   password="root", 
                   database="air_ticket_reservation_system", 
                   charset="utf8mb4", 
                   cursorclass=pymysql.cursors.DictCursor
)

# cursor = db.cursor()
# @app.before_first_request
# def init_db():
#     db.ping(reconnect=True)



# Function to check whether the customer exists in the databse, used when logging in
def authenticate_customer(email_address_in, password_in):
    cursor = db.cursor()
    query = "SELECT * FROM Customer WHERE Customer.email_address = %s and Customer.password = %s"
    query = "SELECT * FROM Customer WHERE Customer.email_address = %s"
    try:
        # cursor.execute(query, (email_address_in, password_in))
        cursor.execute(query, email_address_in)
        # print("right after executing")
        output = cursor.fetchall() # use .fetchone() becauause the query should only return one row, and not multipe rows
        # Note; type(output) is a list of length (only supports index 0). In this index is a dictionary of the row retrieved) output[0] to access dictionary,
        # output[0]["key_name"] to access the value in that key
        cursor.close()
        if output[0]["password"] == password_in: # If the password_in matches the one retrieved # and output[0]["email_address"] == email_address_in: # if the email and password matches
            return True # return true
        if output[0]["email_address"] == email_address_in: # if only the email_address_in matches the one retrieved, account exists but wrong password
            # email exists, but password does not match what's stored in the database
            flash("Incorrect Password") # displays a temporary message for the user to see
            return False
        # Do not create a case for (output[0]["password"] == password_in)
        return False
    
    except Exception:
        flash("Incorrect Email")
        flash("Incorrect Password")
        print("inside exception for authenticate_customer()")
        return False # return False
    
# fucntion to check whether the airline staff exists in the databse, used when logging in
def authenticate_airline_staff(username, password):
    cursor = db.cursor()
    query = "SELECT password FROM Airline_Staff WHERE username = %s"
    
    try:
        cursor.execute(query, username)
        output = cursor.fetchone() # use .fetchone() becauause the query should only return one row, and not multipe rows
        cursor.close()
        if output[0]["password"] == password: # if the password matches
            return True # return true
        # username exists, but password does not match what's stored in the database
        flash("Incorrect Password") # displays a temporary message for the user to see
        return False
    
    except Exception:
        flash("Incorrect Username")
        flash("Incorrect Password")
        return False # return False
        
    

# function to check whether the airline staff already exists in the databse, used when registering
def airline_staff_exists(username):
    cursor = db.cursor()
    query = "SELECT * FROM Airline_Staff WHERE username = %s"
    
    try:
        cursor.execute(query, username) #m ust be username, because you have to pass in a tuple, not a single variable
        output = cursor.fetchone() # this query should only be returning one row becuase usernames are unique
        if output[0]["username"] == username: # if the retrieved output matches the username passed in 
            return True # return true becuase the username exists
        return False # if the usernames do not match, aka if it returns an empty set, the username doesn't exist
    
    except Exception:
        return False # erorr occured, couldn't check staff exists
        

# function to check whether the customer already exists in the databse, used when registering
def customer_exists(email_addess):
    cursor = db.cursor()
    query = "SELECT * FROM Customer WHERE email_address = %s"
    
    try:
        cursor.execute(query, (email_addess,)) # ust be email_address, because you have to pass in a tuple, not a single variable
        output = cursor.fetchone() # this query should only be returning one row becuase email_address are unique
        if output[0]["email_address"] == email_addess: # if the retrieved output matches the username passed in 
            return True # return true becuase the username exists
        return False # if the usernames do not match, aka if it returns an empty set, the username doesn't exist
    
    except Exception:
        return False# erorr occured, couldn't check customer exists
    


        
        
        

    

@app.route('/')
def index_page():
    # fetch()
    return render_template('/index.html')

@app.route('/customer_login_page.html', methods = ['GET', 'POST']) # route to the customer's login page (Where they enter email and password)
def customer_login_page():
    if request.method == "POST":
        # Retrieve username and password from the form
        email = request.form['email_address']
        password = request.form['password']
        
        if (authenticate_customer(email, password)):
            session["email"] = email
            return redirect(url_for('customer')) # successful login, change url to load the customer page
            # return render_template('/customer_dashboard.html')
    
    # Authentication failed or method not POST
    # Redirect back to the login page with an error message
    print("failed authentication")
    return render_template('customer_login_page.html', error=True)

@app.route('/airline_staff_login_page.html', methods = ['GET', 'POST']) # route to the arline staff's login page (Where they enter email and password)
def airline_staff_login_page():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
    
        if (authenticate_airline_staff(username, password)):
            session["username"] = username
            return redirect(url_for('/airline_staff_dashboard.html'))  # successful login, change url to load the airline staff page
            # return render_template('/airline_staff_board.html')
    
    # Authentication failed or method not POST
    # Redirect back to the login page with an error message
    return render_template('airline_staff_login_page.html', error=True)


@app.route('/customer_dashboard.html', methods = ['GET', 'POST'])
def customer():
    print("inside customer board")
    try:
        email_address = session['email']
        cursor = db.cursor()
        query = "SELECT * FROM Customer where email_address = %s"
        cursor.execute(query, email_address)
        user_data = cursor.fetchall() # retrieves the data of the customer logged in
        query = """
        SELECT sum(Ticket.sold_price) 
        FROM Customer, Purchase, Ticket 
        WHERE Customer.email_address = %s and Customer.email_address = Purchase.email_address and Purchase.id_number = Ticket.id_number 
        and Purchase.purchase_date >= DATE_SUB(NOW(), INTERVAL 1 YEAR)
        """
        cursor.execute(query, email_address)
        user_spending = cursor.fetchall() # retrieves the sum of spendings spent
        cursor.close()
        return render_template('customer_dashboard.html', customer = user_data[0], spendings = user_spending[0])

    except Exception:
        message = 'Please Login or Create an Account'
        print("inside exception for customer()")
        return render_template('customer_login_page.html', error=message)

@app.route('/spending_range', methods=['POST'])
def spending_range():
    try:
        email_address = session['email']
        cursor = db.cursor()
        
        # fetch user data:
        query = "SELECT * FROM Customer where Customer.email_address = %s"
        cursor.execute(query, email_address)
        user_data = cursor.fetchall() # extracts user data
        
        # fetch spending within a range
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        query = """
        SELECT sum(Ticket.sold_price)
        FROM Customer, Purchase, Ticket 
        WHERE Customer.email_address = %s and Customer.email_address = Purchase.email_address and Purchase.id_number = Ticket.id_number 
        and Purchase.purchase_date >= %s and Purchase.purchase_date <= %s
        """
        cursor.execute(query, (email_address, start_date, end_date))
        spending_data = cursor.fetchall()
        cursor.close()
        
        return render_template('customer_dashboard.html', customer = user_data[0], spendings_within_range = spending_data[0])
    
    except Exception as e:
        # Handle exceptions
        return "Error: Unable to fetch spending data within the specified range"
        
        


@app.route('/airline_staff_board.html', methods = ['GET', 'POST'])
def airline_staff():
    # if 'username' in session:
        # return redirect(url_for('/airline_staff_dashboard'))
    if 'username' in session:
        return render_template('airline_staff_dashboard.html')
    
@app.route('/registration_for_airline_staff.html', methods = ['GET', 'POST'])
def register_airline_staff():
    if request.method == "POST":
        first_name = request.form['username']
        last_name = request.form['last_name']
        username = request.form['username']
        email_address = request.form['email_address']
        password = request.form['password']
        date_of_birth = request.form['date_of_birth']
        phone_number = request.form['phone_number']
        
        cursor = db.cursor()
        try:    
            if (airline_staff_exists(username)): #if airline staff exists
                flash("Error: Account already exists")
        
            else: # if airline staff doesn't exist
                #First, create queries
                # Insert data into Airline_Staff table
                query1 = "INSERT INTO Airline_Staff (username, password, first_name, last_name, date_of_birth) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query1, (username, password, first_name, last_name, date_of_birth))
                # Insert email address into Airline_Staff_Email_Address table
                query2 = "INSERT INTO Airline_Staff_Email_Address (username, email_address) VALUES (%s, %s)"
                cursor.execute(query2, (username, email_address))
                # Insert phone number into Airline_Staff_Phone_Number table
                query3 = "INSERT INTO Airline_Staff_Phone_Number (username, phone_number) VALUES (%s, %s)"
                cursor.execute(query3, (username, phone_number))
                
                #commit changes
                db.commit()
                
                # Let the user know the registration was successful
                flash("Registration successful")

        
        except Exception:
            db.rollback()
            flash("An error occurred during registration. Please try again.")
            
        finally:
            cursor.close()
            render_template('registration_for_airline_staff.html', error=True) # return the registration page always
        
    return render_template('registration_for_airline_staff.html', error=True)


@app.route('/registration_for_customer.html', methods = ['GET', 'POST'])
def register_customer():
    if request.method == "POST":
        email_address = request.form["email_address"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        password = request.form["password"]
        building_number = request.form["building_number"]
        street = request.form["street"]
        apt_number = request.form["apt_number"]
        city = request.form["city"]
        state = request.form["state"]
        zipcode = request.form["zipcode"]
        passport_number = request.form["passport_number"]
        passport_expiration = request.form["passport_expiration"]
        passport_country = request.form["passport_country"]
        date_of_birth = request.form["date_of_birth"]
        phone_number = request.form["phone_number"]
        
        cursor = db.cursor()
        
        try:
            if (customer_exists(email_address)): # if customer exists
                flash("Error: Account already Exists")
                
            else: # if customer doesn't exist
                query1 = "INSERT INTO Customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query1, (email_address, first_name, last_name, password, building_number, street, apt_number, city, state, zipcode, passport_number, passport_expiration, passport_country, date_of_birth))
                
                query2 = "INSERT INTO CustomerPhone VALUES (%s, %s)"
                cursor.execute(query2, (email_address, phone_number))
                
                # commit changes
                db.commit()
                
                # Let the user know the registration was successful
                flash("Registration successful")
        
        except Exception:
            db.rollback()
            flash("An error occurred during registration. Please try again.")
            
        finally:
            cursor.close()
            render_template('registration_for_customer.html', error=True) # return the registration page always





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
    