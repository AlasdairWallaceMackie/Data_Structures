import unittest
from unittest.case import TestCase

class SL_Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class S_List:
    def __init__(self):
        self.head = None

    def get_length(self):
        counter = 0
        runner = self.head
        while runner != None:
            runner = runner.next
            counter+=1
        return counter


    def add_to_front(self, val, *values):
        new_node = SL_Node(val)
        new_node.next = self.head
        self.head = new_node

        if values != None:
            counter = 1
            for v in values:
                self.insert_at(v, counter)
                counter += 1

        return self

    def add_to_back(self, val, *values):
        new_node = SL_Node(val)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node

        for v in values:
            self.add_to_back(v)

        return self

    def insert_at(self, val, n):
        runner = self.head
        if runner == None or n == 0:
            self.add_to_front(val)
            return self
        elif n < 0:
            n = self.get_length() + n #Has to be "+" otherwise it's a double negative
            self.insert_at(val, n)
            return self
        elif n >= self.get_length():
            self.add_to_back(val)
            return self

        for i in range(n-1): #-1 because the runner always needs to be able to look ahead
            runner = runner.next
        
        new_node = SL_Node(val)
        new_node.next = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        new_head = self.head.next
        self.head.next = None
        removed_value = self.head.value
        self.head = new_head
        return removed_value

    def remove_from_back(self):
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value

    def remove_val(self, val):
        runner = self.head
        if runner != None:
            if runner.value == val: #If first value == val
                self.remove_from_front()
                return self
            else:
                while runner.next.value != val:
                    runner = runner.next
                    if runner.next == None:
                        break
                runner.next = runner.next.next #Removes the node and links the two around it
                return self
                        
        # print("Value not found")
        return self
        

    def print_values(self):
        runner = self.head
        while runner != None:
            print (runner.value)
            runner = runner.next
        return self

    def return_values(self): #For testing
        val_list = []
        runner = self.head
        
        if runner == None:
            return "List is empty"

        while runner != None:
            val_list.append(runner.value)
            runner = runner.next
        return val_list

class Testers(unittest.TestCase):
    def setUp(self):
        self.node_list = S_List()
        self.multi_node_list = S_List()
        self.single_item_list = S_List()
        self.single_item_list.add_to_front('A')
        self.multi_node_list.add_to_front('A').add_to_back('B').add_to_back('C')

    def test_get_length_empty_list(self):
        self.assertEqual( self.node_list.get_length(), 0)
    def test_get_length_single_item(self):
        self.assertEqual( self.single_item_list.get_length(), 1)
    def test_get_length_multi_item(self):
        self.assertEqual( self.multi_node_list.get_length(), 3)

    def test_Add_to_Front_single_item(self):
        self.assertEqual( self.node_list.add_to_front("A").return_values(), ['A'] )
    def test_Add_to_Front_many_items(self):
        self.assertEqual( self.node_list.add_to_front("C").add_to_front("B").add_to_front("A").return_values(), ['A','B','C'])
    def test_add_to_front_multiple_args(self):
        self.assertEqual( self.node_list.add_to_front('A','B','C','D','E').return_values(), ['A','B','C','D','E'] )

    def test_add_to_back_empty_list(self):
        self.assertEqual( self.node_list.add_to_back('X').return_values(), ['X'] )
    def test_add_to_back_single_list(self):
        self.assertEqual( self.single_item_list.add_to_back('X').return_values(), ['A','X'] )
    def test_add_to_back_multi_list(self):
        self.assertEqual( self.multi_node_list.add_to_back('X').return_values(), ['A','B','C','X'] )
    def test_add_to_back_multi_args(self):
        self.assertEqual( self.multi_node_list.add_to_back('X','Y','Z').return_values(), ['A','B','C','X','Y','Z'] )

    def test_insertion_multi_items(self):
        self.assertEqual( self.multi_node_list.insert_at('X', 1).return_values(), ['A','X','B','C'] )
    def test_insertion_single_item_out_of_bounds(self):
        self.assertEqual( self.single_item_list.insert_at('X',12).return_values(), ['A','X'] )
    def test_insertion_multi_list_last_index(self):
        self.assertEqual( self.multi_node_list.insert_at('X', 2).return_values(), ['A','B','X','C'] )
    def test_insertion_multi_list_negative_n(self):
        self.assertEqual( self.multi_node_list.insert_at('X', -2).return_values(), ['A','X','B','C'] )
        
    def test_remove_val_empty_list(self):
        self.assertEqual( self.node_list.remove_val('X').return_values(), "List is empty" )
    def test_remove_val_single_item(self):
        self.assertEqual( self.single_item_list.remove_val('A').return_values(), "List is empty" )
    def test_remove_val_multi_list_beginning(self):
        self.assertEqual( self.multi_node_list.remove_val('A').return_values(), ['B','C'] )
    def test_remove_val_multi_list_middle(self):
        self.assertEqual( self.multi_node_list.remove_val('B').return_values(), ['A','C'] )
    def test_remove_val_multi_list_end(self):
        self.assertEqual( self.multi_node_list.remove_val('C').return_values(), ['A','B'] )


if __name__ == '__main__':
    unittest.main()

# node_list = S_List()
# node_list.add_to_front('A','B','C').print_values()
# node_list.remove_val('B').print_values()


# new_list = S_List()
# for i in range(10):
#     new_list.add_to_front(i)

# new_list.print_values().add_to_back(13).print_values()

# node_list = S_List()
# # node_list.add_to_front("XCOM").add_to_front("That's").add_to_back("Baby!").add_to_back("1").add_to_back("2").add_to_back("3")
# node_list.add_to_back("A")

# # node_list.remove_from_front()
# # node_list.remove_from_back()

# node_list.remove_val("That's")

# node_list.print_values()
