
class mustSolve:

  def majorityElement(self, array, length):

    dictionary = {}
    for element in array:
      if element not in dictionary: dictionary[element] = 1
      else:                         dictionary[element] += 1

    for idx in dictionary:
      if dictionary[idx] > length / 2:
        print(f'the majority element in an array is {dictionary[idx]}')
      
    return True
    
def main():

  t = int(input('test cases :\t'))
  while t > 0:

    length = int(input('length of an array :\t'))
    print('Enter your array elements :')
    array  = [int(idx) for idx in input().strip().split()]
    object = mustSolve()
    print(object.majorityElement(array, length))

    t -= 1

if __name__ == '__main__':
  main()

