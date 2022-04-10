from sender1 import *
import sys

def getDatafromConsoleOutput():
  for line in sys.stdin:
    line=line.split(',')
    for character in line:
      if "temperature" in character:
        print(character)
      elif "charge_rate" in character:
        print(character)
        
if __name__ == '__main__':
  getDatafromConsoleOutput()
