def get_op():
    op = int(input("1 - add student,\n 2- add subject,\n 3 - add rate,\n 4 - show all information,\n 5 - show student,\n 6 - exit\n"))
    return op   

def input_student():
    name = input("Write first and second name: ")
    return name
    
def input_less():
    less = input("Write lesson: ")
    return less
def get_mark():
    name = input("Write second name: ")
    less = input("Write lesson: ")
    mark = input("Write mark: ")
    return name,less,mark

def input_student_table():
    name = input("Write name student and I show you him mark: ")
    return name