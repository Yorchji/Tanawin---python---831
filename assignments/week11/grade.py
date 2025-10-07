"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

passing_grade = 50

def input_students(num_students):
    students = [
        {
            'name': 'Tanawin',
            'scores': [56, 75, 45]
        },
        {
            'name': 'Benz',
            'scores': [85, 55, 45]
        },
    ]
    return students

def calculate_averages(student):
    for student in students:
        sum = 0 
        for score in student['scores']:
            sum = sum + score
        student['average'] = sum / 3
       
        return students
    
def display_results(students):
   for student in students:
      print("Name:", student['name'])
      print("Average: %.1f" % student['average'])
      if student['average'] > passing_grade:
         print("Status: PASS")
      else:
         print("Status: FAIL")

students_list = input_students()
students_list = calculate_average(students_list)
display_results(students_list)