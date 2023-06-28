import os
import time
from date_parser import parser

class Logger:

    def __init__(self, path: str or None) -> None:
        if (path == None):
            self.__path = os.path.join(os.getcwd(), 'logs')
        else:
            self.__path = path

        if (os.path.exists(self.__path) == False and os.path.isdir(self.__path) == False):
            os.mkdir(self.__path)

    def log(self, mode: str, title: str, msg: str) -> None:
        file = os.path.join(self.__path, f"{str(parser.dateutil.parser.parse(time.asctime())).split(' ')[0]}-{title.upper()}.log")

        if (os.path.exists(file) == False):
            f = open(file, "w")
            f.write(f"[INFO] {str(parser.dateutil.parser.parse(time.asctime())).split(' ')[0]} Begin of LOG {title.upper()}\n")
            f.close()

        f1 = open(file, "a")
        f1.write(f"[{mode.upper()}] {str(parser.dateutil.parser.parse(time.asctime())).split(' ')[0]} {msg}\n")
        f1.close()
    
    def log_err(self, err: str) -> None:
        self.log("ERROR", err)
        print(f"\033[91m{err}")
        print("\033[0m")
