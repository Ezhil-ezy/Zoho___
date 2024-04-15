# print all the divisior for the given number....
def numberDivisor(number: int):
  idx = 1

  while idx < number + 1:
    if number % idx == 0:
      print(idx, end = ' ')
    idx += 1
numberDivisor(10) 
# 1 2 5 10
