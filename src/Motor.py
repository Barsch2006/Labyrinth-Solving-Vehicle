import pigpio

class Motor:
    def __init__(self, port) -> None:
        self.port = port
        self.pi = pigpio.pi()
        self.power = 0
        #  todo
        self.updatePower()

    def setPower(self, level: int):
        self.power = level
        self.updatePower()

    def updatePower(self):
        if self.power == 1:
            pass
        else:
            self.pi.set_servo_pulsewidth(self.port, 0) # Stop servo pulses.
        pass

    def off(self):
        self.pi.stop()
