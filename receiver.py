from sender1 import *
import sys

def getDatafromConsoleOutput():
  for line in sys.stdin:
    line=line.split(',','[',']')
    for character in line:
      if "temperature" in character:
        for i in character:
          print(i)
      elif "charge_rate" in character:
        for i in character:
          print(i)  
        
if __name__ == '__main__':
  getDatafromConsoleOutput()
