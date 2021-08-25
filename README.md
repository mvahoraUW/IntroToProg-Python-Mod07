# IntroToProg-Python-Mod07

  
Moiz Vahora
08/24/2021
IT FDN 110 A
Assignment 7
https://github.com/mvahoraUW/IntroToProg-Python-Mod07


# Working with Exception Handling and Pickles
## Introduction
The purpose of this assignment is to research exception handling and the pickle module along with showing an application of the two concepts for this assignment. The program written for this assignment is rather simple for the purpose of demonstration, but it showcases the concepts rather well, The program will ask the user for 2 numbers which will be divided and then stored into a pickled file for future reference. As division can lead to a divide by zero error this is a good example of exception handling, this program checks the user input for errors and then stores the results in a pickled file. 

## Exception Handling
Exception handling is a relatively straightforward concept as the creator of the programs wants to ensure their program does not crash or cause problems due to erroneous usage. The following links were a useful resource in regards to explaining exception handling as they give a good high level summary for a beginer that is easy to understand. 
The first link tells us about the different types of exception errors that are built into python and how to view them using the following command “print(dir(locals()['__builtins__']))” which lists out the built in exceptions, functions, and attributes. The second link gives examples of how the exceptions are used in a program and it gives a good brief summary of how to catch exceptions using a variety of methods with the try clause. The pseudo code given by this examples are helpful as they can be modified and implemented into the users program as the develop and refine their code. 
https://www.programiz.com/python-programming/exceptions
https://www.programiz.com/python-programming/exception-handling




## Pickles
Pickling is a very interesting concept that takes data/objects in python and converts it into a serial format for later usage. It is a very useful concecpt as it allows us to read files without having to go through too much of a hassle of trying to parse or sort through a text file and format it into a dictionary. This makes loading the file into Python much easier as you do not need to go through the hassle of setting up loops to read the file and store them locally into a dictionary like the previous assignments. This was explained in the first video link as it gives a good high level summary of pickling and its use case. The first two links give us some examples of how to use the pickle module and some example usages. The third link is from the python website which also provides a decent high level summary and it also dives into the specifics of the module which can be useful for more advanced users as they become more proficient with python. 
https://www.youtube.com/watch?v=Pl4Hp8qwwes
https://www.geeksforgeeks.org/understanding-python-pickling-example/
https://docs.python.org/3/library/pickle.html


## Steps Taken
These are the step-by-step tasks taken by the author of the code to demonstrate exception handling and pickling. This program takes two numbers imputed by the user, divides them, and then saves the results to a “.pkl” file. The steps 
  1.	Import the pickle module for the program. 
  2.	Take user imputed with exception handling implemented to prevent the program from taking in strings or none inputs. The program will display the error and exit. 
  3.	The user input is divided and calculation is conducted under an exception handle to prevent any divide by zero errors. Alternatively we could catch the exception during the       input step above if we verify the input is none zero using the handles.
  4.	The input data and the calculation is then placed inside of a dictionary
  5.	The dictionary is then “pickled” and saved to the “data_pick.pkl” file. 
  6.	The “pickled” file then loaded and “un-pickled” into the program as a dictionary.
  7.	The first dictionary and “un-pickled” entries are then displayed to the user using a print function. 

## Python Code
See file attached, it does not format well on the webpage...

## Pycharm Display

### General Run

![image](https://user-images.githubusercontent.com/88759658/130723963-be19490d-f26a-4677-a4f8-af6252ae3ba0.png)

### With exceptions

![image](https://user-images.githubusercontent.com/88759658/130724031-0456842e-1a5c-46a2-9aa6-5cf3e4da7806.png)
![image](https://user-images.githubusercontent.com/88759658/130724045-1d1174e1-1584-4861-96e1-cf8dd86207de.png)

## Command Prompt Display

![image](https://user-images.githubusercontent.com/88759658/130724072-933c555b-18ab-4e7b-832b-ff24f698fd49.png)

## Pickled Text

€#•H       }”(Œ	Numerator”G?ð      Œ#Denominator”G@       Œ#Calculation”G?à      u.
![image](https://user-images.githubusercontent.com/88759658/130724118-a2eeec94-6bc7-4a21-9a9c-36df7217ec85.png)

## Conclusion
The script written for this assignment takes uses exception handling to ensure no erroneous input is being given by the user of the program and the program can take their input, a calculation, and then save it into a pickled file for later use. The program also reloads the pickled data and shows there is not difference to the data. 



