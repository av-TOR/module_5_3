class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        n = 0
        if new_floor > self.number_of_floors or new_floor > 1:
            for i in range(new_floor):
                n += 1
                print(n)
        else:
            print("Такого этажа не существует")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


Home1 = House('Дом', 10)
Home2 = House('Высотка', 20)
# Home1.go_to(0)
# Home2.go_to(3)

print(Home1)
print(Home2)

print(Home1 == Home2)

Home1 = Home1 + 10      # __add__
print(Home1)
print(Home1 == Home2)

Home1 += 10             # __iadd__
print(Home1)

Home2 = 10 + Home2         # __radd__
print(Home2)

print(Home1 > Home2)    # __gt__
print(Home1 >= Home2)   # __ge__
print(Home1 < Home2)    # __lt__
print(Home1 <= Home2)   # __le__
print(Home1 != Home2)   # __ne__
