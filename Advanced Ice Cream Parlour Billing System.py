'''
# PRACTICAL NO.: 2(5)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Advanced Ice Cream Parlour Billing System.
'''
#CODE-
#ICE CREAM PARLOUR
print('1.Vanilla')
print('2.Chocolate')
print('3.Strawberry')
print('4.Butterscotch')
print('5.Exit')

choice=int(input('enter the order number:'))
quantity=int(input('enter the quantity:'))

if choice==1:
  print('you order Vanilla with Rs.50/-')
  total=quantity*50
elif choice==2:
  	print('you order Chocolate with Rs.70/-')
  	total=quantity*70
elif choice==3:
	print('you order Strawberry with Rs.60/-')
	total=quantity*60
elif choice==4:
	print('you order Butterscotch with Rs.80/-')
	total=quantity*80
else:
	print("INVALID CHOICE")
if total>200:
	discount=total*25/100
else:
	discount=0
	
net_bill=total-discount
print("Total=",total)
print("Discount=",discount)
print("Net Bill=",net_bill)
	