class Robot():
    def __init__(self):
        pass

    def intro(self):
        age = int(input("Enter your age: "))
        #Decision making
        if age < 18:
            print("You are not eligible")

        else:
            print("On to the next stage :)")

    def __add__(self, x, y, ans):
        self.x = 70
        self.y = 80
        self.ans = x + y
        print("Can you guess what 70 plus 80 is?")
        answer = input("Was your answer", self.ans, "?: ")
        #Decision making
        yes = True
        No = False
        ###
        if answer == yes:
            print("Well done!")

        else:
            print("Are you good at math?")

        r1 = Robot()
        r1.intro()
        r1.__add__()
        













