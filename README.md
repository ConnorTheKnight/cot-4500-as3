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

[left bound fot ti] [right bound fot ti]

[number of Iterations]

[Initial Value]

### Input Data Types
to avoid error in parsing please specify each parameter as the following data types
- write [Function for f(y,t)] as python compatible code
- write [left bound fot ti] as an Integer or Floating Point Number
- write [right bound fot ti] as an Integer or Floating Point Number
- write [number of Iterations] as an Integer
- write [Initial Value] as an Integer or Floating Point Number
### Example Input

t-(y*y)

0 2

10

0

## Requirements.txt
Requirements.txt is not necessary for this program since no external libraries were used
