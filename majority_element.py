"""169. Majority Element
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 """
nums = [2,2,1,1,1,2,2,3]
Dict = {}

# def majority_element(nums):
#     k = 1
#     for i in range(0,len(nums)):
#         if nums[i] in Dict:
#             k +=1
#             Dict.update({nums[i]:k})
#     return Dict
# print(majority_element(nums))
# n = len(nums)
# index = -1
# maxcount = 0
# count = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if nums[i] == nums[j]:
#             count +=1
#         if count > maxcount:
#             maxcount = count
#             index = i
#     print(maxcount)


def majority_element(array):
    majority_number = None
    count = None

    tracker = dict()

    for number in array:
        if number in tracker:
            tracker[number] = tracker[number] + 1
        else:
            tracker[number] = 1

    print(tracker)
    elems = [[key, tracker[key]] for key in tracker]

    def key_find(elem):
        return elem[1]

    # sorted(elems, key=lambda elem:elem[1])
    print(elems)

    elems1 = sorted(elems, key=key_find, reverse=True)

    print(elems1)
    print(elems1[0])

    return {"number": majority_number, "count": None}

    pass


if __name__ == "__main__":
    arr = [1, 2, 1, 3, 3, 3, 4, 4, 4]
    majority_element(arr)

    pass
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

