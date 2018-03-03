import serial                                   #import the serial library
import numpy as np                              #numpy is a scientific computing library
import matplotlib.pyplot as plt
import math
import datetime
from tkinter import *

ser = serial.Serial('com3',9600)                #create serial port object
time = 0
Voltage_Source = 5                              #INPUT VOLTAGE (V) - READ CONNECTED PIN VALUE ON ARDUINO (5V OR 3.5V)
Resistance_R2 = 10000                           #(OHMS) SECOND RESISTOR(BROWN BLACK ORANGE GOLD) - FOR VOLTAGE DIVIDER 
Resistance_Thermistor = 10000                   #(OHMS) RESISTANCE OF THERMISTOR - @ certain T for thermistor
Beta = 4100                                     #BETA VALUE (K) - LISTED ON PRODUCT SPEC
inverseBeta = 1/Beta                            #INVERSE OF BETA VALUE (ABOVE)
Kelvin_Base = 273.15                            #BASE KELVIN CONVERSION UNIT
Kelvin_RoomTemp = 298.15                        #KELVIN @ 25 DEGREES CELSIUS (ROOM TEMPERATURE)
inverseT_O = 1/Kelvin_RoomTemp                  #INVERSE OF KELVIN @ ROOM TEMPERATURE (ABOVE)

voltage_resolution = 0.0048828125

f = open("output.txt", "w")

Celsius_A0 = 0
Celsius_A1 = 0
Celsius_A2 = 0
Celsius_A3 = 0

#plt.ion()
#fig = plt.figure()
#ax = fig.add_subplot(111)


#x = np.linspace(0, 2, 4)
#a = np.array([0, 0, 0, 0])
#line1, = ax.plot(x,a, 'b-')

frame = Tk()                                                            #creates tkinter object
frame.geometry("480x360")                                               #defines window dimensions
Label(frame, text="Temperature Readings").grid(row=1, column=1)         #title label text/location
display0 = Label(frame, text="")                                        #label variables
display1 = Label(frame, text="")
display2 = Label(frame, text="")
display3 = Label(frame, text="")
display0.grid(row=2, column=1)                                          #label locations
display1.grid(row=3, column=1)
display2.grid(row=4, column=1)
display3.grid(row=5, column=1)

def main():
    try:
        while True:
            if(ser.inWaiting()>0):        
                data = ser.readline()                    #read the serial input
                data2 = data.decode('ascii')             #converts binary string to string
                #print(data2)
                Voltage_A0, Voltage_A1, Voltage_A2, Voltage_A3 = data2.split(" ")        #Separates the data to individual variables
                #time = time + 1                         #time inremental counter
                
                #print("Voltage_A0=" + Voltage_A0)
                #print("Voltage_A1=" + Voltage_A1)
                #print("Voltage_A2=" + Voltage_A2)
                #print("Voltage_A3=" + Voltage_A3)

                A0 = voltage_resolution*int(Voltage_A0)     #calculates actual voltage reading
                #print("A0=" + str(A0))
                A1 = voltage_resolution*int(Voltage_A1)
                A2 = voltage_resolution*int(Voltage_A2)
                A3 = voltage_resolution*int(Voltage_A3)

                
                Resistance_A0 = Resistance_R2 * ((Voltage_Source - A0)/A0)      #calculates actual temperature
                #print("Resistance_A0=" + str(Resistance_A0))
                if (Resistance_A0 > 0):
                    inverseTemperature_A0 = inverseT_O + inverseBeta*math.log(Resistance_A0/Resistance_Thermistor)
                    Kelvin_A0 = 1/inverseTemperature_A0
                    Celsius_A0 = Kelvin_A0 - Kelvin_Base

                Resistance_A1 = Resistance_R2 * ((Voltage_Source - A1)/A1)
                #print("Resistance_A1=" + str(Resistance_A1))
                if (Resistance_A1 > 0):
                    inverseTemperature_A1 = inverseT_O + inverseBeta*math.log(Resistance_A1/Resistance_Thermistor)
                    Kelvin_A1 = 1/inverseTemperature_A1
                    Celsius_A1 = Kelvin_A1 - Kelvin_Base

                Resistance_A2 = Resistance_R2 * ((Voltage_Source - A2)/A2)
                #print("Resistance_A2=" + str(Resistance_A2))
                if (Resistance_A2 > 0):
                    inverseTemperature_A2 = inverseT_O + inverseBeta*math.log(Resistance_A2/Resistance_Thermistor)
                    Kelvin_A2 = 1/inverseTemperature_A2
                    Celsius_A2 = Kelvin_A2 - Kelvin_Base

                Resistance_A3 = Resistance_R2 * ((Voltage_Source - A3)/A3)
                #print("Resistance_A3=" + str(Resistance_A3))
                if (Resistance_A3 > 0):
                    inverseTemperature_A3 = inverseT_O + inverseBeta*math.log(Resistance_A3/Resistance_Thermistor)
                    Kelvin_A3 = 1/inverseTemperature_A3
                    Celsius_A3 = Kelvin_A3 - Kelvin_Base


                print("Celsius_A0=" + str(Celsius_A0))
                print("Celsius_A1=" + str(Celsius_A1))
                print("Celsius_A2=" + str(Celsius_A2))
                print("Celsius_A3=" + str(Celsius_A3))
                print("\n")


                
                f.write(str(Celsius_A0) + " ")      #output file write segment
                f.write(str(Celsius_A1) + " ")
                f.write(str(Celsius_A2) + " ")
                f.write(str(Celsius_A3))
                f.write("\n")

                
                #a[0] = Celsius_A0
                #a[1] = Celsius_A1
                #a[2] = Celsius_A2
                #a[3] = Celsius_A3
                #line1.set_ydata(a)
                #fig.canvas.draw()


                display0.configure(text="%.2f" %Celsius_A0)     #changes the labels
                display1.configure(text="%.2f" %Celsius_A1)
                display2.configure(text="%.2f" %Celsius_A2)
                display3.configure(text="%.2f" %Celsius_A3)
                frame.update_idletasks()                        #redraws the window
                frame.update()
                
    except KeyboardInterrupt:                                   #checks for control+c keyboard input
        pass                                                    #pass: does nothing


    print("Code is past the loop")
    f.close()                                                   #closes the write file

    
main()

