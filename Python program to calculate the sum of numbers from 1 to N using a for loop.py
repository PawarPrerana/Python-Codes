'''
# PRACTICAL NO.: 3(6)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to calculate the sum of numbers from 1 to N using a for loop.
'''

#CODE-
N=int(input("Enter N:"))
sum=0
for i in range(N+1):
	sum=sum+i
print("SUM=",sum)

'''OUTPUT-
Enter N:13
SUM= 91
'''