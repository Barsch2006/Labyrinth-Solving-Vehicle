class Motor:
    def __init__(self) -> None:
        self.power = 0
        #  todo
        self.updatePower()

    def setPower(self, level: int):
        self.power = level
    
    def updatePower(self):
        # todo
        pass
                                
import os
import time
import pigpio

class Motor:
    def __init__(self, pin, max_value):
        self.pin = pin
        self.max_value = max_value
        self.pi = pigpio.pi()
        self.pi.set_servo_pulsewidth(self.pin, 0)

    def drive(self, speed):
        speed = max(0, min(speed, self.max_value))
        self.pi.set_servo_pulsewidth(self.pin, speed)

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

    def stop(self):
        self.pi.set_servo_pulsewidth(self.pin, 0)
        self.pi.stop()


ESC = 4  # Verbinde den ESC mit diesem GPIO-Pin
max_value = 2000  # Ändere diesen Wert, falls der maximale Wert deines ESCs anders ist
min_value = 700   # Ändere diesen Wert, falls der minimale Wert deines ESCs anders ist

motor = Motor(ESC, max_value)

print("Für den ersten Start wähle 'calibrate'")
print("Gib das exakte Wort für die gewünschte Funktion ein")
print("calibrate ODER drive ODER stop")

while True:
    inp = input()

    if inp == "calibrate":
        motor.calibrate(min_value)
        break
    elif inp == "drive":
        print("Du hast die manuelle Option gewählt. Gib einen Wert zwischen 0 und deinem Maximalwert ein.")
        while True:
            speed = int(input())
            if speed == 0:
                motor.stop()
                break
            motor.drive(speed)
    elif inp == "stop":
        motor.stop()
        break
    else:
        print("Bitte gib 'calibrate', 'drive' oder 'stop' ein.")
