customer = {
    "name": "John",
    "age" : 30,
    "is_verified": True
}

print(customer["age"])


#CONVERT PHONE NUMBER TO TEXT

phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

output = ""
for ch in phone:
    # inserts a ! if item doesnt exist in dictionary
    output += digits_mapping.get(ch, "!")
print(output)
