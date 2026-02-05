numbers = []
while True:
    value = input("Enter a number (press Enter to quit): ")
    if value == "":
    numbers.append(float(value))
if len(numbers) > 0:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")
