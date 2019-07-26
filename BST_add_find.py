class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def insert(self, val):
        if val < self.data:
            if self.left_node == None:
                self.left_node = Node(val)
            else:
                self.left_node.insert(val)

        elif val > self.data:
            if self.right_node == None:
                self.right_node = Node(val)
            else:
                self.right_node.insert(val)

    def find(self, search_num):
        if search_num == self.data:
            print(search_num, 'found')
        elif search_num < self.data:
            if self.left_node == None:
                print(search_num, " not found")
            elif self.left_node.data == search_num:
                print(search_num, " found")
            else:
                self.left_node.find(search_num)


        elif search_num > self.data:
            if self.right_node == None:
                print(search_num, 'not found')
            elif self.right_node.data == search_num:
                print(search_num, " found")
            else:
                self.right_node.find(search_num)

    def print_tree(self):
        if self.data:
            print(self.data)
            if self.left_node:
                self.left_node.print_tree()

            """
            #             check once to see difference
            #             elif self.right_node:     
            #                 self.right_node.print_tree()       

            """

            if self.right_node:
                self.right_node.print_tree()

            print('returning from ', self.data)




r = Node(20)
r.insert(14)
r.insert(23)
r.insert(17)
r.insert(26)
r.insert(12)
r.insert(13)
r.find(17)
r.print_tree()

