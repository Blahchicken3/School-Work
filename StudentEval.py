#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

print('Hello! This program will calculate the average scores of three tests for each student, as well as the class average')

Test1 = []
Test2 = []
Test3 = []
Students = []
Count = int(0)
MoreStudents = 'Yes'

while MoreStudents in ['Yes', 'yes', 'YES']:
    print('')
    StudentName = input('Please enter student name: ')
    print('\033[A                                                           \033[A')
    Students.append(StudentName)
    print(StudentName)
    TestScore1 = float(input('Please enter their first test score: '))
    print('\033[A                                                           \033[A')
    Test1.append(TestScore1)
    print('Test one score:',TestScore1)
    TestScore2 = float(input('Please enter their second test score: '))
    print('\033[A                                                           \033[A')
    Test2.append(TestScore2)
    print('Test two score:',TestScore2)
    TestScore3 = float(input('Please enter their third test score: '))
    print('\033[A                                                           \033[A')
    Test3.append(TestScore3)
    print('Test three score:',TestScore3)
    AverageScore = (TestScore1+TestScore2+TestScore3)/3
    print('Average score for',StudentName,'is',round(AverageScore,2))
    Count = Count+1
    MoreStudents = input('Do you have another student? (Yes or No): ')
    print('\033[A                                                           \033[A')
    while MoreStudents not in ['Yes', 'yes', 'YES', 'No', 'no', 'NO']:
        print("Sorry, I didn't understand that. Try again.")
        MoreStudents = input('Do you have another student? (Yes or No): ')
        print('\033[A                                                           \033[A')
        print('\033[A                                                           \033[A')
if MoreStudents in ['No', 'no', 'NO']:
    print('')
    Test1Total = sum(Test1)
    Test1Average = Test1Total/Count
    print('The class average for test one is:',round(Test1Average,2))
    Test2Total = sum(Test2) 
    Test2Average = Test2Total/Count
    print('The class average for test two is:',round(Test2Average,2))
    Test3Total = sum(Test3)
    Test3Average = Test3Total/Count
    print('The class average for test three is:',round(Test3Average,2))
    ClassAverage = (Test1Average+Test2Average+Test3Average)/3
    print('The class average for all test is:',round(ClassAverage,2))