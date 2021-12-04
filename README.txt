Hello! This is my Cars Program. All this program is designed to do, is calculate Horsepower and Torque for different cars based off of whatever the user inputs for Power and RPM.

The main Car class does all of the math. It has one set method and four get methods. 
The set method takes in a power and rpm input and sets the torque for the rest of the methods to use.
All of our get methods, minus get_hp() are just for use in the main() function, so that it is easier to print out to the text file that this program generates.
The get_hp() method actually does some math and returns the horsepower, the main deal. This is also printed out to the text file later on in our main() function.

Finally, our isfast() method is a conditional method. It will print out messages based on how much horsepower a given car has. If it is under 180, the program will print out "That's fast enough!" If the hp is more than 170 but less than 240, it will print out "OOooohhh wow that's fast :)" and finally, if it is more than 230 but less than 500 it will print out "Holy moly that is one fast car"

To use this program, all you have to do is go into the python file and changed the values where it is marked by comments. This should be on lines 37 and 38, in the main() function. The Car class takes one input of a string. The set_torq() method takes in two inputs, the first one being power and the second being RPM.

Then, just run the program in the terminal window and it should create a text file called "cars.txt" with all of the information in it :)

Enjoy!

-gena

