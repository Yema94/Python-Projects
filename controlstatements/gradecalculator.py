#Grade Calculation
"""Subjects: Maths, Physics, Chemistry
Pass Marks : 35
if Avg <=59 grade C
if Avg <=69 grade B
if Avg >69 grade A """

subjects = input("Enter the names of 3 subjects: ").split()
marks = [float(mark) for mark in input("Enter 3 subjects marks:").split(',')]
if marks[0]>=35 and marks[1]>=35 and marks[2]>=35 :
    print( "passed ")
    avg = sum(marks)/len(marks)
    if avg <=59 : print ("Grade C")
    elif avg <=69 : print("Grade B")
    else : print ("Grade A")
else : print("Failed!")