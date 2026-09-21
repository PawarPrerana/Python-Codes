'''
# PRACTICAL NO.: 2(8)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Academic Grade Calculator.
'''
#CODE-
print('ACADEMIC GRADE CALCULATOR')
print('90% to 100%:Grade O(OUTSTANDING')
print('75% to 89%:Grade A+')
print('60% to 74%:Grade A')
print('50% to 59%:Grade B')
print('40% to 49%:Grade C')
print('Below 40%:Fail')
percentage=float(input("Enter the student percentage:"))
if percentage>=90 and percentage<=100:
	print("Grade=Outstanding")
elif percentage>=75 and percentage<=89:
	print("Grade='A+'")
elif percentage>=60 and percentage<=74:
	print("Grade='A'")
elif percentage>=50 and percentage<=59:
	print("Grade='B'")
elif percentage>=40 and percentage<=49:
	print("Grade='C'")
elif percentage<=40:
	print("FAIL")
else:
	print("sorry")