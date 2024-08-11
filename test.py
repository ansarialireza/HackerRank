#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
def gradingStudents(grades):
    
    round_num = lambda num : (((num // 5)+1)*5)
    for i in range(0,len(grades)):
        print(i)
        if grades[i] >= 38 :
            state = round_num(grades[i])-grades[i]
            if state < 3:
                grades[i]+=state
        
    return grades

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))

