class BMW():
    def country(self):
        print("BMW is from Germany")

    def founder(self):
        print("BMW was founded by Franz Josef Popp")

    def type(self):
        print("BMW makes luxury and performance cars")


class Ferrari():
    def country(self):
        print("Ferrari is from Italy")

    def founder(self):
        print("Ferrari was founded by Enzo Ferrari")

    def type(self):
        print("Ferrari makes luxury sports cars")


obj_bmw = BMW()
obj_ferrari = Ferrari()

for car in (obj_bmw, obj_ferrari):
    car.country()
    car.founder()
    car.type()