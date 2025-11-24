###file=open("stock_data.csv","r")
'''print(file.read())
file.close()


empty =(1,2, 3,4,)

print(type(empty))

print(list(empty))

diff_data_ypes ="sumithra",12,True
a,b,c=diff_data_ypes
print(a)
print(b)
print(c)

a={12,23,45,56,67}
b={23,56,78,90,56}

set=a.union(b)
print(set)

set_intersection=a.intersection(b)
print(set_intersection)'''

a={12,23,45,56,67}
b={23,56,78,90,56}

a.intersection(b)
print(a)

print(type(a))
c={}
print(type(c))


student={"name":"sumithra","age":34,"father_name":"guna "}
print(student)
student_copy=student
print(student)

print(student_copy)

student_copy=student.copy()
student["name"]="sumithra1"
print(student)

print(student_copy)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for value,key in student.items():
    print(value,key)


students={
     "student1":{"name":"nisha" ,"age":"45"},
     "student2":{"name":"shivasharan" ,"age":"89"}
 }
print(students)
print(students ["student1"]["name"])
print(students ["student1"]["age"])
squares={x:x**2 for x in range (5)}
print(squares)