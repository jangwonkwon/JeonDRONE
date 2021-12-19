import bmpsensor
import time


class BMP180_data(self):
    self.temp, self.pressure, self.altitude = bmpsensor.readBmp180()
    print("Temperature is ",temp)  # degC
    print("Pressure is ",pressure) # Pressure in Pa 
    print("Altitude is ",altitude) # Altitude in meters
    print("\n")

#    time.sleep(0.1)
