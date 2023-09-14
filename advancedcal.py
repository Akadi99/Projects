number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")
number3 = int(input("Enter the final number: "))

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))
final_number = int(round_number/number3)

print(number1)
print(number2)
print(round_number)
print(final_number)