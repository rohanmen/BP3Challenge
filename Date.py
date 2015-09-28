
class Date:

	#timeString shoudl be in the format "YYYY-MM-DDTHH:MM:3SSZ"
	#keeps the same format as the time format given in the json files
	#
	#to create a new Date object, do the following:
	#d = Date("2014-10-13T23:32:32Z")
	#
	def __init__(self, timeString):

		date =  timeString.split("T")[0].split("-")
		time = timeString.split("T")[1].split("Z")[0].split(":")

		self.day = date[2]
		self.month = date[1]
		self.year = date[0]
		self.hour = time[0]
		self.minute = time[1]
		self.second = time[2]


	#returns 0 if self == otherDate
	#returns 1 if self > otherDate
	#returns -1 if self < otherDate
	def isEqual(self, otherDate):

		if(self.day == otherDate.day and self.month == otherDate.month and self.year == otherDate.year and
		   self.hour == otherDate.hour and self.minute == otherDate.minute and self.second == otherDate.second):
			return 0


		if self.year > otherDate.year:
			return 1 
		elif self.year < otherDate.year:
			return -1

		if self.month > otherDate.month:
			return 1
		elif self.month < otherDate.month:
			return -1

		if self.day > otherDate.day:
			return 1
		elif self.day < otherDate.day:
			return -1

		if self.hour > otherDate.hour:
			return 1
		elif self.hour < otherDate.hour:
			return -1

		if self.minute > otherDate.minute:
			return 1
		elif self.minute < otherDate.minute:
			return -1

		if self.second > otherDate.second:
			return 1
		elif self.second < otherDate.second:
			return -1



	def printDate(self):
	
		print self.year, self.month, self.day, self.hour, self.minute, self.second
	

