from problemArray import *

# two pointer in array call be solved using both of the loops(for, while).


class ArrayTwoPointer:

  def twoSumDict(self):
  
    array = Array.array
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

    print('terminated')
           
# note it is essential the array should be sorted before going into it.

Obj = ArrayTwoPointer()

# Obj.twoSumDict()
Obj.twoSumAlgo()

    
    


