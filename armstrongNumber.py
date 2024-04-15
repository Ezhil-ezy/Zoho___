# armstrong number cubing every digit of the number and sumed up together.
# if same to the given number is armstrong.

def armstrong_number(number):
  dummy = number
  sum = 0
  while dummy > 0:
    digit = dummy % 10
    sum += (digit ** 3)
    dummy //= 10
  
  return sum == number

print(armstrong_number(153))

