# cot-4500-as3
## Compilation Instructions
### assignment_3.py
In order to compile and run the file assignment_3.py type in the terminal:
- python3 src/main/assignment_3.py
  
then enter input according to [Input Instructions](https://github.com/ConnorTheKnight/cot-4500-as3/blob/main/README.md#input-instructions)
### test_assignment_3.py
In order to compile and run the file test_assignment_3.py type in the terminal:
- python3 src/test/test_assignment_3.py
  
## Input Instructions
When executing assignment_3.py the program will wait for user input, this can be provided either by piping input from a text file (add " < [Name of input file].txt" after the terminal command) or by manually entering input according to the format specified below (if using a text file, the text in the file should also follow this format)
### Input Formatting

[Function for f(y,t)]

[left bound for t] [right bound for t]

[number of Iterations]

[Initial Value]

[Number of unique variables in system of equations]

[Number of rows in the matrix for question 2 of 3b]

[Matrix for question 1 of 3b]

[Matrix for question 2 of 3b]

### Input Data Types
to avoid error in parsing please specify each parameter as the following data types
- write [Function for f(y,t)] as python compatible code
- write [left bound fot ti] as an Integer or Floating Point Number
- write [right bound fot ti] as an Integer or Floating Point Number
- write [number of Iterations] as an Integer
- write [Initial Value] as an Integer or Floating Point Number
- write [Number of unique variables in system of equations] as an Integer
- write [Number of rows in the matrix for question 2 of 3b] as an Integer
- write [Matrix for question 1 of 3b] as space separated Floating Point Numbers or Integers with a newline separating each row
- write [Matrix for question 2 of 3b] as space separated Floating Point Numbers or Integers with a newline separating each row
### Example Input

t-(y*y)

0 2

10

0

3

4

2 -1 1 6

1 3 1 0

-1 5 4 -3

1 1 0 3

2 1 -1 1

3 -1 -1 2

-1 2 3 -1


## Requirements.txt
Requirements.txt is not necessary for this program since no external libraries were used
