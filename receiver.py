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
    print(temperature)
    print(charge_rate)
    for i in range(len(temperature)):
      temperature[i] = re.findall(str(temperature[i]))
    print(temperature)
      

if __name__ == '__main__':
  getDatafromConsoleOutput()
