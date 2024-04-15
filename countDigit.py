def count_digit(number: int):

  count_digit = 0
  while number > 0:
    # digit to fetch last digit by modulo the number.
    digit = number % 10
    # counter for the digit inc once for the iteration
    count_digit += 1
    # to skip on the last digit
    number //= 10

  return count_digit

print(count_digit(54321))


