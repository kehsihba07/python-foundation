inpput=int(input("enter 1 for even odd check: \n enter 2 for positive negative check: \n enter 3 for  pass fail check: \n enter 4 to check largest: "))
if inpput==1:
    num=int(input("enter number for even odd check:"))
    if (num%2==0):
        print("it is a even number")
    else:
        print("it is a odd number")
elif inpput==2:
    num2=int(input("enter a number to check if it a positive or a negative number: "))
    if num2>0:
        print("it is a postive number")
    elif num2<0:
        print("it is a negative number")
    else:
        print("it is zero")
elif inpput==3:
    marks=int(input("enter marks to check pass or fail:"))
    if marks>=40:
        print("pass")
    else:
        print("fail")
elif inpput==4:
    a=int(input("enter a number"))
    b=int(input("enter another number"))
    c=int(input("enter another number"))
    if a>=b and a>=c:
        print("a is largest")
    elif b>=c and b>=a:
        print("b is largest")
    else:
        print("c is largest")
else:
    print("invalid input")
