
class Task:

	def __init__(self, instanceName, dueDate, priority, closeDate, instanceStatus,
				 assigneeType, createDate, name, url, assignee, instanceId, status,
				 variables, processName, myId, isOpen):

		self.instanceName = instanceName
		self.dueDate = dueDate
		self.priority = priority
		self.closeDate = closeDate
		self.instanceStatus = instanceStatus
		self.assigneeType = assigneeType
		self.createDate = createDate
		self.name = name
		self.url = url
		self.assignee = assignee
		self.instanceId = instanceId
		self.status = status
		self.variables = variables
		self.processName = processName
		self.myId = myId
		self.isOpen = isOpen