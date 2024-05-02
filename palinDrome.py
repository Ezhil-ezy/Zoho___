'''
def is_palindrome(num):
    # Store the original number
    original_num = num
    
    reverse_num = 0
    
    while num > 0:
        digit = num % 10  # Extract the last digit
        reverse_num = reverse_num * 10 + digit  
        num = num // 10 

    return original_num == reverse_num

num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
# chatgpt

# using slicing method.

number = input('enter your number:\t')

reversed_number = number[::-1]
if reversed_number == number:
  print('palindrome')
else:
  print('not')

'''

#  palindrome algorithm for a string:

def strPalindrome(string):
    # easy method by slicing.
    return string == string[::-1]
obj = strPalindrome('palindrome')
new = strPalindrome('malayalam')
# print(obj, new)


# by using indexing method.
def strPalindrome(string):
    
    mid = len(string) // 2 
    if len(string) % 2 != 0:
        # print('even')
        print(string[:mid + 1], string[mid :][::-1])
        return string[:mid + 1] == string[mid :][::-1]
    else:
        # print('odd')
        print(string[:mid], string[mid:][::-1])
        return string[:mid] == string[mid:][::-1]

print(strPalindrome('malayalam'))
print(strPalindrome('boob'))