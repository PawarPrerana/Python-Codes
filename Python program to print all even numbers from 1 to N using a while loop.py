'''
# PRACTICAL NO.: 3(9)
# COURSE CODE: CA - 214 (Practical  based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to print all even numbers from 1 to N using a while loop.
'''

#CODE-
N=int(input("Enter N:"))
i=1
while i<=N:
	i=i+1
	if i%2==0:
		print(i)
		
'''OUTPUT-
Enter N:13
2
4
6
8
10
12
14
'''