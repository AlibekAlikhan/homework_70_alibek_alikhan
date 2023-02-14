from random import randint


class Cat:
    year = 2
    happiness = 10
    satiety = 40
    sleep = ""
    img = ''



    def slepp(self):
        self.satiety -= 10
        self.sleep = 'sleep'

    def eat(self):
        self.satiety += 15
        self.happiness += 5
        if self.satiety >= 100:
            self.happiness -= 30

    def play(self):
        self.happiness += 15
        self.satiety -= 10
        if 1 == randint(1, 3):
            self.happiness = 0
        if self.satiety == 'sleep':
            self.sleep = ''
            self.happiness -= 5



