def printval(i,n):
    if i<n:
        return
    print(i, end=" ")
    return printval(i-1,n)
i = int(input("Enter a number: "))
n = int(input("Enter a number: "))
printval(i,n)