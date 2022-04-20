from sender1 import *
import sys
import re

class BatteryParameterStatistics:
  def __init__(self,maximum_temperature,
                    minimum_temperature,
                    maximum_charge_rate,
                    minimum_charge_rate,
                    movingAveragevalue_temperature
                    movingAveragevalue_ChargeRate):
    self.maximum_temperature = maximum_temperature
    self.minimum_temperature = minimum_temperature
    self.maximum_charge_rate = maximum_charge_rate
    self.minimum_charge_rate = minimum_charge_rate
    self.movingAveragevalue_temperature = movingAveragevalue_temperature
    self.movingAveragevalue_ChargeRate = movingAveragevalue_ChargeRate
    
def getMinimumtemperature(temperature):
  minimum_temperature = temperature[0]
  for index in range(len(temperature)):
    if minimum_temperature>temperature[index]:
      minimum_temperature = temperature[index]
  return minimum_temperature


def getMaximumtemperature(temperature):
  maximum_temperature = temperature[0]
  for index in range(len(temperature)):
    if maximum_temperature<temperature[index]:
      maximum_temperature = temperature[index]
  return maximum_temperature

def getMinimumChargeRate(charge_rate):
  return min(charge_rate)

def getMaximumChargeRate(charge_rate):
  return max(charge_rate)

def appendNewListWithFloatValue(batteryParameterOld,batteryParameterNew):
  for index in range(len(batteryParameterOld)):
    batteryParameterNew.append(float(batteryParameterOld[index][0]))
  return batteryParameterNew

def filterBatteryParameterValue(batteryParameter):
  for index in range(len(batteryParameter)):
    batteryParameter[index]=re.findall(r"[-+]?\d*\.\d+|\d+", batteryParameter[index])
  return batteryParameter

def segregateTemperatureandChargerate(line,temperature,charge_rate):
  index=0
  if "temperature" in line[index]:
    while(not("charge_rate" in line[index])):
      temperature.append(line[index])
      index = index+1
    for i in range(index,len(line)):
      charge_rate.append(line[i])
  return temperature,charge_rate

def movingAveragevalue(batteryParameter,windowSize):
  movingAverage = []
  index = 0
  while index < len(batteryParameter)-windowSize+1:
    window = batteryParameter[index:index+windowSize]
    windowAverage = round((sum(window)/windowSize),2)
    movingAverage.append(windowAverage)
    index = index+1
  return movingAverage

def getDatafromConsoleOutput():
  for line in sys.stdin:
    temperature = []
    temperature1 = []
    charge_rate = []
    charge_rate1 = []
    line=line.split(',')
    temperature,charge_rate = segregateTemperatureandChargerate(line,temperature,charge_rate)
    temperature=filterBatteryParameterValue(temperature)
    charge_rate=filterBatteryParameterValue(charge_rate)
    temperature1 = appendNewListWithFloatValue(temperature,temperature1)
    charge_rate1 = appendNewListWithFloatValue(charge_rate,charge_rate1)
    performOperationsOnBatteryParameters(temperature1,charge_rate1)
    
def performOperationsOnBatteryParameters(temperature1,charge_rate1):
  batteryParameterSatistics = BatteryParameterStatistics(getMaximumtemperature(temperature1)
                                                         getMinimumtemperature(temperature1)
                                                         getMaximumChargeRate(charge_rate1)
                                                         getMinimumChargeRate(charge_rate1)
                                                         movingAveragevalue(temperature1,5)
                                                         movingAveragevalue(charge_rate1,5))

if __name__ == '__main__':
  getDatafromConsoleOutput()
