'''
# PRACTICAL NO.: 2(4)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Find Greatest Among Three Numbers.
'''
#CODE-
print('GREATEST AMONG THREE NUMBER')
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b:
	if a>c:
		print("A is Big")
	else:
		print("C is Big")
else:
	if b>c:
		print("B is Big")
	else:
		print("C is Big")
