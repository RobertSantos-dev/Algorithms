def max_num(nums):
    max_value = (0, 0)
    for i in nums:
        if (i[1] > max_value[1]):
            max_value = i
    if (int(max_value[1]) == 1):
        return False
    return int(max_value[0])


def find_duplicate(nums):
    if (not nums or len(nums) == 1):
        return False
    order_nums = {}
    for i in nums:
        if (type(i) == str or i < 0):
            return False
        elif (str(i) in order_nums):
            order_nums[f'{i}'] += 1
        else:
            order_nums[f'{i}'] = 1
    return max_num(list(order_nums.items()))
