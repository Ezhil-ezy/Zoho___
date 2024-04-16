from problemArray import *

# two pointer in array call be solved using both of the loops(for, while).


class ArrayTwoPointer:

  array = Array.array
  def twoSumDict(self):
  
    global array
    x = Array.target

    dictionary = {}
    for idx in array:
      if (x - idx) in dictionary:
        print(idx, end = ' ')
      dictionary[idx] = 1

  def twoSumAlgo(self):

    array = Array.array
    array.sort()
    x = Array.target
    left = 0
    right = len(array) - 1 

    while left < right:

      current_sum = array[left] + array[right]

      if current_sum == x:
        print('presented', array[left], array[right])
        break

      elif current_sum < x:
        right -= 1
  
      elif current_sum > x:
        left += 1

      else: 
        print('-1')

  def twoSumTwoLoop(self):

    array = Array.array
    x = Array.target
    for idx, first in enumerate(array):
      for jdx, secnd in enumerate(array):
        if first + secnd == x:
          print(first, end = ' ')
    else: print('two sum not found')
           
# note it is essential the array should be sorted before going into it.


  def threeSumAlgo(self):

    array = Array.array
    x = Array.target
    left = 0
    rgyt = len(array) - 1

    for idx in range(len(array)):
      current_sum = array[idx] + array[left] + array[rgyt]

      if current_sum == x:
        print('print')

  def fourSumAlgo(self):

    array = Array.array
    x = Array.target
    left = 0
    rgyt = len(array) - 1

    for idx in range(len(array)):
      for jdx in range(len(array)):
        current_sum = array[idx] + array[jdx] + array[left] + array[rgyt]

      if current_sum == x:
        print('print', x)

    print(array)    

  def tripletSum(self):

    array = Array.array
    n = len(array)

    for idx in range(n - 2):
      l, r = idx + 1, n - 1
      array.sort()
      while l < r:
        current_sum = array[idx] + array[l] + array[r]

        if current_sum == 0:
          print(array[idx], array[l], array[r])
          while array[l] == array[l + 1] and l < r:
            l += 1
          while array[r] == array[r- 1] and l < r:
            r -= 1
          l += 1
          r -= 1
        elif current_sum < 0: 
          l += 1
        else:
          r -= 1

      

Obj = ArrayTwoPointer()

# Obj.twoSumDict()
Obj.twoSumTwoLoop()
Obj.twoSumAlgo()
Obj.threeSumAlgo()
Obj.fourSumAlgo()
Obj.tripletSum()



    
    


