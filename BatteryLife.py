import psutil
import pprint


class QueryBatteries():

    def __init__(self):
        pass

    def _getBatteries(self):

        bat = psutil.sensors_battery()

        print(type(bat))



if __name__ == '__main__':

    q = QueryBatteries()
    q._getBatteries()