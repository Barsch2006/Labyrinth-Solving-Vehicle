import pigpio

class Motor:
    def __init__(self, pin):
        self.max_value = 2000
        self.min_value = 700
        self.pin = pin
        self.max_value = self.max_value
        self.pi = pigpio.pi()
        self.pi.set_servo_pulsewidth(self.pin, 0)
        self.calibrate(self.min_value)

    def calibrate(self, min_value):
        self.pi.set_servo_pulsewidth(self.pin, 0)
        print("Trenne die Batterie und drücke Enter")
        input()
        self.pi.set_servo_pulsewidth(self.pin, self.max_value)
        print("Verbinde jetzt die Batterie... du wirst zwei Pieptöne hören, dann warte auf einen allmählichen Abfallton und drücke Enter")
        input()
        self.pi.set_servo_pulsewidth(self.pin, min_value)
        print("Seltsam, oder? Besonderer Ton")
        time.sleep(7)
        print("Warte...")
        time.sleep(5)
        print("Ich arbeite daran, KEINE SORGEN, WARTEN...")
        self.pi.set_servo_pulsewidth(self.pin, 0)
        time.sleep(2)
        print("Aktiviere den ESC jetzt...")
        self.pi.set_servo_pulsewidth(self.pin, min_value)
        time.sleep(1)
        print("Geschafft!")
    
    def setPower(self, power):
        speed = max(0, min(power, self.max_value))
        self.pi.set_servo_pulsewidth(self.pin, speed)

    def stop(self):
        self.pi.set_servo_pulsewidth(self.pin, 0)
        self.pi.stop()
