# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.


num = [5,1,1,5]
# num=[2,4,6,2,5]
list1 = []
for i in range(0, len(num)):

    for j in range(2, len(num)):
        #         print(num[j])
        num_added = 0

        for k in range(i, len(num), j):
            num_added = num_added + num[k]
            # print("value of num_added ", num_added)
            list1.append(num_added)
#         print(list1)
print(max(list1))

