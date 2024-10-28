# a = []
# d = 0
# for i in range(4):
#     b = int(input("enter a number:"))
#     a.append(b)
#     d += b
# c = d/len(a)
# for i in a:
#     if i < c:
#         a.remove(i)
# print(a)


class Garbage:
    def __init__(self, location, capacity, quantity):
        self.location = location
        self.capacity = float(capacity)
        self.quantity = float(quantity)

    def __str__(self):
        return f"self.locayion = {self.location}"


garbage_can_1 = Garbage("13_street", 100, 35)
garbage_can_2 = Garbage("14_street", 100, 55)
garbage_can_3 = Garbage("15_street", 100, 49)
garbage_can_4 = Garbage("16_street", 100, 30)
garbage_can_5 = Garbage("17_street", 100, 25)
garbage_cans =[garbage_can_1, garbage_can_2, garbage_can_3, garbage_can_4, garbage_can_5]
for i in garbage_cans:
    if i.quantity < i.capacity//2:
        i.quantity = 0
garbage_cans_location = []


def my_garbage_cans(a):
    a = garbage_cans
    for i in my_garbage_cans:







