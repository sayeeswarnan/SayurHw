num_students = 3
num_marks = 2

for student in range(1, num_students + 1):
    input_data = input(f"Enter data for Student {student} (e.g., Student Name - Chitra, Mark1:55, Mark 2:67): ")
    
    # Split the input data into parts based on commas
    data_parts = input_data.split(',')
    
    # Extract student name
    student_name = data_parts[0].split('-')[1].strip()
    
    # Extract and parse the marks
    marks = []
    for mark_str in data_parts[1:]:
        mark_name, mark_value = mark_str.split(':')
        marks.append(float(mark_value))
    
    # Use string formatting to print the student's name and all their marks in the desired format
    print(f"{student_name}'s marks {' '.join(map(str, marks))}")
