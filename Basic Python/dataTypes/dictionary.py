#************#
# DICTIONARY #
#************#
dictionary = {
    123 : [1,2,3],
    True : 'Hello',
    'c' : True
}
# LISTS can not be keys(keys must be IMUTABLE)
# KEYS can NOT be THE SAME
# notaion is {}
# a:1 is know as a key value pari key --> a and value --> 1

# dictionary['b'] to acsess you state the key and it retuns value

dictionary.get('age', 55) #trys to find the age key if not there returns the scond paramitar
dictionary.keys() #retuns keys
dictionary.values() #returns values
dictionary.items() # (In one line )REUNTRS:
dictionary.pop() #takes off the last item
dictionary.popitem() #same as pop
dictionary.update({'c' : False}) #updates the value of the key. If the key is not there adds the key and value
# dict_items([
#   (123, [1, 2, 3]), 
#   (True, 'Hello'), 
#   ('c', True)
# ])

# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE N#
#  MOST of the functions for list work for python
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE N#
