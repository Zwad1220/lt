Ziyad Khan

The program getbest.py should find the top student in the class (for simplicity we assume that
all marks are distinct, so that there are no ties). The data file consists of comma separated
values. The first line is a header line which could contain a number of arbitrary headings,
but you are guaranteed that two of the headings will be “Student Number” and “Mark”. In
different data files the order of the columns may differ, so your program has to find which
columns are the student number column and the mark column and then scan through the data
to find which student got the top mark. Your program then prints out the student number
and mark of the top student. You can assume that all data files are in the correct format.

Fixes were done in the dev branch by ensuring the column index increments appropriately. Additionally, the best_idx is now updated appropriately.

To run the code use: python getbest.py data.csv
To run the tests use: python getbest.py data.csv
