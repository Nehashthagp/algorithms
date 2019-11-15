# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.


# list1=[-10,-30,-20,2,7]
list1=[-10,-10,5,2]
list_new=[]
for i in range(len(list1)):
    print(list1[i])
    for j in range(i+1, len(list1)):
        mult_num=1
        # print("mult_num is ", mult_num)
        for k in range(j+1, len(list1)):
            print("value of j is ", list1[j])
            print("value of k is ", list1[k])
            mult_num=list1[i]*list1[j]*list1[k]
            list_new.append(mult_num)
print(max(list_new))