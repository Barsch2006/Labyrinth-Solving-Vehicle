class Motor:
    def __init__(self) -> None:
        self.power = 0
        #  todo
        self.updatePower()

    def setPower(self, level: int):
        self.power = level
        self.updatePower()
    
    def updatePower(self):
        # todo
        pass
