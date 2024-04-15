def reverse_digit(number: int):

  count_digit = 0
  while number > 0:
    # digit to fetch last digit by modulo the number.
    digit = number % 10
    # counter for the digit inc once for the iteration
    # to skip on the last digit
    number //= 10
    print(digit, end = '')

reverse_digit(54321) # 12345.