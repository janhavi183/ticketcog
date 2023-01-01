import mysql.connector 
import pandas as pd 
 
# Connect to database 
mydb = mysql.connector.connect( 
  host='127.0.0.1', database='ticketcog', user ='root', password ='root',auth_plugin='mysql_native_password') 
 
mycursor = mydb.cursor() 
mycursor.execute("""SELECT ticketid ,subject , status_idup, priority_idup, created_at,Category, application_name FROM ticket""") 
 
df = pd.DataFrame(mycursor.fetchall(), columns = ["ticket_id","subject","status_idup","priority_idup","created_at","Category","application_name"]) 
df.to_csv('ticketdatabaseappend.csv',index=False)
# df.to_csv("ticketpredictdata2.csv", index=False) 