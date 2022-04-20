from receiver import *
import unittest

def test_getMinimumtemperature(self):
  self.assertEqual(receiver.getMinimumtemperature(25,30,21,50,60)==21)


def test_getMaximumtemperature(self):
  self.assertEqual(receiver.getMaximumtemperature(25,30,21,50,60)==60)


def test_getMinimumChargeRate(self):
  self.assertEqual(receiver.getMinimumChargeRate(40,30,55,50,60)==30)


def test_getMaximumtemperature(self):
  self.assertEqual(receiver.getMaximumChargeRate(40,30,55,50,60)==60)

if __name__ == '__main__':
  getDatafromConsoleOutput()
  unittest.main()
