# konvertering med två decimaler.
#   1km = 0.62 miles
#   1mile = 1.61km

def km_to_miles(dist_km):
    dist_miles = dist_km * 0.62
    return dist_miles


def miles_to_km(dist_miles):
    dist_km = dist_miles * 1.61
    return dist_km


input_km_miles = input("Ange distans: ")

numbers_in_input = []
numbers_in_input = int()

if "km" in input_km_miles:
    for numbers in input_km_miles:
        if numbers.isdigit():
            numbers_in_input.append(numbers)
            km_to_miles(numbers_in_input)

print("*" * 25)
print(numbers_in_input)

