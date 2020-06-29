#names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
#names[0] = "Jon"
#print(names)

numbers = [1,2,27,4,5]
print(max(numbers))

#Or

numberlist = [1,2,27,4,5]
largest_number = numberlist[0]
for number in numberlist:
    if number > largest_number:
        largest_number = number
print(largest_number)
