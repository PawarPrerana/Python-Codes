'''
# PRACTICAL NO.: 2(6)
# COURSE CODE: CA - 214 (Practical based on Python Programming)
# CLASS: SYBCA (Semester-III) | Academic Year: 2026-2027
# NAME: PAWAR PRERANA SATISH
# TITLE: Simple Calculator using match-case.
'''
#CODE-
print("Simple Calculator using match-case")
print("Operator")
print("1.Addition(+)=a+b")
print("2.Subtraction(-)=a-b")
print("3.Multiplication(*)=a*b")
print("4.Division(/)=a/b")
val=int(input("enter the operator:"))
var1=float(input("enter the first number:"))
var2=float(input("enter the second number:"))

match val:
	case 1:
		ans=var1+var2
		print("Addition=",ans)
	case 2:
		ans=var1-var2
		print("Subtraction=",ans)
	case 3:	
	   ans=var1*var2
	   print("Multiplication=",ans)
	case 4:
	    ans=var1/var2
	    print("Division=",ans)
	case _:
	 	print("sorry")
	