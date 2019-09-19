# This problem was asked by Microsoft.
#
# A number is considered perfect if its digits sum up to exactly 10.
#
# Given a positive integer n, return the n-th perfect number.
#
# For example, given 1, you should return 19. Given 2, you should return 28.


def digits_sum(num,num_1):
    for i in range(0,10):
        if num_1+ i==num:
            print((num_1*10)+i)
 
def main():
    num=int(input("enter number to find addition"))
    num_1=int(input("enter first number"))
    digits_sum(num,num_1)

main()