from sender1 import *
import sys
import re

def getMinimumtemperature(temperature):
  minimum_temperature = temperature[0]
  for i in range(len(temperature)):
    if minimum_temperature>temperature[i]:
      minimum_temperature = temperature[i]
  return minimum_temperature


def getMaximumtemperature(temperature):
  maximum_temperature = temperature[0]
  for i in range(len(temperature)):
    if maximum_temperature<temperature[i]:
      maximum_temperature = temperature[i]
  return maximum_temperature

def getMinimumChargeRate(charge_rate):
  return min(charge_rate)

def getMaximumChargeRate(charge_rate):
  return max(charge_rate)

def appendNewListWithFloatValue(batteryParameterOld,batteryParameterNew):
  for i in range(len(batteryParameterOld)):
    batteryParameterNew.append(float(batteryParameterOld[i][0]))
  return batteryParameterNew

def filterBatteryParameterValue(batteryParameter):
  for index in range(len(batteryParameter)):
    batteryParameter[index]=re.findall(r"[-+]?\d*\.\d+|\d+", batteryParameter[index])
  return batteryParameter
      
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
    temperature=filterBatteryParameterValue(temperature)
    charge_rate=filterBatteryParameterValue(charge_rate)
    temperature1 = appendNewListWithFloatValue(temperature,temperature1)
    charge_rate1 = appendNewListWithFloatValue(charge_rate,charge_rate1)
    maximum_charge_rate = getMaximumChargeRate(charge_rate1)
    minimum_charge_rate = getMinimumChargeRate(charge_rate1)
    maximum_temperature = getMaximumtemperature(temperature1)
    minimum_temperature = getMinimumtemperature(temperature1)
            
if __name__ == '__main__':
  getDatafromConsoleOutput()
