test = 1
test01 = 1
test_01 = 1
_test_01 = 1



example_list_01 = []                        #creat empty list
example_list_02 = [1, 2.0, 'c', [0, 'a']]   #creat list with multiple types data
print(example_list_01)
print(example_list_02)

#example_list_03 = []                     #creat empty list
#example_list_03.append([1, 2, 3])        #add data as a single element
#example_list_03.extend(['a', 'b', 'c'])  #add data as a different element
#example_list_03.insert(0)                #add data in front of the list


example_dict_01 = {}                        #creat empty dictionary
example_dict_02 = {1: 0, 2: 'a', 3: 2.0}    #creat dictionary with multiple types data
print(example_dict_01)
print(example_dict_02)


example_tuple_01 = ()                       #creat empty tuple
example_tuple_02 = (1, 'b',3.0)             #creat tuple with multiple types data
print(example_tuple_01)
print(example_tuple_02)


example_set_01 = set()                          #creat empty tuple
example_set_02 = {0, 0, 'b', 'b', 3.0}   #creat tuple with multiple types data
print(example_set_01)
print(example_set_02)


example_stack_01 = [2, 3, 4]
example_stack_01.append(5)
print(example_stack_01)

example_stack_01.pop()
print(example_stack_01)

>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
