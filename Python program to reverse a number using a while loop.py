'''
# PRACTICAL NO.: 3(11)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to reverse a number using a while loop.
'''

#CODE-
n=int(input("Enter number:"))
digit=0
add=0
while n>0:
	digit=n%10
	add=(add*10)+digit
	n=n//10
print("Reverse=",add)

'''OUTPUT-
Enter number:13
Reverse= 31
'''