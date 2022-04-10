from sender1 import *
import sys
import re

def getMinimumtemperature(temperature):
  minimum_temperature = float(temperature[0])
  for i in range(len(temperature)):
    if minimum_temperature>float(temperature[i]):
      minimum_temperature = float(temperature[i])
  return minimum_temperature


def getMaximumtemperature(temperature):
  maximum_temperature = float(temperature[0])
  for i in range(len(temperature)):
    if maximum_temperature<float(temperature[i]):
      maximum_temperature = float(temperature[i])
  return maximum_temperature

def getDatafromConsoleOutput():
  for line in sys.stdin:
    temperature = []
    temperature1 = []
    charge_rate = []
    line=line.split(',')
    index=0
    if "temperature" in line[index]:
      while(not("charge_rate" in line[index])):
        temperature.append(line[index])
        index = index+1
      for i in range(index,len(line)):
        charge_rate.append(line[i])
    for i in range(len(temperature)):
      temperature[i]=re.findall(r"[-+]?\d*\.\d+|\d+", temperature[i])
      charge_rate[i]=re.findall(r"[-+]?\d*\.\d+|\d+", charge_rate[i])
    maximum_charge_rate = max(charge_rate)
    minimum_charge_rate = min(charge_rate)
    for i in range(len(temperature)):
      temperature1.append(temperature[i][0])
    for i in range(len(temperature)):
      print(temperature1[i])
    maximum_temperature = getMaximumtemperature(temperature1)
    minimum_temperature = getMinimumtemperature(temperature1)
    print(type(temperature1[0]))
    print(type(temperature1[0]))
            
if __name__ == '__main__':
  getDatafromConsoleOutput()
