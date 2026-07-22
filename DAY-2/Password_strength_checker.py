password = input("Enter Password: ")

if len(password) >= 8:
    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True

    if upper and lower and digit:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Password must contain at least 8 characters.")