
from problemArray import *
class arrayManipulation:

  tik = [22, 26, 13, 17, 11, 9, 5]
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

    print(tiktak[ptr], tiktak)
    


if __name__ == '__main__':
  Obj = arrayManipulation()
  Obj.finalKthElement()
  