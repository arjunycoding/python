#***********#
# FOR LOOPS #
#***********#

# NOTIOAN:
# for <var> in <iterable(list,dic,str,tuple,ect.)>:
    # <code to be exucuted>

for i in [1,2,3]:
    print(i)
# OUTPUT
# 1
# 2
# 3

#************************#
# FOR LOOPS & DICTIONARY #
#************************#

a = {
    'a':1,
    'b':2,
    'c':3
}

for i in a:
    print(i)
# OUTPUT:
# a
# b
# c
# this is retuning the KEYS of the dict
dict
for i in a.values():
    print(i)

# OUTPUT:
# 1
# 2
# 3
# this is retuning the VALUES of the dict

for i in a.items():
    print(i)

# OUTPUT:
# ('a', 1)
# ('b', 2)
# ('c:', 3)
# this is retuning the KEYS & VALUES of the dict in a TUPLE
