class Robot():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def adds(self):
        print("My name is", self.name, "i am", self.age)

        r1 = Robot("Roy", 40)
        r1.adds()

class Intelligence(Robot):
    def __init__(self, speech):
        super().__init__(self, name, age)
        self.speech = speech

        def multi(self):
            print("Okay can you", self.speech)

        r2 = Intelligence("talk?")
        r2.multi()


        
