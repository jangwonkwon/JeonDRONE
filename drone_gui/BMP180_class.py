import bmpsensor
import time


class BMP180_data():
    def startBMP(self):
        self.temp, self.pressure, self.altitude = bmpsensor.readBmp180()
        print("Temperature is ",self.temp)  # degC
        print("Pressure is ",self.pressure) # Pressure in Pa 
        print("Altitude is ",self.altitude) # Altitude in meters
        print("\n")

#    time.sleep(0.1)
