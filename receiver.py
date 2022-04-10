from sender1 import *
import sys

def getDatafromConsoleOutput():
  for line in sys.stdin:
    line=line.split(',')
    for character in line:
      if character.find("temperature"):
        print("The temperature readings{}".format(character))
      elif character.find("charge_rate"):
        print("The charge_rate readings{}".format(character))
        
if __name__ == '__main__':
  getDatafromConsoleOutput()
