from os import dup


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# for i in some_list:
#     if some_list.count(i) == 2:
#         duplicates.append(i)
#         some_list.remove(i)
# print(duplicates)

duplicates = list(set([num for num in some_list
if some_list.count(num) > 1]))
print(duplicates)