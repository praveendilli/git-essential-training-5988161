print("Student Management System")
students=[]
n=int(input("Enter no. of. entries: "))
for i in range(n):
  j=input("Enter name: ")
  k=int(input("Student ID: "))
  l=float(input("Enter CGPA: "))
  students.append([j,k,l])

print(students)
