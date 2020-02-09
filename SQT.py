# transfer the students.txt file to a list
fhandle=open('students.txt')
student_all=[]
for record in fhandle:
    record=record.rstrip()
    record=record.split('\t')
    student=[]
    for info in record:
        student.append(info)
    student_all.append(student)
print('student_all:',student_all)
