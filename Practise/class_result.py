#Class Performance
print("\n")
print(".........Welcome to the Class result 2025.......... \n \nFollow the instructions below \u2193 ")

#input to get the grades from the teacher
grades = input("Please enter the overall percentage of the students in your class separated by space %age: ").split()

#input test
# print(f"Output of input from the teacher is {grades}")

#convert the values of the grades into list of int values
grades = [int(grade) for grade in grades]

#Pass the Values in pass list if for every student who scored more than 50 marks, else marks goes to fail list
pass_list = []
fail_list = []

for grade in grades:
    if grade >= 50:
        pass_list.append(grade)
    else:
        fail_list.append(grade)

# print(f"Pass List: {pass_list}")
# print(f"Fail List: {fail_list}")

#Percentage each student represent in the class
total_students = len(grades)
percentage_per_student = round(100/total_students, 1)
# print(f"each student represents: {percentage_per_student}%")

#How may percentage of people passed and failed
total_students_passed = len(pass_list)*percentage_per_student
total_students_failed = len(fail_list)*percentage_per_student

if total_students_passed > total_students_failed:
    print(f"Good Job Class, {total_students_passed}% students passed")
else:
    print("Work Harder Class, Majority of you are fail")
