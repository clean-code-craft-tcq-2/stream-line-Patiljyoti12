from sender1 import *
import sys

def getDatafromConsoleOutput():
  for line in sys.stdin:
    temperature =[]
    line=line.split('[')
    print(line)
    index=0
    if "temperature" in line[index]:
      while("charge_rate" is not in line[index]):
        index=index+1
        tempeataure = temperature.append(line[index])

if __name__ == '__main__':
  getDatafromConsoleOutput()
