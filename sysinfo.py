import psutil
import pprint


class Batteries():

    def __init__(self):
        pass

    def _getBatteries(self):

        bat = psutil.sensors_battery()

        print(type(bat))

class CPU:

    def __init__(self):
        pass

    def get_cpu(self):
        x = psutil.cpu_percent()
        float(x)
        return x


class RAM():

    def __init__(self):
        pass

    def get_RAM(self):
        ram=psutil.virtual_memory()
        total = ram.total >> 30
        return total



class DISK():

    def __init__(self):
        pass

class NET():

    def __init__(self):
        pass

if __name__ == '__main__':

    q = QueryBatteries()
    q._getBatteries()
