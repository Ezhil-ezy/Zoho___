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
