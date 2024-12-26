#Class Performance

#input to get the grades from the teacher
grades = input("Please enter the grades separated by space: ").split()

#input test
print(f"Output of input from the teacher is {grades}")

#convert the values of the grades into int
grades = [int(grade) for grade in grades]

#Pass the Values in pass list if for every student who scored more than 50 marks, else marks goes to fail list
pass_list = []
fail_list = []

for grade in grades:
    if grade >= 50:
        pass_list.append(grade)
    else:
        fail_list.append(grade)

print(f"Pass List: {pass_list}")
print(f"Pass List: {fail_list}")

#Decide if most of the students passed or failed and generate a message for students
total_students = len(grades)
print(total_students)

#how much Percentage each student represents?
percentage_per_student = (total_students/100)*100
print(f"each student represents {percentage_per_student}%")

#How may percentage of people passed and failed
