#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    for i, head in enumerate(headings): 
        # Iterate through the headings and identify the columns for student number and mark (bug 1)
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = -1; 
    best_idx = None
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        if mark > best:
            # Assigned the best mark and the student number to the variables best and best_idx (bug 2)
            best=mark
            best_idx = data[num_col] 
    return best_idx, best

if __name__ == '__main__':
    f = open(sys.argv[1])
    num_col, mark_col = getCols(f)
    best_idx, best = findTop(f,num_col,mark_col)
    print("The top student was student %s with %d"%(best_idx,best))


