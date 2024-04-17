# topics covered {sliding window, }

from problemArray import *
class arrayManipulation:

  tik = [2, 6, 3, 7, 1, 9, 5]
  tak = [25, 29, 5, 6, 23]

  def finalKthElement(self):

    tik = self.tik
    tak = self.tak
    ptr = Array.target
    tiktak = tik + tak
    # sorting........
    for idx in range(len(tiktak) - 1):
      for jdx in range(len(tiktak) - 1 - idx):
        if tiktak[jdx] > tiktak[jdx + 1]:
          tiktak[jdx], tiktak[jdx + 1] = tiktak[jdx + 1], tiktak[jdx]

    print(f'in the index of {ptr}, {tiktak[ptr]} is located')


  def findContigiousSubArray(self):

    array = self.tik
    x = Array.target
    sub_arr_values = []

    for idx in range(len(array) - (x - 1)):
      # print(array[idx: x + idx])
      total_sub_sum = sum(array[idx: x + idx])
      sub_arr_values.append(total_sub_sum)
    
    print(f'the maximum continous sub array is, {(max(sub_arr_values))}')
  
  def findMaxSubArray(self):

    array = self.tik
    x = Array.target
    dictionary, current_sum, maximum_sum = {}, 0, 0

    for idx in range(len(array)):
      current_sum += array[idx]

      if current_sum == x:
        maximum_sum = max(maximum_sum, idx + 1)
      
      reminder = current_sum - x
      if reminder in dictionary:
        maximum_sum = maximum_sum(maximum_sum, idx - dictionary[reminder])

      if current_sum not in dictionary:
        dictionary[current_sum] = idx
    
    print(maximum_sum)


    
    




if __name__ == '__main__':
  Obj = arrayManipulation()
  Obj.finalKthElement()
  Obj.findContigiousSubArray()
  