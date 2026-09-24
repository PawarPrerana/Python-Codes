'''
# PRACTICAL NO.: 3(12)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to count the number of digits in a number.
'''

#CODE-
n=int(input("Enter number:"))
digit=0
while n>0:
	n=n//10
	digit=digit+1
print("Number of digit=",digit)

'''OUTPUT-
Enter number:13
Number of digit= 2
'''