# BP3Challenge

#First get the tasks from the json file
tasks = getTasksFromFile(FILE_NAME)

#Example on how to create Date objects
Argument for creating a Date object follows the format "YYYY-MM-DDTHH:MM:3SSZ"

date1 = Date.Date("2015-02-22T22:24:57Z")

date2 = Date.Date("2014-12-22T21:33:19Z")

#Example on how to run the methods
currentOpenAndClosed(tasks, date1)

openAndClosedInRange(tasks, date1, date2)

mostRecentTaskByInstanceId(tasks, 477)

tasksByInstanceId(tasks, 634)

openAndClosedTaskByAssignee(tasks, "dbailie")
