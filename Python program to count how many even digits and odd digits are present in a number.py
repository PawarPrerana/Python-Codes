'''
# PRACTICAL NO.: 3(15)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Write a Python program to count how many even digits and odd digits are present in a number.
'''

#CODE-
n=int(input("Enter number:"))
even=0
odd=0
while n>0:
	digit=n%10
	if digit%2==0:
		even=even+1
	else:
		odd=odd+1
	n=n//10
print("Even digits=",even)
print("Odd digits=",odd)

'''OUTPUT-
Enter number:13
Even digits= 0
Odd digits= 2
'''