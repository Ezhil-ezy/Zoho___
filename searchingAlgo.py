# searching algorithm _________________

class searchingAlgorithm:
  
  # Linear Search: Sequentially checks each element in the collection 
  # until the target element is found or the end of the collection is reached.
  def linearSearch(self, array, n, k):

    # using for loop
    if k in array:
      for idx in range(n):
        if array[idx] == k:
          return f'Target element {k} is presented in position of {idx + 1}'
    else:
      return f'Target element {k} is not found'
    
    # using while loop
    if k in array:
      idx = 0 
      while idx < n:
        if array[idx] == k:
          return f'Target element {k} is presented in position of {idx + 1}'
        idx += 1
    else:
      return f'Target element {k} is not found'
    

if __name__ == '__main__' :
  number = int(input('Enter the length of the array:\t'))
  target = int(input('Enter the target element of the array :\t'))
  array = list(map(int, input().strip().split()))
  obj = searchingAlgorithm().linearSearch(array, number, target)
  print(obj)
  