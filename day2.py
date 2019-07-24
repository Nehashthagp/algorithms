# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def arr(my_list):
    new_list = []
    for i in range(len(my_list)):
        # print(i)
        # print(arr_list[i])
        count = 1
        for j in range(len(my_list)):
            """
            if i==j: 
            continue--> iteration continues but when i==j, it ignores and moves to next iteration 
            whereas break  discontinues the iteration.
            """
            if i == j:
                continue
            count = count * my_list[j]
        # print(count)
        new_list.append(count)
    return new_list

def main():
    arr_list=[1,2,3,4,5]
    arr_new_list = arr(arr_list)
    print(arr_new_list)

main()




