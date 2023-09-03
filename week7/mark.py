######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

# for student in range (#FillinMissingCode):
#     #FillinMissingCode  to get studnet name
#     for mark in range (#FillinMissingCode):
#         inputMark = float (input(f"#FillinMissingCode")) #use formatted string
#         print (#FillinMissingCode)
            
no_of_students = 4#intializing student count
marks = 3#intializing marks

for student in range(1, no_of_students):#in this outer loop it took range as 1,2,3 not 4
    student_name = input(f"Enter name for Student {student}: ")
    
    for mark in range(1, marks):#in this inner loop it took range as 1,2 not 3
        input_mark = float(input(f"Enter Mark {mark} for Student {student}: "))
        print(f"Mark {mark} for {student_name} is {input_mark}")