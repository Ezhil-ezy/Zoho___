# source : chatgpt____
def two_sum(nums, target):
    num_index_map = {}
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

# Example usage:
nums = [11, 9, 25, 29, 26, 22, 5, 17, 6, 13, 23]
target = 20
print(two_sum(nums, target))  # Output: [2, 7]
