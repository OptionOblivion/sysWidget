import psutil
import pprint


class Batteries():

    def __init__(self):
        pass

    def _getBatteries(self):

        bat = psutil.sensors_battery()

        print(type(bat))

class CPU():

    def __init__(self):
        pass

class RAM():

    def __init__(self):
        pass

class DISK():

    def __init__(self):
        pass

class NET():

    def __init__(self):
        pass

if __name__ == '__main__':

    q = QueryBatteries()
    q._getBatteries()