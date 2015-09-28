import json
import Task
import Date

FILE_NAME = "task.json"



#parses the json file and makes a list of task objects
#
#input : filename -> name of the json file
#
#output : returns a list of Task objects made from parsing the json file
# 
def getTasksFromFile(fileName):
	allTasks = []

	jsonFile = open(fileName)
	data = json.load(jsonFile)
	#print len(data)

	#print data[len(data) - 1]["id"]
	for i in range(len(data)):
		instanceName = data[i]["instanceName"]
		dueDate = data[i]["dueDate"]
		priority = data[i]["priority"]
		closeDate = data[i]["closeDate"]
		instanceStatus = data[i]["instanceStatus"]
		assigneeType = data[i]["assigneeType"]
		createDate = data[i]["createDate"]
		name = data[i]["name"]
		url = data[i]["url"]
		assignee = data[i]["assignee"]
		instanceId = data[i]["instanceId"]
		status = data[i]["status"]
		variables = data[i]["variables"]
		processName = data[i]["processName"]
		myId = data[i]["id"]
		isOpen = False
		if closeDate == None:
			isOpen = True
		else:
			closeDate = Date.Date(closeDate)

		if dueDate != None:
			dueDate = Date.Date(dueDate)

		if createDate != None:
			createDate = Date.Date(createDate)

		t = Task.Task(instanceName, dueDate, priority, closeDate, instanceStatus, 
			assigneeType, createDate, name, url, assignee, instanceId, status, 
			variables, processName, myId, isOpen)

		allTasks.append(t)

	return allTasks



#*****************************************
#*************** METHOD 1 ****************
#*****************************************

#prints current number of open and closed tasks given a date
#
#inputs : tasks -> list of Task objects
#		 givenDate -> Date object representing the date for the tasks
#
#outputs : returns nothing
#		   prints the Open and Closed count
#
def currentOpenAndClosed(tasks, givenDate):

	#filter the tasks
	tasks_needed = []
	for i in range(len(tasks)):
		myDate = tasks[i].createDate
		if myDate.isEqual(givenDate) != 1:
			tasks_needed.append(tasks[i])

	openCount = 0
	closedCount = 0
	for i in range(len(tasks_needed)):
		closeDate = tasks_needed[i].closeDate
		if closeDate == None:
			openCount = openCount + 1
		elif closeDate.isEqual(givenDate) == 1:
			openCount = openCount + 1
		else:
			closedCount = closedCount + 1

	#return openCount, closedCount
	print "Open Count: ", openCount
	print "Closed Count: ", closedCount



#*****************************************
#*************** METHOD 2 ****************
#*****************************************

#prints current number of open and closed tasks given a range of dates
#
#inputs : tasks -> list of Task objects
#		  openDate -> Date object representing the start date of the range
#		  closeDate -> Date object representing the end date of the range
#
#outputs : returns nothing
#		   prints the Open and Closed count
#
def openAndClosedInRange(tasks, openDate, closeDate):

	#filter by openDate
	tasks_needed = []
	for i in range(len(tasks)):
		myDateCreate = tasks[i].createDate
		myDateClose = tasks[i].closeDate
		if myDateCreate.isEqual(closeDate) != 1:
			if myDateClose == None:
				tasks_needed.append(tasks[i])
			elif myDateClose.isEqual(openDate) == 0 or myDateClose.isEqual(openDate) == 1:
				tasks_needed.append(tasks[i])

	openCount = 0
	closedCount = 0
	for i in range(len(tasks_needed)):
		myDateClose = tasks_needed[i].closeDate
		if myDateClose == None:
			openCount = openCount + 1
		elif myDateClose.isEqual(closeDate) == 1:
			openCount = openCount + 1
		else:
			closedCount = closedCount + 1

	#return openCount, closedCount
	print "Open Count: ", openCount
	print "Closed Count: ", closedCount



#*****************************************
#*************** METHOD 3 ****************
#*****************************************

#prints the most recent task based on instanceId
#
#inputs : tasks -> list of Task objects
#		  intanceId -> integer representing the instanceId of a task
#
#outputs : returns nothing
#		   prints the name of the most recent task for that instance id
#
def mostRecentTaskByInstanceId(tasks, instanceId):

	#get all tasks with instanceId
	name = "Task with this instance id doesn't exist"
	tasks_needed = []
	for i in range(len(tasks)):
		if tasks[i].instanceId == instanceId:
			tasks_needed.append(tasks[i])


	if len(tasks_needed) == 0:
		return name

	myTask = tasks_needed[0]
	#myTask.createDate.printDate()
	for i in range(len(tasks_needed)):
		myDate = myTask.createDate
		otherDate = tasks_needed[i].createDate
		#otherDate.printDate()

		if otherDate.isEqual(myDate) == 1:
			myTask = tasks_needed[i]

	#return myTask.name
	print "Name: ", myTask.name



#*****************************************
#*************** METHOD 4 ****************
#*****************************************

#prints the number of for a given instanceId
#
#inputs : tasks -> list of Task objects
#		  instanceId -> integer representing the instanceId of a task
#
#outputs : returns nothing
#		   prints the count of tasks
#
def tasksByInstanceId(tasks, instanceId):
	count = 0
	for i in range(len(tasks)):
		if tasks[i].instanceId == instanceId:
			count = count + 1

	#return count
	print "Number of Tasks : ", count




#*****************************************
#*************** METHOD 5 ****************
#*****************************************

#prints the number of open and closed tasks for a given asignee
#
#inputs : tasks -> list of Task objects
#		  instanceId -> string representing the assignee of a task
#
#outputs : returns nothing
#		   prints the count of open and closed tasks
#
def openAndClosedTaskByAssignee(tasks, assignee):
	openCount = 0
	closedCount = 0
	for i in range(len(tasks)):
		if tasks[i].assignee == assignee:
			if tasks[i].isOpen:
				openCount = openCount + 1
			elif not tasks[i].isOpen:
				closedCount = closedCount + 1
	#return openCount, closedCount
	print "Open Count: ", openCount
	print "Closed Count: ", closedCount



#*****************************************
#*****************************************
#**** WRITE CODE TO TEST METHODS HERE ****
#*****************************************
#*****************************************

#first get the tasks form the json file
tasks = getTasksFromFile(FILE_NAME)

#example on how to create Date objects
#date1 = Date.Date("2015-02-22T22:24:57Z")
#date2 = Date.Date("2014-12-22T21:33:19Z")

#example on how to run the methods
#currentOpenAndClosed(tasks, date1)
#openAndClosedInRange(tasks, date1, date2)
#mostRecentTaskByInstanceId(tasks, 477)
#tasksByInstanceId(tasks, 634)
#openAndClosedTaskByAssignee(tasks, "dbailie")

