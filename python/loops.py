while True:
    print("\n1. Print numbers 1 to n")
    print("2. Print even numbers in range n")
    print("3. Print sum of n natural numbers")
    print("4. Count digits in a number")
    print("5. Print multiplication table")
    print("6. EXIT")
    
    option = input("enter your choice: ")
    
    if option == '1':
        n = int(input("enter a number to print numbers from 1 to n: "))
        for i in range(1, n + 1):
            print(i)
    elif option == '2':
        n = int(input("enter a number to print even number in range n: "))
        for i in range(1, n + 1):
            if(i % 2 == 0):
                print(i)
    elif option == '3':
        sum_val = 0 
        n = int(input("enter range n for sum: "))
        for i in range(1, n + 1):
            sum_val = sum_val + i
        print(sum_val)
    elif option == '4':
        count = 0
        n = int(input("enter a number: "))
        if n == 0: count = 1 
        while n > 0:
            n = n // 10
            count += 1
        print(count)
    elif option == '5':
        n = int(input("enter a number to print the table: "))
        for i in range(1, 11):
            print(f"{n} * {i} = {n*i}")
    elif option == 'exit' or option == '6': 
        print("exiting program")
        break
    else:
        print("invalid choice")