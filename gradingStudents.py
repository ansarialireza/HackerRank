


def gradingStudents(grades):
    
    round_num = lambda num : (((num // 5)+1)*5)
    for i in range(0,len(grades)):
        print(i)
        if grades[i] >= 38 :
            state = round_num(grades[i])-grades[i]
            if state < 3:
                grades[i]+=state
        
    return grades
    
    
grades=[4,73,67,38,33]
grades=gradingStudents(grades)
print(grades)
