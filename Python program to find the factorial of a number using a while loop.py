'''
# PRACTICAL NO.: 3(16)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to find the factorial of a number using a while loop.
'''

#CODE-
n=int(input("Enter number:"))
fact=1
i=1
while i<=n:
	fact=fact*i
	i=i+1
print("Factorial=",fact)

'''OUTPUT-
Enter number:5
Factorial= 120
'''