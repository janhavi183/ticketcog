import matplotlib.pyplot as plt  
import mysql.connector
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import os
from matplotlib.figure import Figure
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="ticketcog")
mycursor=mydb.cursor()
def applicationcurrentcount():
	mycursor.execute("SELECT application_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 0 MONTH) GROUP BY (application_name) ")
	result = mycursor.fetchall
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for current month")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Current_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationcount1monthbefore():
	mycursor.execute("SELECT application_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 1 MONTH) GROUP BY (application_name) ")
	result = mycursor.fetchall
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "1monthbefore_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationcount2monthbefore():
	mycursor.execute("SELECT application_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 2 MONTH) GROUP BY (application_name) ")
	result = mycursor.fetchall
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "2monthbefore_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationcount3monthbefore():
	mycursor.execute("SELECT application_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 2 MONTH) GROUP BY (application_name) ")
	result = mycursor.fetchall
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "October_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationcount3monthsbefore():
	mycursor.execute("SELECT application_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 3 MONTH) GROUP BY (application_name) ")
	result = mycursor.fetchall
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "3monthbeforeapplication"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationcurrentweek():
	mycursor.execute("SELECT application_name,COUNT(ticketid) as Count, created_at FROM ticket WHERE YEARWEEK(`created_at`, 1) = YEARWEEK( CURDATE() - INTERVAL 0 WEEK) group by application_name")
	result = mycursor.fetchall
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 15)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Currentweek_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationpreviousweek():
	mycursor.execute("SELECT application_name,COUNT(ticketid) as Count, created_at FROM ticket WHERE YEARWEEK(`created_at`, 1) = YEARWEEK( CURDATE() - INTERVAL 1 WEEK) group by application_name")
	result = mycursor.fetchall
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 10)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for previos week")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "previousweek_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationlast3months():
	mycursor.execute("SELECT application_name,COUNT(ticketid) as Count FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 3 MONTH group by application_name")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 10)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for last 3 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last3months_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationlast6months():
	mycursor.execute("SELECT application_name,COUNT(ticketid) as Count , created_at FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 6 MONTH group by application_name")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application last 6 months wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 10)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for last 6 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last6months_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationlast2months():
	mycursor.execute("SELECT application_name,COUNT(ticketid) as Count , created_at FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 2 MONTH group by application_name")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application last 2 months wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 10)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for last 2 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last2months_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationlast12months():
	mycursor.execute("SELECT application_name,COUNT(ticketid) as Count , created_at FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 12 MONTH group by application_name")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application last year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Application, count)
	plt.ylim(0, 10)
	plt.xticks(rotation=90)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for last year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "lastyear_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationSAPmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'SAP' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application last year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "SAP_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationVPNmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'VPN' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Month")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "VPN_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationVSmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'VS' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "VS_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationOutlookmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'Outlook'  GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Outlook_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationPowerpointmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'Powerpoint'  GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Powerpoint_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationExcelmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'Excel' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Excel_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationERPmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'ERP' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "ERP_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationHRmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'HR' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "HR_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return

def applicationEssmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'Ess' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Ess_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationAccessmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'Access' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Access_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationPowerBimonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'PowerBi' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "PowerBi_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationSKYPEmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'SKYPE' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "SKYPE_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationEnginermonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'Engineering_tool' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Enginer_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def applicationHardwaremonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE application_name = 'Hardware' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Application = []
	count = []

	for i in mycursor:
		Application.append(i[0])
		count.append(i[1])
		
	print("Application", Application)
	print("Count of Application  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Application)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Application")
	plt.ylabel("Count by month")
	plt.title("Issues raised Application wise yearly")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Hardware_application"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
# def categorycurrentcount():
# 	mycursor.execute("SELECT Category, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 0 MONTH) GROUP BY (Category)")
# 	result = mycursor.fetchall
# 	Category = []
# 	count = []

# 	for i in mycursor:
# 		Category.append(i[0])
# 		count.append(i[1])
		
# 	print("Category", Category)
# 	print("Count of Category month wise ", count)


# 	# Visulizing Data using Matplotlib
# 	plt.bar(Category, count)
# 	plt.ylim(0, 30)
# 	plt.xticks(rotation=45)
# 	plt.xlabel("Category")
# 	plt.ylabel("Count by month")
# 	plt.title("Issues raised Category wise")
# 	# plt.show()
# 	script_dir = os.path.dirname(__file__)
# 	results_dir = os.path.join(script_dir, 'static/')
# 	sample_file_name = "Current_Category"

# 	if not os.path.isdir(results_dir):
# 		os.makedirs(results_dir)

# 	# plt.plot([1,2,3,4])
# 	# plt.ylabel('some numbers')
# 	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
# 	# plt.savefig('my_plot.png')
# 	plt.close()
# 	return
def Categorycurrentcount():
	mycursor.execute("SELECT Category, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 0 MONTH) GROUP BY (Category) ")
	result = mycursor.fetchall
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Current_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorycount1monthbefore():
	mycursor.execute("SELECT Category, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 1 MONTH) GROUP BY (Category) ")
	result = mycursor.fetchall
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "1monthbefore_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorycount2monthbefore():
	mycursor.execute("SELECT Category, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 2 MONTH) GROUP BY (Category) ")
	result = mycursor.fetchall
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "2monthbefore_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorycountoctober():
	mycursor.execute("SELECT Category, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 2 MONTH) GROUP BY (Category) ")
	result = mycursor.fetchall
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "October_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorycount3monthsbefore():
	mycursor.execute("SELECT Category, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 3 MONTH) GROUP BY (Category) ")
	result = mycursor.fetchall
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "3monthbeforeCategory"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorycurrentweek():
	mycursor.execute("SELECT Category,COUNT(ticketid) as Count, created_at FROM ticket WHERE YEARWEEK(`created_at`, 1) = YEARWEEK( CURDATE() - INTERVAL 0 WEEK) group by Category")
	result = mycursor.fetchall
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 15)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Currentweek_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorypreviousweek():
	mycursor.execute("SELECT Category,COUNT(ticketid) as Count, created_at FROM ticket WHERE YEARWEEK(`created_at`, 1) = YEARWEEK( CURDATE() - INTERVAL 1 WEEK) group by Category")
	result = mycursor.fetchall
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "previousweek_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorylast3months():
	mycursor.execute("SELECT Category,COUNT(ticketid) as Count FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 3 MONTH group by Category")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for last 3 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last3months_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorylast6months():
	mycursor.execute("SELECT Category,COUNT(ticketid) as Count , created_at FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 6 MONTH group by Category")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category last 6 months wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for last 6 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last6months_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorylast2months():
	mycursor.execute("SELECT Category,COUNT(ticketid) as Count , created_at FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 2 MONTH group by Category")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category last 2 months wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for last 2 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last2monthsCategory"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def Categorylast12months():
	mycursor.execute("SELECT Category,COUNT(ticketid) as Count , created_at FROM ticket WHERE created_at >= DATE(NOW()) - INTERVAL 12 MONTH group by Category")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category last year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Category, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for last year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "lastyear_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryLoginmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Login' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Login_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryConfigurationmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Configuration' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Month")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Configuration_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryAccessmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Access'  GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Access_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryCrashmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Crash'  GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Crash_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryReportmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Report'  GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Report_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryPagemonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Page_not_loading' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Page_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryFinancemonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Finance' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Finance_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return

def CategoryHardwaremonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Hardware' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Hardware_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def CategoryBackupmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' FROM ticket WHERE Category = 'Backup' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Category = []
	count = []

	for i in mycursor:
		Category.append(i[0])
		count.append(i[1])
		
	print("Category", Category)
	print("Count of Category year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Category)
	plt.ylim(0, 10)
	plt.xticks(rotation=45)
	plt.xlabel("Category")
	plt.ylabel("Count by month")
	plt.title("Issues raised Category wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Backup_Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return

def prioritycurrentcount():
	mycursor.execute("SELECT priority_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 0 MONTH) GROUP BY (priority_name) ")
	result = mycursor.fetchall
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Current_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritycount1monthbefore():
	mycursor.execute("SELECT priority_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 1 MONTH) GROUP BY (priority_name) ")
	result = mycursor.fetchall
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "1monthbefore_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritycount2monthbefore():
	mycursor.execute("SELECT priority_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 2 MONTH) GROUP BY (priority_name) ")
	result = mycursor.fetchall
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "2monthbefore_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritycount3monthbefore():
	mycursor.execute("SELECT priority_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 2 MONTH) GROUP BY (priority_name) ")
	result = mycursor.fetchall
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "October_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritycount3monthsbefore():
	mycursor.execute("SELECT priority_name, COUNT(ticketid) as Count, MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE MONTH(created_at) = MONTH(CURDATE() - INTERVAL 3 MONTH) GROUP BY (priority_name) ")
	result = mycursor.fetchall
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "3monthbeforepriority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritycurrentweek():
	mycursor.execute("SELECT priority_name,COUNT(ticketid) as Count, created_at from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE YEARWEEK(`created_at`, 1) = YEARWEEK( CURDATE() - INTERVAL 0 WEEK) group by priority_name")
	result = mycursor.fetchall
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 15)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Currentweek_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritypreviousweek():
	mycursor.execute("SELECT priority_name,COUNT(ticketid) as Count, created_at from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE YEARWEEK(`created_at`, 1) = YEARWEEK( CURDATE() - INTERVAL 1 WEEK) group by priority_name")
	result = mycursor.fetchall
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "previousweek_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritylast3months():
	mycursor.execute("SELECT priority_name,COUNT(ticketid) as Count from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE created_at >= DATE(NOW()) - INTERVAL 3 MONTH group by priority_name")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Category month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise for last 3 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last3months_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritylast6months():
	mycursor.execute("SELECT priority_name,COUNT(ticketid) as Count , created_at from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE created_at >= DATE(NOW()) - INTERVAL 6 MONTH group by priority_name")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority last 6 months wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise for last 6 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last6months_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritylast2months():
	mycursor.execute("SELECT priority_name,COUNT(ticketid) as Count , created_at from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE created_at >= DATE(NOW()) - INTERVAL 2 MONTH group by priority_name")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority last 2 months wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise for last 2 months")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "last2months_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritylast12months():
	mycursor.execute("SELECT priority_name,COUNT(ticketid) as Count , created_at from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE created_at >= DATE(NOW()) - INTERVAL 12 MONTH group by priority_name")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority last year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(Priority, count)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise for last year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "lastyear_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def priorityLowmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE priority_name = 'Low' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority last year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Priority)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Low Priority wise for year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Low_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def priorityMediummonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE priority_name = 'Medium' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority last year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Priority)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Month")
	plt.ylabel("Count by month")
	plt.title("Issues raised for Medium Priority wise for last year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Medium_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def priorityHighmonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE priority_name = 'High' GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority last year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Priority)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised High Priority wise for year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "High_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritySeveremonths():
	mycursor.execute("SELECT COUNT(ticketid) as Count,MONTHNAME(created_at) as 'Month Name' from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup WHERE priority_name = 'Severe'  GROUP BY MONTH(created_at)")
	result = mycursor.fetchall 
	Priority = []
	count = []

	for i in mycursor:
		Priority.append(i[0])
		count.append(i[1])
		
	print("Priority", Priority)
	print("Count of Priority  year wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(count , Priority)
	plt.ylim(0, 30)
	plt.xticks(rotation=0)
	plt.xlabel("Priority")
	plt.ylabel("Count by month")
	plt.title("Issues raised Priority wise for  year")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "Severe_priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return

# applicationcount1monthbefore()
# applicationlast2months()
# applicationlast6months()
# applicationlast12months()
# applicationSAPmonths()
# # application
# # categorycount()
# applicationlast3months()
# applicationcurrentweek()
# applicationpreviousweek()
# applicationcurrentcount()
# # applicationcountoctober()
# applicationcount3monthsbefore()
# # categorycurrentcount()
# applicationcount2monthbefore()
# applicationPowerpointmonths()
# applicationEnginermonths()
# applicationVSmonths()
# applicationERPmonths()
# applicationExcelmonths()
# applicationHRmonths()
# applicationOutlookmonths()
# applicationSKYPEmonths()
# applicationVPNmonths()
# applicationPowerBimonths()
# applicationAccessmonths()
# applicationEssmonths()
# applicationHardwaremonths()

# Categorycount1monthbefore()
# Categorylast2months()
# Categorylast6months()
# Categorylast12months()
# # CategorySAPmonths()
# # Category
# # categorycount()
# Categorylast3months()
# Categorycurrentweek()
# Categorypreviousweek()
# Categorycurrentcount()
# Categorycountoctober()
# Categorycount3monthsbefore()
# # categorycurrentcount()
# Categorycount2monthbefore()
# CategoryLoginmonths()
# CategoryConfigurationmonths()
# CategoryAccessmonths()
# CategoryCrashmonths()
# CategoryReportmonths()
# CategoryPagemonths()
# CategoryFinancemonths()
# CategoryHardwaremonths()
# CategoryBackupmonths()
# prio