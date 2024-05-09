# searching algorithm _________________

class searchingAlgorithm:
  def searching(self, array, n, k):
    pass
if __name__ == '__main__' :
  n = int(input('Enter the length of the array:\t'))
  k = int(input('Enter the target element of the array:\t'))
  array = list(map(int, input().strip().split()))
  obj = searchingAlgorithm().searching(array, n, k)
  print(obj)
  