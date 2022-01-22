#******#
# SETS #
#******#
# UNODERED colection on unque objects
# can not use indexs
my_set = {1,2,3,4,5,5}
# If you were to print this set you qould get {1,2,3,4,5}
my_set.add(100) #adds 100 to the end

#******************#
# BUILT IN METHODS #
#******************#
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

my_set.difference(your_set)# retuns {1,2,3} *no change
my_set.discard(5)# retuns {1,2,3,4}
my_set.differrence_update(your_set)# retuns {1,2,3} **modifyes
my_set.intersection(your_set)#retuns {4,5} 
my_set.isdisjoint(your_set)#retuns False finds if the set haave nothib=ng in common
my_set.issubset(your_set)#retuns False my_set is not insde your_set
my_set.issuperset(your_set)#retuns Fasle revers of issubset
my_set.union(your_set)#retuns {1,2,3,4,5,6,7,8,9,10} **new set removes all duplictates and joins to sets

# EXSERSIZE:
# how can you print [1,2,3,4,5,5] as a set?
# my_list = [1,2,3,4,5,5]
# my_list = set(my_list)
# print(my_list)
