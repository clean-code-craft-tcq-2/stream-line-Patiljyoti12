import receiver
import unittest

class receiver_test(unittest.TestCase):
  def test_getMinimumtemperature(self):
    self.assertTrue(receiver.getMinimumtemperature([25,30,21,50,60])==21)


  def test_getMaximumtemperature(self):
    self.assertTrue(receiver.getMaximumtemperature([25,30,21,50,60])==60)


  def test_getMinimumChargeRate(self):
    self.assertTrue(receiver.getMinimumChargeRate([40,30,55,50,60])==30)


  def test_getMaximumtemperature(self):
    self.assertTrue(receiver.getMaximumChargeRate([40,30,55,50,60])==60)

if __name__ == '__main__':
  unittest.main()
