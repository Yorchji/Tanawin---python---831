while True:
    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Age must more than 0")
        elif age <=12:
            print("You are Child")
        elif age <=19:
            print("You are Teenager")
        elif age <=59:
            print("You are Adult")
        else:
            print("60+: Senior")
            break
    except ValueError:
        print("Invalid age")                