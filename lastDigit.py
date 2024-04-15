# print the last digit of the number using while loop.

number = int(input('Input number is:\t'))
while number > 0:
  # digit to fetch last digit by modulo the number.
  digit = number % 10
  print(digit)
  break