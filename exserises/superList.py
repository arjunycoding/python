class SuperList(list):
  def __len__(self):
    return 1000
superList1 = SuperList()

print(len(superList1))
superList1.append(5)
print(superList1)