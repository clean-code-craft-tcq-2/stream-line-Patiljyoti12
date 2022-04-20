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
  
  def test_filterBatteryParameterValue(self):
    self.assertTrue(receiver.filterBatteryParameterValue(['*12.1/','22.0/','*25.8*','*8.09*','60.0'])==[['12.1'],['22.0'],['25.8'],['8.09'],['60.0']])

  def test_appendNewListWithFloatValue(self):
    newList =[]
    receiver.appendNewListWithFloatValue([['12.1'],['22.0'],['25.8'],['8.09'],['60.0']],newList)
    self.assertTrue(newList == [12.1,22.0,25.8,8.09,60.0])
  
  def test_movingAveragevalue(self):
    self.assertTrue(receiver.movingAveragevalue([40,30,55,50,60],3)==[41.67, 45.0, 55.0])
  
  def test_performOperationsOnBatteryParameters(self):
    batteryParameterSatistics = receiver.BatteryParameterSatistics
    performOperationsOnBatteryParameters(batteryParameterSatistics,[25,30,21,50,60],[40,30,55,50,60])

  def test_getDatafromConsoleOutput(self):
    receiver.getDatafromConsoleOutput()
    
if __name__ == '__main__':
  unittest.main()
