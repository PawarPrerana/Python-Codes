'''
# PRACTICAL NO.: 3(13)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to find the sum of all digits of a number.
'''

#CODE-
n=int(input("Enter number:"))
count=0
while n>0:
	count=count+1
	n=n//10
print("SUM=",count)

'''OUTPUT-
Enter number:13
SUM= 2
'''