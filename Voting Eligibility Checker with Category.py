'''
# PRACTICAL NO.: 2(2)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Voting Eligibility Checker with Category.
'''
#CODE-
age=int(input("enter a person age:"))
if age <0:
	print("Invalid age")
elif age>0 and age<17:
	print("Not eligible to vote")
elif age>18 and age<59:
	print("Eligible to vote (Adult votet)")
else:
	print("Eligible to vote (Senior citizen voter)")
	