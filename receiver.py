from sender1 import *
import sys

def getDatafromConsoleOutput():
  if(sys.stdin):
    print('data available')
  else:
    print('data not available')
