class BattingAverage():
    def __init__(self, atBats, strikeOuts, hits):
        self.atBats = 0
        self.strikeOuts = 0
        self.hits = 0

    def atThePlate(self, atBats):
        self.atBats += 1
        print(f"Your average is: " + {self.hits}/{self.atBats})

    def strikeOut(self, atBats, strikeOuts):
        self.atBats += 1
        self.strikeOuts += 1
        print(f"Your average is: " + {self.hits}/{self.atBats})


    def getAHit(self, atBats, hits):
        self.atBats += 1
        self.hits += 1
        print(f"Your average is: " + {self.hits}/{self.atBats})

cabassa_average = BattingAverage(7, 2, 3)
cabassa_average.getAHit()
