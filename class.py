class Robot():
    def __init__(self, name, age, hobby, iq, clr):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.iq = iq
        self.clr = clr

    def intro(self):
        print("My name is", self.name, "i am", self.age, "years old")

    def nitro(self):
        print("I play", self.hobby, "i have an IQ score of", self.iq, "and im", self.clr, ":)")

        robot1 = Robot("Mark", 18, "dancing", 75, "red")
        robot2 = Robot("Tom", 20, "swimming", 80, "blue")
        robot1.intro()
        robot1.nitro()
        robot2.intro()
        robot2.nitro()


