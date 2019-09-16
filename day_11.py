# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].


def string_query(str,my_list,message):

    message_list = list(message)

    make_list=list(str)
    for m in range(len(message_list)):
        # print(message_list[m])
        if make_list[m]!= message_list[m]:
            return None
    # print("Loop ended")
    my_list.append(str)
    return my_list


def main():
    message = input("enter prefix to find string")
    strings = ['dog', 'deal', 'dear','denmark','angel','angle','america']
    my_list=[]
    for i in strings:
        str=string_query(i,my_list,message)
    print(my_list)

main()