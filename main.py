import robot

def acceptableTypes(userInput):
    types = ["unipedal", "bipedal", "quadrupedal", "arachnid", "radial", "aeronautical"]
    return userInput in types

## run script and actions
numRobots = int(input("Enter number of robots you'd like to create: "))
robotHomes = {}

for i in range(numRobots):

    botName = input("Enter robot name: ")
    print("Acceptable Robot Types: unipedal, bipedal, quadrupedal, arachnid, radial, aeronautical")

    botType = False
    while not acceptableTypes(botType):
        botType = input("Enter Acceptable Robot Type: ")

    userRobot = robot.Robot(botName, botType)
    robotHomes[i] = userRobot

#complete tasks
for i in range(len(robotHomes)):
    currBot = robotHomes[i]
    print("Robot Name, Type: ", currBot.showRobot())
    print(currBot.doingTasks())
