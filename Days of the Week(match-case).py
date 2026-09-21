'''
# PRACTICAL NO.: 2(9)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Days of the Week(match-case).
'''
#CODE-
print('Days of The Week')
print('1.Monday')
print('2.Tuesday')
print('3.Wednesday')
print('4.Thursday')
print('5.Friday')
print('6.Satursday')
print('7.Sunday')
day=int(input("Enter the number:"))
match day:
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6:
		print("Satursday")
	case 7:
		print("Sunday")
	case _:
		print("INVALID DAY NUMBER")	