from sender1 import *
import sys

def getDatafromConsoleOutput():
  for line in sys.stdin:
    line=line.split(',')
    for character in line:
      if "temperature" in character:
        index=0
        while (character[index]!= '['):
          list(character)
          del(character[index])
          index=index+1
        del(character[index])
        print(character)
      elif "charge_rate" in character:
        index=0
        while (character[index]!= '['):
          list(character)
          del(character[index])
          index=index+1
        del(character[index])
        print(character)
        
        
if __name__ == '__main__':
  getDatafromConsoleOutput()
