import json
import Task
import Date

FILE_NAME = "task.json"




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
		if tasks_needed[i].isOpen:
			openCount = openCount + 1
		else:
			closedCount = closedCount + 1

	#return openCount, closedCount
	print "Open Count: ", openCount
	print "Closed Count: ", closedCount


def openAndClosedInRange(tasks, openDate, closeDate):

	#filter by openDate
	tasks_needed = []
	for i in range(len(tasks)):
		myDateCreate = tasks[i].createDate
		myDateClose = tasks[i].closeDate
		if myDateCreate.isEqual(closeDate) == -1:
			if myDateClose == None:
				tasks_needed.append(tasks[i])
			elif myDateClose.isEqual(openDate) == 0 or myDateClose.isEqual(openDate) == 1:
				tasks_needed.append(tasks[i])

	openCount = 0
	closedCount = 0
	for i in range(len(tasks_needed)):
		if tasks_needed[i].isOpen:
			openCount = openCount + 1
		else:
			closedCount = closedCount + 1

	#return openCount, closedCount
	print "Open Count: ", openCount
	print "Closed Count: ", closedCount

#most recent by createDate
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
	myTask.createDate.printDate()
	for i in range(len(tasks_needed)):
		myDate = myTask.createDate
		otherDate = tasks_needed[i].createDate
		otherDate.printDate()

		if otherDate.isEqual(myDate) == 1:
			myTask = tasks_needed[i]

	#return myTask.name
	print "Name: ", myTask.name


def tasksByInstanceId(tasks, instanceId):
	count = 0
	for i in range(len(tasks)):
		if tasks[i].instanceId == instanceId:
			count = count + 1

	#return count
	print "Number of Tasks : ", count

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

tasks = getTasksFromFile(FILE_NAME)
date1 = Date.Date("2010-11-22T21:33:19Z")
date2 = Date.Date("2014-11-22T21:33:19Z")
tasksByInstanceId(tasks, 634)
#openAndClosedTaskByAssignee(tasks, "dbailie")
#print date1.isEqual(date2)
#mostRecentTaskByInstanceId(tasks, 477)
#openAndClosedInRange(tasks, date1, date2)
currentOpenAndClosed(tasks, date2)
