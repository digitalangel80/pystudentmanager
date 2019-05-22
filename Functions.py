students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(students)
        return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id = 332):
    student = {"name": name, "student_id": student_id}
    students.append(name)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('Could not read file')


read_file()
print_students_titlecase()

students_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(students_name, student_id)
save_file(students_name)
