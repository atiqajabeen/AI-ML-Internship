balance=1000
while True:
    print(" 1. Check Balance")
    print(" 2. Deposit")
    print(" 3. Withdraw")
    print(" 4. Exit")

    choice=input("Enter your choice: ")
    if choice =='1':
        print("Current Balance:",balance)
    elif choice =='2':
        amount=int(input("Enter deposit amount:"))
        balance += amount
        print("Deposit Successful")
    elif choice == '3':
        amount=int(input("Enter withdrawal amount "))
        if amount<=balance:
            balance-=amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")
    elif choice == '4':
        print("Thankyou!")
        break
    else:
        print("Invalid Choice!")
    
    
    