from sender1 import *
import sys
import re

def getDatafromConsoleOutput():
  for line in sys.stdin:
    temperature = []
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
      temperature[i] = re.findall(r"[-+]?\d*\.\d+|\d+", temperature[i])
      charge_rate[i] = re.findall(r"[-+]?\d*\.\d+|\d+", charge_rate[i])
    maximum_charge_rate = max(charge_rate)
    minimum_charge_rate = min(charge_rate)
    minimum_temperature = min(temperature,key=lambda x:float(x))
    maximum_temperature = max(temperature,key=lambda x:float(x))
    print(maximum_temperature)
    print(minimum_temperature)

if __name__ == '__main__':
  getDatafromConsoleOutput()
