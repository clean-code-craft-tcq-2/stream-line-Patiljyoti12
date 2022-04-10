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
    for i in range(len(temperature)):
      print(type(temperature[i]))
      

if __name__ == '__main__':
  getDatafromConsoleOutput()
