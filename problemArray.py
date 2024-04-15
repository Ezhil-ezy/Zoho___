class array:

  array = [26, 22, 13, 25, 29, 5, 6, 1, 17, 9, 11, 23, 16 , 15, 11, 9, 4, 26, 6, 5, 9, 21]
  missing_number_array = [1, 5, 3, 7, 6, 2, 8, 7]
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

  def repeatingNumber(self):

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

if __name__ == '__main__':

  Obj = array()
  
  Obj.searchTarget()
  Obj.missingNumber()
  Obj.repeatingNumber()
  Obj.largestElement()
  Obj.smallestElement()
  Obj.largestElementAlgo()
  Obj.smallestElementAlgo()








  
