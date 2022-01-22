class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
def oldestCat(*args):
    return max(args)
cat1 = Cat('Tom', 1)
cat2 = Cat('Jhon', 2)
cat3 = Cat('Bob', 3)
old = oldestCat(cat1.age, cat2.age, cat3.age)
print(f"The oldest cat is {old} years old")