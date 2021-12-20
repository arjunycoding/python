#*********#
# STRINGS #
#*********#

'hi hello there' # works with single quotes
"hi hello there" # works with double quotes
"24, a, !"       # works with numbers and other charecters quotes

#****************#
# DIFFERENT WAYS #
#****************#

# 1  means NOTHING
'hi hello there'
# 2  in varibles
username = "supercoder"
# 3  multiline
long_stirng = """
WWW
0 0
---
"""


#***************#
# CONCATENATION #
#***************#

# Adding stirngs together

first_name = "Arjun"
last_name = "Yuvaraj"

full_name = first_name + " " + last_name

#****************#
# CHANGING TYPES #
#****************#

type(str(100)) # <class 'str'>
type(int(str(100))) # <class 'int'>

#****************#
# ESPACE SEQUNCE #
#****************#

# weather = 'it's sunny' == UH OH
# solution one
weather = "it's sunny"
# solution two
weather = 'it\'s sunny'

# \t == add tab
# \n == new line
# \\ == \
# \' == '

#*******************#
# FORMATTED STRINGS #
#*******************#

name = 'Jhonny'
age = 55
print(f"hi, {name}. You are {age} years old.")
#     ^
# making the sitng formtted
# OR...
print("hi, {}. You are {} years old.".format('Jhonny', '55'))

#****************#
# STRING INDEXES #
#****************#

selfish = '01234567'
#          01234567
selfish[7] # returns '7'
selfish[0] # returns '0'
selfish[2] # returns '2'

# [start:stop:step]
selfish[0:8:2] # returns '0246'
selfish[::-1] # returns '76543210'
selfish[::-2] # returns '75310'