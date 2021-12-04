#Genevieve Trepte, Assignment 10.1
#This program will be able to answer questions about cars, and output a file that has all of this infomation in addition to the name of the car entered.

import sys

og_stdout = sys.stdout #setting the normal print format to print to terminal

class Car(object): #creating a class called car with a generic obj passed through
    def __init__(self, car, __torq = 0, __hp = 0): #init method, setting torq and hp to 0 to start, for continuity 
        self.car = car
        self.torq = __torq
        self.hp = __hp
    def set_torq(self, pwr, rpm): #this sets the torq to whatever the user inputs
        self.rpm = rpm
        self.pwr = pwr
        self.torq = ((9.5488 * pwr) / rpm) #where we actually set the self.torq
    def get_hp(self):
        return (self.torq * self.rpm) / 5252 #calculations for horsepower
    def get_torq(self): #method to grab the torq
        return self.torq
    def get_pwr(self): #method to grab the power
        return self.pwr
    def get_rpm(self):
        return self.rpm
    def name(self): #returns the name of the car inputted 
        return self.car
    def isfast(self): #conditional method, prints out a message based on what output the get_hp method returns
        if self.get_hp() <= 180: #basic logic if statement
            print("That's fast enough!")
        if self.get_hp() <= 240 and self.get_hp() >= 179:
            print("OOooohhh wow that's fast :)")
        if self.get_hp() <= 500 and self.get_hp() >= 239:
            print("Holy moly that is one fast car")

def main(): #defining our main function

    C = Car("1995 Mazda Miata") #                     ~  We change the arguments in these two when running the program  ~
    C.set_torq(5000, 6000) #                          ~  Miata is an example filler, but this can be changed to anything  ~

    name = C.name()
    hp = C.get_hp()
    with open('cars.txt', 'w') as cars: #now we are creating a text file with the name cars, and giving it a variable name cars
        sys.stdout = cars #setting the system print to print into the tex file
        print("The car you entered is: " + str(name)) #now we just print out our values and format it inside the text file
        print("")
        print("\tGiven Torque: " + str(C.get_torq()))
        print("\tGiven Power: " + str(C.get_pwr()))
        print("\tGiven RPM: " + str(C.get_rpm()))
        print("\tHorsepower: " + str(hp))
        print("")
        C.isfast()
        sys.stdout = og_stdout #making sure we go back to the og system print setting for contiuity 

if __name__== "__main__": #calling our main function
    main()


