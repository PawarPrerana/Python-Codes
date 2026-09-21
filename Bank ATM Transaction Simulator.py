'''
# PRACTICAL NO.: 2(10)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Bank ATM Transaction Simulator.
'''
#CODE-
print("Simulate a simple ATM")
balance=5000
print("Amount Balance=",balance)
pin=int(input("Please enter your 4(four) digit pin:"))
if pin == 1234:
	print("1.Check Balance")
	print("2.Withdraw Money")
	select=int(input("Choose option:"))
	if select == 1:
		print(balance)
	elif select == 2:
		choice=int(input("Enter your amount:"))
		if choice<balance:
			x=balance-choice
			print("Withdraw Successful!")
			print("Remaining Balance:",x)
		else:
			print("Insufficient Funds")
	else:
		print("Please select above options")
else:
	print("Incorrect PIN.Access Denied.")	