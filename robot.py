import random
import time

#TODO: need to delete it /10 part of the tasks
# need to have all the robots do their tasks concurrently
# create leadership board
# think of some other functionality?
# move the interface part into a new file called main?

class Robot:
    tasks = {"do the dishes": 1, "sweep the house": 3, "do the laundry": 10, "take out the recycling": 4, "make a sammich": 7,
                "mow the lawn": 20, "rake the leaves": 18, "give the dog a bath": 14.5, "bake some cookies": 8, "wash the car": 20}
    taskKeys = list(tasks.keys())
    types = ["unipedal", "bipedal", "quadrupedal", "arachnid", "radial", "aeronautical"]

    def __init__(self, name, type):
        self.name = name;
        self.type = type; #string

    def showRobot(self):
        return self.name, self.type

    def assignTasks(self):
        taskList = []
        while len(taskList) < 5:
            n = random.randint(0, 9)
            if n not in taskList:
                taskList.append(n)
        return taskList

    def doingTasks(self):
        taskAssignments = self.assignTasks()

        for i in range(5):
            taskNum = taskAssignments[i]
            currTask = self.taskKeys[taskNum]
            taskTime = self.tasks[currTask]
            print(currTask,"- ETA: ", taskTime)
            time.sleep(taskTime/10)
        return "Finished tasks"

def acceptableTypes(userInput):
    types = ["unipedal", "bipedal", "quadrupedal", "arachnid", "radial", "aeronautical"]
    return userInput in types

##### INFERFACE
numRobots = int(input("Enter number of robots you'd like to create: "))
robotHomes = {}

for i in range(numRobots):

    botName = input("Enter robot name: ")
    print("Acceptable Robot Types: unipedal, bipedal, quadrupedal, arachnid, radial, aeronautical")

    botType = False
    while not acceptableTypes(botType):
        botType = input("Enter Acceptable Robot Type: ")

    userRobot = Robot(botName, botType)
    robotHomes[i] = userRobot

#complete robot tasks
for i in range(len(robotHomes)):
    currBot = robotHomes[i]
    print("Robot Name, Type: ", currBot.showRobot())
    print(currBot.doingTasks())
