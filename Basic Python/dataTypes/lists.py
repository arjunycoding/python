#*******#
# LISTS #
#*******#

# Notation is []

li = [1, 2, 3, 4, 5] # lists can contain ints and floats
li2 = ["a", "b", "c"] # lists can contain strs
li3 = [True, False] # lists can contain bools
li4 = [1, "a", True] # lists can contain different data types


#*********#
# INDEXES #
#*********#

amozon_cart = ['notebooks', 'sunglasses']
amozon_cart[0] # returns 'notebooks'
amozon_cart[0] # returns 'sunglsses'

#*********#
# SLICING #
#*********#

amozon_cart = ['notebooks', 'sunglasses', 'toys', "grapes"]
amozon_cart[0:2] #notebooks, sunglasses
amozon_cart[0::2] # notebooks, toys

#******************#
# BUILT IN METHODS #
#******************#

# adding
ls = [1, 2, 3, 4, 5]
ls.append(6) # [1, 2, 3, 4, 5, 6]

# insert
ls.insert(9, 4) # [1, 2, 3, 4, 9, 5]

# extend
ls.extend([6, 7 ,8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# remove
ls.pop() # 5 (list is now [1, 2, 3, 4]) you can also inster index inside the ()
ls.remove(4) # [1, 2, 3, 5]
ls.clear() # []

# index
ls.index(2) # retuns the value of the number in teis case 3

# in
1 in ls #True
9 in ls #False

# count
ls.count(1) #retuns how many times value is repeated in this case 1

# list unpacking

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# RESULT
a = 1
b = 2
c = 3
other = [4,5,6,7,8]
d = 9
#********#
# MATRIX #
#********#

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# can be acseesed
matrix[0][1] # returns 2