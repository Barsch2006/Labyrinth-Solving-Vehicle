"""
Main
"""

from Vehicle import Vehicle
from Logger.Logger import Logger
from time import sleep

logger: Logger = Logger(None)
vehicle: Vehicle = Vehicle(1,2) # create vehicle with both motors
print("Driving")
vehicle.driveForwards() # drive straight forwards
sleep(2)
print("Stopping")
vehicle.stop()
sleep(5)
print("Driving")
vehicle.driveForwards()
sleep(5)
print("Destroying Vehicle")
vehicle.destroy()
print("Finished")
