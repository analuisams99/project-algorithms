def find_duplicate(nums):
    num_dict = dict()

    for num in nums:
        if type(num) != int or num < 0:
            return False

        if num not in num_dict:
            num_dict[num] = 1

        else:
            return num

    return False
