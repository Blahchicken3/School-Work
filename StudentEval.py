#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

#Welcome message
print('Hello! This program will calculate the average scores of three tests for each student, as well as the class average')

#Set initial values
Test1 = []
Test2 = []
Test3 = []
Students = []
Count = int(0)
MoreStudents = 'Yes'

#Loop until the user says there are no more students
while MoreStudents in ['Yes', 'yes', 'YES']:
    print('')
    #Ask for student name
    StudentName = input('Please enter student name: ')
    print('\033[A                                                           \033[A')
    #Add student name to "StudentName" list
    Students.append(StudentName)
    #Outputs student name
    print(StudentName)
    #Ask for test 1 score
    TestScore1 = float(input('Please enter their first test score: '))
    print('\033[A                                                           \033[A')
    #Adds score 1 to "TestScore1" list
    Test1.append(TestScore1)
    #Outputs test score 1
    print('Test one score:',TestScore1)
    #Ask for test 2 score
    TestScore2 = float(input('Please enter their second test score: '))
    print('\033[A                                                           \033[A')
    #Adds score 2 to "TestScore2" list
    Test2.append(TestScore2)
    #Outputs test score 2
    print('Test two score:',TestScore2)
    #Ask for test 3 score
    TestScore3 = float(input('Please enter their third test score: '))
    print('\033[A                                                           \033[A')
    #Adds score 3 to "TestScore3" list
    Test3.append(TestScore3)
    #Outputs test score 3
    print('Test three score:',TestScore3)
    #Calculates the average score for this student
    AverageScore = (TestScore1+TestScore2+TestScore3)/3
    #Outputs the average score for this student
    print('Average score for',StudentName,'is',round(AverageScore,2))
    Count = Count+1
    #Asks the user if there are any more students
    MoreStudents = input('Do you have another student? (Yes or No): ')
    print('\033[A                                                           \033[A')
    #Loop to make sure the input is valid
    while MoreStudents not in ['Yes', 'yes', 'YES', 'No', 'no', 'NO']:
        print("Sorry, I didn't understand that. Try again.")
        MoreStudents = input('Do you have another student? (Yes or No): ')
        print('\033[A                                                           \033[A')
        print('\033[A                                                           \033[A')
#Exit first loop
if MoreStudents in ['No', 'no', 'NO']:
    print('')
    #Calculates the test 1 class average and then outputs
    Test1Total = sum(Test1)
    Test1Average = Test1Total/Count
    print('The class average for test one is:',round(Test1Average,2))
    #Calculates the test 2 class average and then outputs
    Test2Total = sum(Test2) 
    Test2Average = Test2Total/Count
    print('The class average for test two is:',round(Test2Average,2))
    #Calculates the test 3 class average and then outputs
    Test3Total = sum(Test3)
    Test3Average = Test3Total/Count
    print('The class average for test three is:',round(Test3Average,2))
    #Calculates the class average for all tests and then outputs
    ClassAverage = (Test1Average+Test2Average+Test3Average)/3
    print('The class average for all test is:',round(ClassAverage,2))