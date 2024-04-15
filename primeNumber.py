# find prime numbers

def findPrime(number):
  if number <= 1:
    print('its not a prime number')
  elif number >= 2:
    for idx in range(2, number):
      if number % idx == 0:
        print(f'{number} is not a prime number.')
        break
    else:
      print(f'{number} is a prime number.')
findPrime(21)