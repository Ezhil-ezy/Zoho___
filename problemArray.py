class Array:

  array = [26, 22, 13, 25, 29, 5, 6, 1]
  missing_number_array = [1, 5, 3, 7, 6, 2, 8, 7]
  a = [3, 4, 2, 5, 1]
  b = [5, 3, 1, 4, 2]

  target = int(input('enter your target value:\t'))

  def largestElement(self):
    print('the largest element is : ', max(self.array))
  
  def smallestElement(self):
    print('the smallest element is : ', min(self.array))

  def largestElementAlgo(self):
    array = self.array
    maximum = array[0]
    for idx in range(1, len(array)):
      if array[idx] > maximum:
        maximum = array[idx]

    print('the largest element is : ', maximum)     
        
  def smallestElementAlgo(self):
    array = self.array
    minimum = array[0]
    for idx in range(1, len(array)):
      if array[idx] < minimum:
        minimum = array[idx]

    print('the smallest element is : ', minimum)  

  def searchTarget(self):

    k = self.target
    array = self.array

    if k in array:
      for idx, value in enumerate(array):
        if k == value:
          print(f'the element present in the place of :', idx)

    else: print(f'the element {k} which is not present in an array')

  def missingNumber(self):

    array_ = self.missing_number_array
    maximum = max(array_)
        
    for idx in range(1, maximum):
      if idx not in array_:
        print(f'the missing number is : ', idx)

  # using dictionary repeating_____
  def repeatingNumberDict(self):

    array = self.array
    dictionary = {}
    duplicates = []
    for idx in array:
      if idx not in dictionary:   dictionary[idx] = 1 
      else:                       dictionary[idx] += 1
    
    for values in dictionary:
      if dictionary[values] > 1:
        duplicates.append(values)
    
    print(f'the duplicates elements are ', duplicates)
  # using list  repeating_____
  
  def sortingAlgo(self):
    
    array = self.array
    # bubble_sort_____
    for idx in range(len(array) - 1):
      for jdx in range(len(array) - 1 - idx):
        if array[jdx] > array[jdx + 1]:
          array[jdx], array[jdx + 1] = array[jdx + 1], array[jdx]
      
    print('the sorted array is :', *array, sep = ' ') 
    # its applicable for every sorting questions.....

  def arrayCheck(self):

    array = self.a
    check = self.b

    if sorted(array) == sorted(check):  print('this matches')
    else:                               print('not matched')
  
  def rotateArrayPop(self):

    array = self.array
    last  = array.pop()

    print('rotating by one ', [last] + array)

  def rotateArraySlice(self):

    array = self.array
    k = self.target
    print('rotating by k ', array[k:] + array[:k])
    print('rotating by one ', array[-1:] + array[:-1])

    


#---------------------------------------------------------------------->
if __name__ == '__main__':

  Obj = Array()

  Obj.arrayCheck()
  Obj.rotateArrayPop()
  Obj.rotateArraySlice()
  Obj.sortingAlgo()
  Obj.searchTarget()
  Obj.missingNumber()
  Obj.repeatingNumberDict()
  Obj.largestElement()
  Obj.smallestElement()
  Obj.largestElementAlgo()
  Obj.smallestElementAlgo()