'''
# PRACTICAL NO.: 2(7)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Leap Year Checker.
'''
#CODE-
print("LEAP YEAR CHECKER")
year=int(input("Enter a Year:"))
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 ==0:
			print("Year is Leap")
		else:
			print("Year is Not Leap")
	else:
		print("Year is Leap")
else:
	print("Year is Not Leap")		
			