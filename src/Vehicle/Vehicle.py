from Logger.Logger import Logger
from time import sleep


class Vehicle:

    def __init__(self) -> None:
        # @info Position of Vehicle in Virtual Coordination_System
        self.x: int = 0
        self.y:int = 0
    
    def turn90Left(self) -> None:
        # todo
        try:
            return
        except Exception as err:
            logger = Logger(None)
            logger.print_err(err)

    def turn90Right(self) -> None:
        # todo
        try:
            return
        except Exception as err:
            logger = Logger(None)
            logger.print_err(err)
    
    def turn180(self) -> None:
        # todo
        try:
            return
        except Exception as err:
            logger = Logger(None)
            logger.print_err(err)

    def driveForwards(self) -> None:
       # todo
        try:
            return
        except Exception as err:
            logger = Logger(None)
            logger.print_err(err)
    
    def stop(self) -> None:
        # todo
        return
    
    def getAllSensorData(self) -> dict: 
        # todo
        try:
            return
        except Exception as err:
            logger = Logger(None)
            logger.print_err(err)
    
    def getSensorDataByID(self, id: int) -> dict:
       # todo
        try:
            return
        except Exception as err:
            logger = Logger(None)
            logger.print_err(err)
