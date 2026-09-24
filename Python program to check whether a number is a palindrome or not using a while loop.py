'''
# PRACTICAL NO.: 3(14)
# COURSE CODE: CA - 214 (Practical  based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to check whether a number is a palindrome or not using a while loop.
'''

#CODE-
n=int(input("Enter  number:"))
add=0
temp=n
while n>0:
	r=n%10
	add=(add*10)+r
	n=n//10
if temp==add:
	print("Number palindrome")
else:
	print("Number not palindrome")
	
'''OUTPUT-
Enter  number:313
Number palindrome
'''