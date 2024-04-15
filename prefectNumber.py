def perfectNumber(number):

  idx = 1
  count = 0
  while idx < number:
    if number % idx == 0:
      count += idx
    idx += 1
      
  if count == number:   print(f'{number} is a perfect number.')
  else:                 print(f'{number} is a not perfect number.')
  

perfectNumber(16)
perfectNumber(6)