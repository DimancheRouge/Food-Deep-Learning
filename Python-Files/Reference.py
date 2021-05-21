#Create and write header for cook book file
def logInitiate():
    file = open("FOOD-LIBRARY.txt", "w")
    file.write("Food | Cook Time (sec) | Temperature (C)\n")
    file.close()

#Add item to cook book
def logItem(name, time, temp):
    file = open("FOOD-LIBRARY.txt", "a")
    file.write("{} {} {}\n".format(name, time, temp))
    file.close()

#Pull requested item from cook book (returns list)
def logPull(name):
    with open("FOOD-LIBRARY.txt", "r") as file:
        for line in file:
            for word in line.split():
                if (word == name):
                    file.close()
                    return line.split()
