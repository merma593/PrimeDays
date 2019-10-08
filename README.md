COSC326 ETUDE 2

Prime Days

Markham Meredith

Takes input from the command line which is a single sequence of month lengths (always positive integers) separated by spaces and prints to stdout all the truly prime days of the corresponding calendar, one per line in the following format:
<number of day>: <number of month> <day of month>
  
For instance if you submitted a java program called App in a package called calendar
then the following input:
> java calendar.App 5 5 10
would produce the output:
7: 2 2
13: 3 3
17: 3 7


To run the code, cd to the primeDays.py folder in the terminal and in the terminal write e.g.  "python PrimeDays.py 5 5 10",
or however many arguments you want the program to use.

Some test cases i ran were:

5 5 10
5 5 10 3 2
5 5 12 13 4
2 3 10 2 6 7 8 9 10 23 12 9
5 5 106473 34321 53243
