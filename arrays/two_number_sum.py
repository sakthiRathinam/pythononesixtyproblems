#dict method
#O(N) time complexity and O(N) space complexity
def solution_one(array:int,target_sum:int):
    target_map = {}
    for arr in array:
        remind_sum = target_sum - arr
        if remind_sum in target_map:
            return [arr,remind_sum]
        target_map[arr] = True
    return []

#array sorting and left right pointer method
#O(nlogn) time complexity and O(1) space complexity

def solution_two(array,target_sum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        two_sum = array[right] + array[left]
        if two_sum == target_sum:
            return [array[right],array[left]]
        if two_sum > target_sum:
            right -= 1
        else:
            left += 1
    return []




