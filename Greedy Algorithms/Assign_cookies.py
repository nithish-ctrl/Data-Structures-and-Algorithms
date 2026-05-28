
def Assign_cookies(student, cookies):
    student.sort()
    cookies.sort()
    assigned = 0
    student_iter = 0
    cookie_iter = 0
    while student_iter<len(student) and cookie_iter<len(cookies):
        if student[student_iter] <= cookies[cookie_iter] : 
            assigned+=1
            student_iter+=1
        cookie_iter+=1
    return assigned  # assigned and student_index will be same so technically assigned is not required

    

Student = [1, 2, 3]
Cookie = [1, 1]
print(Assign_cookies(Student, Cookie))

Student = [1, 2] 
Cookie = [1, 2, 3]
print(Assign_cookies(Student, Cookie))