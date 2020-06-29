#GOAL IS TO PRINT THIS:
#xxxxx
#xx
#xxxxx
#xx
#xx

numbers = [5,2,5,2,2]
letters = ["x"]

for numbers in numbers:
    output  = ""
    for count in range(numbers):
        output += "x"
    print(output)

#for number in numbers:
#    for letter in letters:
#        print(int(number) * (letter))

#for number in numbers:
#    print("x" * int(number))

#unrelated
#for x in range(4):
#    for y in range (3):
#        print(f"{x}, {y}")