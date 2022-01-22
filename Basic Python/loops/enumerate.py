#***********#
# ENUMERATE #
#***********#

# gives the index of the itterable you use
for i,char in enumerate('hello'):
    print(i, char)
# With varible i
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o

# withour varible i
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# find the index of 50 is in the list
for i,char in enumerate(list(range(100))):
    print(i, char)


# scroll down for awnser























































# ANSWER:
for i,char in enumerate(list(range(100))):
    if char == 50:
        print(i)