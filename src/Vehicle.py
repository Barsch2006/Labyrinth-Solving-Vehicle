from time import sleep
from Logger.Logger import Logger
from Motor import Motor

class Vehicle:

    def __init__(self, motorR, motorL) -> None:
        self.motorR: Motor = Motor(motorR)
        self.motorL : Motor = Motor(motorL)
    
    def turn90Left(self) -> None:
        # todo
        try:
            self.motorR.setPower(2)
            self.motorL.setPower(1)
            sleep(1)
            self.stop()
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)

    def turn90Right(self) -> None:
        # todo
        try:
            self.motorR.setPower(1)
            self.motorL.setPower(2)
            sleep(1)
            self.stop()
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)

    def driveForwards(self) -> None:
        try:
            self.motorL.setPower(3)
            self.motorR.setPower(3)
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)
    
    def stop(self) -> None:
        self.motorL.setPower(0)
        self.motorR.setPower(0)

    def destroy(self) -> None:
        self.motorL.stop()
        self.motorR.stop()
        self.motorL.stop()
        self.motorR.stop()
