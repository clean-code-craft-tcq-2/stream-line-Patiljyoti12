from sender1 import *
import sys

def getDatafromConsoleOutput():
  for line in sys.stdin:
    line=line.split(',')
    print(line)
    
if __name__ == '__main__':
  getDatafromConsoleOutput()
