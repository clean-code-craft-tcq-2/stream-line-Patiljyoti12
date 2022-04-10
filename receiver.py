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

def getMinimumChargeRate(charge_rate):
  return min(charge_rate)

def getMaximumChargeRate(charge_rate):
  return max(charge_rate)
  
def getDatafromConsoleOutput():
  for line in sys.stdin:
    temperature = []
    temperature1 = []
    charge_rate = []
    charge_rate1 = []
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
    for i in range(len(temperature)):
      temperature1.append(temperature[i][0])
    for i in range(len(charge_rate)):
      charge_rate1.append(charge_rate[i][0])
    maximum_charge_rate = getMaximumChargeRate(charge_rate1)
    minimum_charge_rate = getMinimumChargeRate(charge_rate1)
    maximum_temperature = getMaximumtemperature(temperature1)
    minimum_temperature = getMinimumtemperature(temperature1)
    print(maximum_charge_rate)
    print(minimum_charge_rate)
            
if __name__ == '__main__':
  getDatafromConsoleOutput()
