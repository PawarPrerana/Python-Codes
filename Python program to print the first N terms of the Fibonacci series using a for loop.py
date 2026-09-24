'''
# PRACTICAL NO.: 3(17)
# COURSE CODE: CA - 214 (Practical  based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to print the first N terms of the Fibonacci series using a for loop.
'''

#CODE-
level=int(input("Enter the level number:"))
a=0
b=1
print(a)
print(b)
for i in range(level):
	c=a+b
	print(c)
	a=b
	b=c
	
'''OUTPUT-
Enter the level number:13
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
'''