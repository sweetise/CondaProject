try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("Can't divide by zero fool")