class Robot():
    def __init__(self):
        pass

    def intro(self):
        name = input("Enter your names: ")
        print("Welcome", name)
        age = int(input("Enter your age: "))
        #Decision making
        if age < 10:
            print("You are too young")

        else:
            print("On to the next stage")

    def __add__(self, a, b, sum):
        self.a = a
        self.b = b
        self.sum = a + b
        #User input
        sum = int(input("if you spent $140 on clothes and $150 on groceries, What would be your total spending? "))
        #Decision making
        if sum == 290:
            print("Correct :) ")

        else:
            print("Wrong, try again!")
            sum = int(input("if you spent $140 on clothes and $150 on groceries, What would be your total spending? "))
            print("Correct...")


    def __sub__(self, x, y, min):
        self.x = x
        self.y = y
        self.min = x - y
        #User input
        min = int(input("You also have $70, but you'll need $50 to get back home. How much will remain? "))
        #Decision making
        if min == 20:
            print("Good, you know basic math :) ")

        else:
            print("Are you good at math?, try again...")
            min = int(input("You also have $70, but you'll need $50 to get back home. How much will remain? "))
            ###
            print("lets move to something about multiples ;) ")


    def __mul__(self, o, q, h, pro):
        self.o = o
        self.q = q
        self.h = h
        self.pro = o * q * h
        print("Okay, so you just got home from shopping...right")
        print("And now, you need to calculate the product of 7 Bananas, 5 apples and 4 lemons to keep in refrigirator... ")
        #User input
        pro = int(input("So how many Fruits will we regrigirate? "))
        #Decision making
        if pro == 140:
            print("Well done!")

        else:
            print("Oops, try again...")
            ###
            pro = int(input("Last chance. How many Fruits will we regrigirate? "))
            print("Very good, i think we're done here :) ")


r1 = Robot()
r1.intro()
r1.__add__(140, 150, 290)
r1.__sub__(70, 50, 20)
r1.__mul__(7, 5, 4, 140)





