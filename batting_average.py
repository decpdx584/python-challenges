class BattingAverage():
    def __init__(self, batterName, atBats, strikeOuts, hits):
        self.batterName = batterName
        self.atBats = atBats
        self.strikeOuts = strikeOuts
        self.hits = hits
        self.average = int(hits) / int(atBats)

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

cabassa = BattingAverage("Cabassa", 7, 2, 3)
cabassa.getAHit()
print(cabassa)
