def sum_of_odd_and_even(nums):
    result = [0, 0]
    for num in nums:
        if num % 2 == 0:
            result[0] += num
        else:
            result[1] += num
    return result