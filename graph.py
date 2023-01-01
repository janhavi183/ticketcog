import matplotlib.pyplot as plt  
import mysql.connector
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import os
from matplotlib.figure import Figure
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="ticketcog")
mycursor=mydb.cursor()
def applicationcount():
	mycursor.execute("select application_name,count(1) from ticket where date_add(curdate(),INTERVAL -3 month)<created_at group by application_name")
	result = mycursor.fetchall
	application_name = []
	count = []

	for i in mycursor:
		application_name.append(i[0])
		count.append(i[1])
		
	print("Application Name ", application_name)
	print("Count of application monthly ", count)

	# figure1 = data1.plot(figsize=(15,6))
	#     fig = figure1.figure
	#     fig.savefig('z1.png')

	# Visulizing Data using Matplotlib
	
	plt.bar(application_name, count)
	# fig = figure1.figure
	# plt.plot(figsize=(15,6))
	plt.ylim(0, 30)
	# plt.xlim(0, 10)
	plt.xlabel("Application name")
	# plt.autoap()
	# plt.style.use("ggplot")
	# plt.tight_layout()

	plt.xticks(rotation=90)
	# plt.setp(application_name.get_application_name(), rotation=30, horizontalalignment='right')
	plt.ylabel("Count by month")
	plt.title("Issues Application wise")
	

	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "sample"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	# plt.legend(loc='upper center', numpoints=1, bbox_to_anchor=(0.5, -0.05),ncol=2, fancybox=True, shadow=True)

	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def prioritycount():
	mycursor.execute("select  priority_name,count(1) from ticket t1 LEFT JOIN priority_table  t2  ON t2.priority_id = t1.priority_idup where date_add(curdate(),INTERVAL -3 month)<created_at group by priority_name  ")
	result = mycursor.fetchall
	priority_name = []
	count = []

	for i in mycursor:
		priority_name.append(i[0])
		count.append(i[1])
		
	print("Priority id", priority_name)
	print("Count of priority id month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(priority_name, count)
	plt.ylim(0, 30)
	plt.xlabel("Priority id")
	plt.ylabel("Count by month")
	plt.title("Issues raised priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "priority"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name)
	# plt.savefig('my_plot.png')
	plt.close()
	return
def statuscount():
	mycursor.execute("select  status_name,count(1) from ticket t1 LEFT JOIN status_table  t2  ON t2.status_id = t1.status_idup where date_add(curdate(),INTERVAL -3 month)<created_at group by status_name  ")
	result = mycursor.fetchall
	status_name = []
	count = []

	for i in mycursor:
		status_name.append(i[0])
		count.append(i[1])
		
	print("Priority id", status_name)
	print("Count of priority id month wise ", count)


	# Visulizing Data using Matplotlib
	plt.bar(status_name, count)
	plt.ylim(0, 30)
	plt.xlabel("Priority id")
	plt.ylabel("Count by month")
	plt.title("Issues raised priority wise")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "status"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name)
	# plt.savefig('my_plot.png')
	plt.close()
	return

def categorycount():
	mycursor.execute("select  Category,count(1) from ticket where date_add(curdate(),INTERVAL -3 month)<created_at group by Category ")
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
	sample_file_name = "Category"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name ,dpi=(250), bbox_inches='tight')
	# plt.savefig('my_plot.png')
	plt.close()
	return
def createdticket():
	mycursor.execute("select  created_at,count(1) from ticket where date_add(curdate(),INTERVAL -3 month)<created_at group by created_at ")
	result = mycursor.fetchall
	created = []
	count = []

	for i in mycursor:
		created.append(i[0].date())
		count.append(i[1])
		
	print("No of tickets= ", created)
	print("Count month wise = ", count)


	# Visulizing Data using Matplotlib
	plt.scatter(created, count)
	plt.ylim(0, 50)
	plt.xlabel("Created at ")
	plt.ylabel("Count of tickets by month")
	plt.title("Overall ticekt issues")
	# plt.show()
	script_dir = os.path.dirname(__file__)
	results_dir = os.path.join(script_dir, 'static/')
	sample_file_name = "ticketsratio"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	plt.savefig(results_dir + sample_file_name , dpi=(250))
	# plt.savefig('my_plot.png')
	plt.close()
	return
# statuscount()
# createdticket()
# prioritycount()
# applicationcount()
# categorycount()
