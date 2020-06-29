weight = float(input(("Enter your Weight: ")))
unit = input(("Is this in 'lb' or 'kg'?"))

convert_kg_to_lb = round(weight * 2.2)
convert_lb_to_kg = round(weight / 2.2)

if unit == "kg":
    print(f" Your weight in lbs is: {convert_kg_to_lb}")

elif unit == "lb":
    print(f" Your weight in kg is: {convert_lb_to_kg}")

else:
    print("Invalid input.  Please enter weight in 'kg', 'kgs', 'kilograms' or 'lb', 'lbs', 'pounds'")




