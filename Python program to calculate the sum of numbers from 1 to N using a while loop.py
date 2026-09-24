'''
# PRACTICAL NO.: 3(10)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) |  Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to calculate the sum of numbers from 1 to N using a while loop.
'''

#CODE-
N=int(input("Enter N:"))
i=1
sum=0
while i<=N:
	sum=sum+i
	i=i+1
print("SUM=",sum)

'''OUTPUT-
Enter N:13
SUM= 91
'''