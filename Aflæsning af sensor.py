import smufy as sy

import serial #Importere seriel kommonikation
import numpy as np #Importere matematisk bibliotek
import matplotlib.pyplot as plt #importere as plot bibliiotek
from drawnow import *

plt.ion() #Plotting live data (Interative live data)

ThermistorTempC = []
MCP1TempC = []
MCP2TempC = []
cnt=0

ArduinoData = serial.Serial('COM9',115200)


def Figgur(): #Laver en funtion til vore plot
    #Første plot er med en yakse mellem 10 og 40, den anden er 'fri'
    plt.ylim(10,40) # y axies limit
    plt.title('Tempratures') #Tittle of the plot
    plt.grid(True) #Show grid
    plt.ylabel('Temperature') #Label y axies
    plt.xlabel('Time') #Label x axies
    plt.plot(ThermistorTempC, 'r-', label = 'Thermistor') #Plot ThermistorTempC, redline and name it "Thermistor"
    plt.plot(MCP1TempC, 'g-', label = 'MCP1') #Plot MCP1TempC, greenline and name it "MCP1"
    plt.plot(MCP2TempC, 'y-', label = 'MCP2') #Plot MCP2TempC, yellowline and name it "MCP2"
    plt.legend(loc = 'upper left') #Label for the funtions
    
    plt2 = plt.twinx() #Make a new plot in the same plot, with another y axies and with the same x axies
    plt2.ticklabel_format(useOffset=False) #Force the second plot not the autoscale the y axies
    plt2.set_ylabel('Free Temperatur.')
    
    plt.plot(ThermistorTempC, 'ro', label = 'Thermistor copy') #Plot ThermistorTempC, reddot and name it "Thermistor copy"
    plt.plot(MCP1TempC, 'go', label = 'MCP1 copy') #Plot MCP1TempC, greendot and name it "MCP1 copy"
    plt.plot(MCP2TempC, 'yo', label = 'MCP2 copy') # Plot MCP2TempC, yellowdot and name it "MCP2 copy"
    plt.legend(loc = 'upper right') #Label for funtions in plot 2
    
    

while True: #Et whileloop der køre for evigt
    while (ArduinoData.inWaiting()==0): #Vent intil der er data
        pass #Do nothing
    ArduinoString = ArduinoData.readline() #Læst data i fra Arduino
    data = ArduinoString.decode().split(" , ") #Flå data op til en Array(data)
    Thermistor = float(data[0]) #Værdi for Thermistor
    MCP1 = float(data[1]) #Værdi for MCP
    MCP2 = float(data[2]) #Værdi for MCP
    
    ThermistorTempC.append(Thermistor) #Array with all the values in
    MCP1TempC.append(MCP1)#Array with all the values in
    MCP2TempC.append(MCP2)#Array with all the values in
    
    drawnow(Figgur)    #Calls for the funtion to plot it
    plt.pause(0.000001) #Pass
    cnt = cnt+1 #How many times/ plot-point it has gone through
    
    if(cnt>50): #Funtion that actives when the plot-point are at 50
        ThermistorTempC.pop(0) #Deletes the first value ine the array
        MCP1TempC.pop(0)#Deletes the first value ine the array
        MCP2TempC.pop(0)#Deletes the first value ine the array
    