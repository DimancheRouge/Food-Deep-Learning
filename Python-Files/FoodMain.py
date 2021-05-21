import DLFood
import Reference
import os

def main():
    while (True):
        #Allow user to ID food, train new DL model, manage food library, exit
        print("--AUTOMATED DEEP LEARNING MICROWAVE SOFTWARE MANAGEMENT PROGRAM V1.0--")
        print("\t1) Identify Food")
        print("\t2) Train New Model")
        print("\t3) Manage Food Cooking Library")
        print("\t4) Exit")
        userInp = int(input("Enter desired choice: "))
        lnBreak()

        #ID food
        if (userInp == 1):
            imgName = input("Enter target file name: ") #INCLUDE EXTENSIONS
            modelName = input("Enter model file name: ") #INCLUDE EXTENSIONS
            
            detectedItem = DLFood.identify(imgName, modelName)
            lnBreak()

            report = Reference.logPull(detectedItem)
            print ("Food: {} | Time to cook (in sec): {} | Cooking Temperature (in C): {}".format(report[0], report[1], report[2]))
            lnBreak()

        #Train DL model
        elif (userInp == 2):
            epochs = int(input("Enter epoch count for training: "))
            modelNum = int(input("Enter model designation #: "))
            train = int(input("Enter training image count (PER CLASS): "))
            validate = int(input("Enter validation image count (PER CLASS): "))

            DLFood.train(epochs, modelNum, train, validate)
            lnBreak()

        #Manage food library
        elif (userInp == 3):
            #User choice for library management
            print("\t1) Generate Library")
            print("\t2) Add to Library")
            print("\t3) Reset Library")
            userInp = int(input("Enter desired choice: "))
            lnBreak()

            #Generate library
            if (userInp == 1):
                if (os.path.exists("FOOD-LIBRARY.txt")):
                    print("ERROR: Library already exists")
                else:
                    Reference.logInitiate()

            #Add item to library
            elif (userInp == 2):
                name = input("Enter food name: ")
                time = input("Enter time to cook food (in sec): ")
                temp = input("Enter temperature at which to cook food (in C): ")

                Reference.logItem(name, time, temp)

            #Reset Library
            elif (userInp == 3):
                if (os.path.exists("FOOD-LIBRARY.txt")):
                    Reference.logInitiate()
                    print("Library reset")
                else:
                    print("ERROR: Library doesn't exist")
                    
            lnBreak()

        #Exit
        elif (userInp == 4):
            break

#For my OCD
def lnBreak():
    print("=====================")

if __name__ == "__main__":
    main()
