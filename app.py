from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql.connector 
import pandas as pd 
import mysql.connector as sql_db 
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')
import nltk
# nltk.download()
from nltk.stem import WordNetLemmatizer
import incidentcount
# import forecast_low
import pandas as pd
import graph
from flask_paginate import Pagination, get_page_parameter
import Mannu
# import forecast_low
import graph1
app = Flask(__name__)


app.secret_key = 'your secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ticketcog'


mysql = MySQL(app)


# @app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_table WHERE username = % s AND password = % s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
            session['username'] = account['username']
            session['role_id'] = account['role_id']
            role = session['role_id']

            if session['role_id'] == 1:
                return redirect(url_for('searchpage'))
            elif session['role_id'] == 2:
                return redirect(url_for('tablepageitsm'))
            elif session['role_id'] == 3:
                return redirect(url_for('smetablepage'))
            elif session['role_id'] == 4:
                return redirect(url_for('admindashboard'))
            else:
                return render_template('login.html', msg = msg)

        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role_id = 1
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_table WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute("INSERT INTO user_table (username, email, password, role_id) VALUES (%s,%s,%s,%s)", (username,email,password,role_id))

            # cursor.execute('INSERT INTO user_table VALUES (NULL, % s, % s, % s, %s)', (username,email,password,role_id))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route("/index")
def index():
    if 'loggedin' in session:
        return render_template("index.html")
    return redirect(url_for('login'))


@app.route("/display")
def display():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_table WHERE user_id = % s', (session['user_id'], ))
        account = cursor.fetchone()
        return render_template("display.html", account = account)
    return redirect(url_for('login'))

@app.route("/update", methods =['GET', 'POST'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            # role_id = request.form['role_id']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user_table WHERE username = % s', (username, ))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'name must contain only characters and numbers !'
            else:
                cursor.execute('UPDATE user_table SET username =% s, password =% s, email =% s WHERE user_id =% s', (username, password, email, (session['user_id'], ), ))
                mysql.connection.commit()
                msg = 'You have successfully updated !'
        elif request.method == 'POST':
            msg = 'Please fill out the form !'
        return render_template("update.html", msg = msg)
        
    return redirect(url_for('login'))
from datetime import datetime


@app.route("/createticket", methods =['GET', 'POST'])
def createticket():
    msg = ''
    ticketnumber = ''
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        user_id = session['user_id']    # msg = ''
        if request.method == 'POST' and 'subject' in request.form and 'description' in request.form and 'priority_idup' in request.form and 'application_name' in request.form and 'Category' in request.form :
            subject = request.form['subject']
            description = request.form['description']
            priority_idup = request.form['priority_idup']
            created_at = datetime.now()
            Category = request.form['Category']
            status_idup = 1
            application_name = request.form['application_name']
            if application_name == 'Outlook' or application_name == 'SAP' or application_name == 'Hr_tool' or application_name == 'Colaboration':
                assigned_to = 'raghav_it'
            elif application_name =='Skype' or application_name == 'VPN' or application_name == 'PowerBi' or application_name == 'Engineering_tool' or application_name == 'Other':
                assigned_to = 'arjun'
            elif application_name == 'Hardware' or application_name == 'ERP' or application_name == 'Access' or application_name == 'Ess' or application_name == 'Windows':
                assigned_to = 'shubhangi'
            else:
                assigned_to == 'None'
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO ticket (subject, description, status_idup, priority_idup, user_id, created_at, Category, application_name, assigned_to) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (subject ,description,status_idup,priority_idup ,user_id, created_at, Category,application_name,assigned_to))
            mysql.connection.commit()
            msg = 'You have successfully created a ticket. !'
            ticketnumber = cursor.fetchone()
            mydb = sql_db.connect(host='127.0.0.1', database='ticketcog', user ='root', password ='root',auth_plugin='mysql_native_password') 
            mycursor = mydb.cursor() 
            mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            mycursor.execute("""SELECT ticketid,subject,status_idup, priority_idup,created_at,Category, application_name FROM ticket""") 
            df = pd.DataFrame(mycursor.fetchall(), columns = ["ticketid","subject","status_idup","priority_idup","created_at","Category","application_name"]) 
            df.to_csv('ticketdatabaseappend.csv',index=False)
        return render_template("createticket.html", msg = msg, ticketnumber = ticketnumber)
    
    return redirect(url_for('login'))

import smtplib;
from email.mime.text import MIMEText;
@app.route('/smeKedbAdd', methods =['GET', 'POST'])
def smeKedbAdd():
    msg=''
    if request.method == 'POST':
        if "ticketid" in request.form and 'description' in request.form and 'status_idup' in request.form and 'priority_idup' in request.form and 'Category' in request.form and 'application_name' in request.form and 'Resolution' in request.form and 'email' in request.form:
            ticketid = request.form["ticketid"]
            description=request.form['description']
            Category =  request.form['Category']
            application_name = request.form['application_name']
            resolved_date = datetime.now()
            resolved_by = session['username']
            status_idup = request.form['status_idup']
            priority_idup = request.form['priority_idup']
            email = request.form["email"]
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE ticket SET status_idup = %s ,priority_idup = %s ,resolved_date =%s ,resolved_by =%s WHERE ticketid = %s", (status_idup,priority_idup,resolved_date,resolved_by, ticketid))
            mysql.connection.commit()
            print("insert resolution")
            Resolution = request.form['Resolution']
            print('description',description ,'Category',Category)      
            if status_idup == '4':   
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute("INSERT INTO kedb (description, Category, application_name, Resolution) VALUES (%s,%s,%s,%s)", (description ,Category ,application_name ,Resolution))
                # cursor.execute("INSERT INTO kedb (description , Category , application_name ,Resolution) VALUES (% s, % s, % s, %s)" ,(description, Category, application_name, Resolution))
                mysql.connection.commit()
                msg = 'You have successfully registered !'
            # elif request.method == 'POST':

                msg = 'Please fill out the form !'
                mydb = sql_db .connect(host='127.0.0.1', database='ticketcog', user ='root', password ='root',auth_plugin='mysql_native_password') 
                mycursor = mydb.cursor() 
                mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                mycursor.execute("""SELECT kdbid , description , Category , application_name , Resolution FROM kedb""") 
                df = pd.DataFrame(mycursor.fetchall(), columns = ["kdbid", "description", "Category", "application_name","Resolution"]) 
                df.to_csv("kedb.csv", index=False) 
            
                ser = smtplib.SMTP('smtp.gmail.com',587);
                ser.starttls();
                ser.login('janhaviparab06@gmail.com','vikpbkunqhgpbzef')
                email_body = """<pre> 
                Congratulations! We've successfully resolved your error.
                    Was your issue resolved: <a href="http://localhost:5000/ticketstatus">Feedback</a>
                    Thanks,
                    SME Team,TicketCOG.
                    </pre>"""

                msg = MIMEText(email_body ,'html')
                ser.sendmail('janhaviparab06@gmail.com', email, msg.as_string());
                print('mail sent');
           
        return redirect(url_for('smetablepage'))
    if 'loggedin' in session:
        if session['role_id'] == 3:
            ticketid = request.args.get('ticketid')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            print(f"tickt ID: {ticketid}")
            cursor.execute('select t1.*, t2.* ,t3.* ,t4.* from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON t3.status_id = t1.status_idup LEFT JOIN user_table  t4  ON t4.user_id = t1.user_id where ticketid = % s', (ticketid, ))
            account = cursor.fetchone()
            print(f"account: {account}")
            return render_template('smeKedbAdd.html', account=account ,ticketid=ticketid)
        else:
            return render_template('error.html')
        
# endpoint for search
# @app.route('/')
@app.route('/')
def redirectpages():
    return redirect(url_for('searchpage'))

@app.route('/searchpage', methods=['GET', 'POST'])
def searchpage():
    Que = request.form.get("Issue")
    if request.method == "POST":
        v = request.form['Issue']
        data=pd.read_csv('ticketcog.csv')
        question=data['description'].tolist()
        # application=data['application_name'].tolist()
        answer=data['resolution_notes'].tolist()

        lemmer = nltk.stem.WordNetLemmatizer()
        def LemTokens(tokens):
            return [lemmer.lemmatize(token) for token in tokens]
            
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

        def LemNormalize(text):
            return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    
        def responses(user):
            response=''
            question.append(user)
            # application.append(user)
            TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
            tfidf = TfidfVec.fit_transform(question)
            val = cosine_similarity(tfidf[-1], tfidf)

            id1=val.argsort()[0][-2]
            #print(idx)
            flat = val.flatten()
            flat.sort()

            req = flat[-2]

                
            for word in response.split():
                if word.lower() in GREETING_INPUTS:
                    return random.choice(GREETING_RESPONSES)

            if(response=='how are you'):
                return random.choice(GREETING_R)

            for word in response.split():
                if word.lower() in ["nice","good","good job","okay","cool","great"]:
                    return "smile.."

            if(req==0):
                response =  ["I am sorry! I don't have a solution ."] 
                return response 
                
            else:
                response = response+answer[id1]
                question.remove(user)
                return response.split(".")
    #   
        if(v=="exit"):
            command=0
        else:
            response = responses(str(v))
            print(response) 
        return render_template('searchpage.html', Que=Que , response=response)
    return render_template('searchpage.html')

@app.route('/tablepageitsm', methods =['GET', 'POST'])
# @app.route('/tablepageitsm', defaults={'page':1})
# @app.route('/tablepageitsm/page/<int:page>')
def tablepageitsm(): 
    if 'loggedin' in session:
        if session['role_id'] == 2:
            page = request.args.get(get_page_parameter(), type=int, default=1)
            limit= 10
            offset = page*limit - limit
            # perpage= 10
            # startat= page*perpage
            # page = request.args.get('page', 1, type=int)
            print("tablepage called!")
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)   
            cursor.execute("select t1.*, t2.* ,t3.*  from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON status_id = t1.status_idup ORDER BY created_at DESC") 
            result = cursor.fetchall() #data from database
            total = len(result)
            print(total) 
            cursor.execute("""select t1.*, t2.* ,t3.*  from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON status_id = t1.status_idup ORDER BY created_at DESC limit %s offset %s""", (limit, offset))
            data = cursor.fetchall()
            pagination = Pagination(page=page, page_per=limit, total=total)
            return render_template("tablepageitsm.html", value=data, pagination=pagination) 
        else:
            return render_template('error.html')
    return redirect(url_for('login'))

import smtplib;
from email.mime.text import MIMEText;

import csv
import sys

@app.route("/itsmopenticket", methods =['GET','POST'])
def itsmopenticket():
    if request.method == 'POST':
        print(request.form)
        if request.form['submit_resolution'] == 'Submit resolution to user' and "ticketid" in request.form and'status_idup' in request.form and 'email' in request.form and 'priority_idup' in request.form and 'resolution_notes_ITSM' in request.form :
            status_idup = request.form['status_idup']
            priority_idup = request.form['priority_idup']
            resolution_notes_ITSM = request.form['resolution_notes_ITSM']
            ticketid = request.form["ticketid"]
            email = request.form["email"]
            resolved_date = datetime.now()
            resolved_by = session['username']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE ticket SET status_idup = %s ,priority_idup = %s ,resolution_notes_ITSM = %s ,resolved_date =%s ,resolved_by=%s WHERE ticketid = %s", (status_idup,priority_idup,resolution_notes_ITSM,resolved_date,resolved_by, ticketid))
            mysql.connection.commit()
            print("insert resolution")
            if status_idup == '4':
                ser = smtplib.SMTP('smtp.gmail.com',587);
                ser.starttls();
                ser.login('janhaviparab06@gmail.com','vikpbkunqhgpbzef')
                email_body = """<pre> 
                Congratulations! We've successfully resolved your error.
                    Was your issue resolved: <a href="http://localhost:5000/ticketstatus">Feedback</a>
                    Thanks,
                    ITSM Team,TicketCOG .
                    </pre>"""

                msg = MIMEText(email_body ,'html')
                ser.sendmail('janhaviparab06@gmail.com', email, msg.as_string());
                print('mail sent');
        return redirect(url_for('tablepageitsm')) 
        
            
    response = []
    if 'loggedin' in session:
        if session['role_id'] == 2:
            ticketid = request.args.get('ticketid')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            print(f"tickt ID: {ticketid}")
            cursor.execute('select t1.*, t2.* ,t3.* ,t4.* from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON t3.status_id = t1.status_idup LEFT JOIN user_table  t4  ON t4.user_id = t1.user_id where ticketid = % s', (ticketid, ))
            account = cursor.fetchone()
            print(f"account: {account}")
            print("kedb")
            number = account['Category']
            application = account['application_name']
            csv_file = csv.reader(open('kedb.csv', "r"), delimiter=",")
            for row in csv_file:
                if number == row[2] and application == row[3]:
                    print (row[0],row[4])
                    responses = (row[4])
                    response.append(responses)
                
            return render_template('itsmopenticket.html', response=response , account =account, ticketid=ticketid)
        else:
            return render_template('error.html')
    return redirect(url_for('login')) 

@app.route('/smetablepage', methods =['GET', 'POST'])
def smetablepage(): 
    if 'loggedin' in session:
        if session['role_id'] == 3:
            print("tablepage called!")
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)   
            cursor.execute("select t1.*, t2.* ,t3.*  from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON status_id = t1.status_idup  WHERE  t1.assigned_to= %s ORDER BY created_at DESC" ,(session['username'],) ) 
            data = cursor.fetchall() 
            return render_template("smetablepage.html", value=data) 
        else:
            return render_template('error.html')
    return redirect(url_for('login'))  

@app.route('/assigntoSME' , methods=['GET','POST'])
def assigntoSME():
    if request.method == 'POST':
        if "ticketid" in request.form and 'status_idup' in request.form and 'priority_idup' in request.form and 'assigned_to' in request.form :
            status_idup = request.form['status_idup']
            priority_idup = request.form['priority_idup']
            assigned_to = request.form['assigned_to']
            ticketid = request.form["ticketid"]
            print("status_idup",status_idup)
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE ticket SET status_idup = %s ,priority_idup = %s ,assigned_to = %s  WHERE ticketid = %s", (status_idup,priority_idup,assigned_to,ticketid))
            mysql.connection.commit()
            print("insert sme")
        return redirect(url_for('tablepageitsm')) 
    if 'loggedin' in session:
        if session['role_id'] == 2:
            ticketid = request.args.get('ticketid')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            print(f"tickt ID: {ticketid}")
            cursor.execute('select t1.*, t2.* ,t3.* ,t4.* from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON t3.status_id = t1.status_idup LEFT JOIN user_table  t4  ON t4.user_id = t1.user_id where ticketid = % s', (ticketid, ))
            account = cursor.fetchone()
            print(f"account: {account}")
            return render_template('assigntoSME.html', account =account, ticketid=ticketid)
        else:
            return render_template('error.html')
        
    return redirect(url_for('login')) 

@app.route('/ticketstatus', methods =['GET', 'POST'])
def ticketstatus(): 
    if 'loggedin' in session:
        print("ticket status page called")
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)   
        cursor.execute("select t1.*, t2.* ,t3.*  from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON status_id = t1.status_idup  WHERE  t1.user_id= %s  ORDER BY created_at DESC " ,(session['user_id'],) ) 
        data = cursor.fetchall() #data from database 
        return render_template("ticketstatus.html", value=data) 
    return redirect(url_for('login'))  

@app.route('/Yesfeedback', methods =['GET', 'POST'])
def Yesfeedback(): 
    msg = ''
    if request.method == 'POST' and "ticketid" in request.form :
        ticketid = request.form["ticketid"]
        status_idup = 3
        closed_date= datetime.now()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE ticket SET status_idup = %s ,closed_date= %s WHERE ticketid = %s", (status_idup,closed_date,ticketid))
        mysql.connection.commit()
        msg = "YOU HAVE SUCCESSFULLY CLOSED THE TICKET"
        return redirect(url_for('ticketstatus'))  

    
    # ticketnumber = ''
    if 'loggedin' in session:
        ticketid = request.args.get('ticketid')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        print(f"tickt ID: {ticketid}")
        cursor.execute('select t1.*, t2.* ,t3.* ,t4.* from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON t3.status_id = t1.status_idup LEFT JOIN user_table  t4  ON t4.user_id = t1.user_id where ticketid = % s', (ticketid, ))
        account = cursor.fetchone()
        print(f"account: {account}")
        
        return render_template("Yesfeedback.html", account=account , ticketid=ticketid) 
    return redirect(url_for('login'))  

@app.route('/Nofeedback', methods =['GET', 'POST'])
def Nofeedback(): 
    msg = ''
    if request.method == 'POST' and "ticketid" in request.form :
        ticketid = request.form["ticketid"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        status_idup = 5
        cursor.execute("UPDATE ticket SET status_idup = %s  WHERE ticketid = %s", (status_idup,ticketid))
        mysql.connection.commit()
        msg ="Ticket reopened"
        return redirect(url_for('ticketstatus'))  

    
    if 'loggedin' in session:
        ticketid = request.args.get('ticketid')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        print(f"tickt ID: {ticketid}")
        cursor.execute('select t1.*, t2.* ,t3.* ,t4.* from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON t3.status_id = t1.status_idup LEFT JOIN user_table  t4  ON t4.user_id = t1.user_id where ticketid = % s', (ticketid, ))
        account = cursor.fetchone()
        print(f"account: {account}")
        
        return render_template("Nofeedback.html", account=account , ticketid=ticketid) 
    return redirect(url_for('login'))  

@app.route('/userlist', methods =['GET', 'POST'])
def userlist(): 
    if 'loggedin' in session:
        if session['role_id'] == 4:
            print("tablepage called!")
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)   
            cursor.execute("select * from user_table" ) 
            data = cursor.fetchall() #data from database 
            return render_template("userlist.html", value=data) 
        else:
            return render_template('error.html')
    return redirect(url_for('login'))

@app.route('/ChangeRole', methods =['GET', 'POST'])
def ChangeRole(): 
    if request.method == 'POST':
        if "user_id" in request.form and 'role_id' in request.form:
            role_id = request.form['role_id']
            user_id = request.form['user_id']
            print("role_id",role_id)
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE user_table SET role_id = %s WHERE user_id = %s", (role_id,user_id))
            mysql.connection.commit()
            print("insert role")
        return redirect(url_for('userlist')) 

    if 'loggedin' in session:
        if session['role_id'] == 4:
            user_id = request.args.get('user_id')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            print(f"tickt ID: {user_id}")
            cursor.execute('select * from user_table where user_id = % s', (user_id, ))
            account = cursor.fetchone()
            print(f"account: {account}")
            return render_template('ChangeRole.html', account =account, user_id=user_id)
        else:
            return render_template('error.html')
    return redirect(url_for('login')) 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@app.route('/bar' , methods =['GET', 'POST'])
def bar():
    if 'loggedin' in session:
        if session['role_id'] == 4:
            incidentcount.ticket_plot()
            return render_template('bar.html')
        else:
            return render_template('error.html')
    return redirect(url_for('login'))
    
@app.route('/admindashboard', methods =['GET', 'POST'])
def admindashboard(): 
    if 'loggedin' in session:
        if session['role_id'] == 4:
            print("tablepage called!")
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)   
            cursor.execute("select t1.*, t2.* ,t3.*  from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON status_id = t1.status_idup ORDER BY created_at DESC LIMIT 5 " ) 
            data = cursor.fetchall() 
            #data from database 
            graph.applicationcount()
            graph.createdticket()
            graph.prioritycount()
            graph.categorycount()
            graph1.applicationcount1monthbefore()
            graph1.applicationcount1monthbefore()
            graph1.applicationlast2months()
            graph1.applicationlast6months()
            graph1.applicationlast12months()
            graph1.applicationSAPmonths()
            # application
            # categorycount()
            graph1.applicationlast3months()
            graph1.applicationcurrentweek()
            graph1.applicationpreviousweek()
            graph1.applicationcurrentcount()
            # applicationcountoctober()
            graph1.applicationcount3monthsbefore()
            graph1.applicationcount4monthsbefore()
            graph1.applicationcount5monthsbefore()
            graph1.applicationcount6monthsbefore()
            # categorycurrentcount()
            graph1.applicationcount2monthbefore()
            graph1.applicationPowerpointmonths()
            graph1.applicationEnginermonths()
            graph1.applicationVSmonths()
            graph1.applicationERPmonths()
            graph1.applicationExcelmonths()
            graph1.applicationHRmonths()
            graph1.applicationOutlookmonths()
            graph1.applicationSKYPEmonths()
            graph1.applicationVPNmonths()
            graph1.applicationPowerBimonths()
            graph1.applicationAccessmonths()
            graph1.applicationEssmonths()

            graph1.Categorycount1monthbefore()
            graph1.Categorylast2months()
            graph1.Categorylast6months()
            graph1.Categorylast12months()
            # CategorySAPmonths()
            # Category
            # categorycount()
            graph1.Categorylast3months()
            graph1.Categorycurrentweek()
            graph1.Categorypreviousweek()
            graph1.Categorycurrentcount()
            graph1.Categorycountoctober()
            graph1.Categorycount3monthsbefore()
            graph1.Categorycount4monthsbefore()
            graph1.Categorycount5monthsbefore()
            graph1.Categorycount6monthsbefore()
            # categorycurrentcount()
            graph1.Categorycount2monthbefore()
            graph1.CategoryLoginmonths()
            graph1.CategoryConfigurationmonths()
            graph1.CategoryAccessmonths()
            graph1.CategoryCrashmonths()
            graph1.CategoryReportmonths()
            graph1.CategoryPagemonths()
            graph1.CategoryFinancemonths()
            graph1.CategoryHardwaremonths()
            graph1.CategoryBackupmonths()
            graph1.applicationHardwaremonths()
            graph1.prioritycount1monthbefore()
            graph1.prioritycount1monthbefore()
            graph1.prioritylast2months()
            graph1.prioritylast3months()
            graph1.prioritylast6months()
            graph1.prioritylast12months()
            graph1.priorityLowmonths()
            # priority
            # categorycount()
            graph1.priorityMediummonths()
            graph1.prioritycurrentweek()
            graph1.prioritypreviousweek()
            graph1.prioritycurrentcount()
            # prioritycountoctober()
            graph1.prioritycount3monthsbefore()
            graph1.prioritycount4monthsbefore()
            graph1.prioritycount5monthsbefore()
            graph1.prioritycount6monthsbefore()
            # categorycurrentcount()
            graph1.prioritycount2monthbefore()
            graph1.priorityHighmonths()
            graph1.prioritySeveremonths()
           

            return render_template("admindashboard.html", value=data) 
        else:
            return render_template('error.html')
    return redirect(url_for('login'))

@app.route('/priorgraph' , methods =['GET', 'POST'])
def priorgraph():
    if 'loggedin' in session:
        if session['role_id'] == 4:
            Mannu.datalow_priority()
            Mannu.datamed_priority()
            Mannu.datahigh_priority()
            Mannu.datasevere_priority()
            # incidentcount.ticket_plot()
            # Mannu.priorityfunction()

            return render_template('priorgraph.html')
        else:
            return render_template('error.html')
    return redirect(url_for('login'))

@app.route('/alltickets', methods =['GET', 'POST'])
# @app.route('/tablepageitsm', defaults={'page':1})
# @app.route('/tablepageitsm/page/<int:page>')
def alltickets(): 
    if 'loggedin' in session:
        if session['role_id'] == 4:
            page = request.args.get(get_page_parameter(), type=int, default=1)
            limit= 10
            offset = page*limit - limit
            # perpage= 10
            # startat= page*perpage
            # page = request.args.get('page', 1, type=int)
            print("tablepage called!")
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)   
            cursor.execute("select t1.*, t2.* ,t3.*  from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON status_id = t1.status_idup ORDER BY created_at DESC") 
            result = cursor.fetchall() #data from database
            total = len(result)
            print(total) 
            cursor.execute("""select t1.*, t2.* ,t3.*  from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup  LEFT JOIN status_table  t3  ON status_id = t1.status_idup ORDER BY created_at DESC limit %s offset %s""", (limit, offset))
            data = cursor.fetchall()
            pagination = Pagination(page=page, page_per=limit, total=total)
            return render_template("alltickets.html", value=data, pagination=pagination) 
        else:
            return render_template('error.html')
    return redirect(url_for('login'))  
# server is running
if __name__ == "__main__":
    app.debug = True
    app.run(host ="localhost", port = int("5000"))

