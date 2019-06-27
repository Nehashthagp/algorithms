# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7,2] and k of 17, return true since 10+3+2 is 15.

def check_num():
    my_list= [10,3,7,5,9,6,2]
    k=8
    for i in range(len(my_list)):
        # print (list[0])
        for j in range(i+1, len(my_list)):
            for m in range(j+1, len(my_list)):
                # print(my_list[m])
                if my_list[i]+ my_list[j]+my_list[m]== k:
                    return True
    return False


var=check_num()

print(var)

print(" This is the end of code")