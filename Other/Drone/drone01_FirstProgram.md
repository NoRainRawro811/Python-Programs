from codrone_edu.drone import *

drone = Drone()
drone.pair()

battery = drone.get_battery()      # ask the drone how much charge is left
print("Battery:", battery, "%")    # show it in the Console

drone.close()