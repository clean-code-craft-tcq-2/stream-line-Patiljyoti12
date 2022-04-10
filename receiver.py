from sender1 import *
import sys

def getDatafromConsoleOutput():
  for line in sys.stdin:
    temperature = []
    line=line.split(',')
    index=0
    if "temperature" in line[index]:
      while(!("charge_rate" in line[index])):
        temperature.append(line[index])
        index = index+1
    print(temperature)
      

if __name__ == '__main__':
  getDatafromConsoleOutput()
