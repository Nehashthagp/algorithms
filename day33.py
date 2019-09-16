# This problem was asked by Microsoft.
#
# Compute the running median of a sequence of numbers. That is, given a stream of numbers,
# print out the median of the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
#
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2


def median(num_list):
    for i in range(0, 5):
        num = int(input("enter num in the list"))
        num_list.append(num)
        num_list.sort()
        print(num_list)
        x=len(num_list)
        print("length of list is ", x)

        mod = len(num_list) % 2
        if mod > 0:
            median_odd = len(num_list) // 2
            print("median with length of list odd is ", num_list[median_odd])
        else:
            div = len(num_list) // 2
            median_even = (num_list[div]+ num_list[div-1])/2
            print("median with length of list even is ", median_even)

def main():
    num_list = []
    median(num_list)

main()