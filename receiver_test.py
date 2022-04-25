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
  
  def test_segregateTemperatureandChargerate(self):
    line = [['The temperature readings[172.4', ' 140.0', ' 174.2', ' 75.2', ' 91.4', 
             ' 150.8', ' 143.6', ' 138.2', ' 87.8', ' 113.0', ' 96.8', ' 125.6', ' 104.0', 
             ' 132.8', ' 129.2', ' 120.2', ' 118.4', ' 165.2', ' 109.4', ' 95.0', ' 145.4', 
             ' 89.6', ' 82.4', ' 163.4', ' 105.8', ' 71.6', ' 141.8', ' 161.6', ' 122.0', 
             ' 123.8', ' 168.8', ' 98.6', ' 149.0', ' 136.4', ' 100.4', ' 80.6', ' 158.0', 
             ' 159.8', ' 73.4', ' 68.0', ' 84.2', ' 170.6', ' 167.0', ' 131.0', ' 127.4', 
             ' 156.2', ' 114.8', ' 116.6', ' 78.8', ' 147.2]', 
             ' and charge_rate readings [27', ' 42', ' 66', ' 40', ' 60', ' 67', ' 73', 
             ' 77', ' 68', ' 56', ' 38', ' 78', ' 32', ' 44', ' 47', ' 31', ' 21', ' 22', 
             ' 45', ' 53', ' 30', ' 23', ' 46', ' 76', ' 74', ' 43', ' 25', ' 29', ' 41', 
             ' 55', ' 62', ' 33', ' 26', ' 51', ' 49', ' 75', ' 39', ' 20', ' 37', ' 63', 
             ' 64', ' 24', ' 52', ' 48', ' 54', ' 72', ' 61', ' 69', ' 65', ' 59]\n']]
    temperature = []
    charge_rate = []
    print(receiver.segregateTemperatureandChargerate(line,temperature,charge_rate))
  
  def test_performOperationsOnBatteryParameters(self):
    receiver.performOperationsOnBatteryParameters([25,30,21,50,60],[40,30,55,50,60],3)
    self.assertTrue(receiver.BatteryParameterStatistics['maximum_temperature'] == 60)
    self.assertTrue(receiver.BatteryParameterStatistics['minimum_temperature'] == 21)
    self.assertTrue(receiver.BatteryParameterStatistics['maximum_chargerate'] == 60)
    self.assertTrue(receiver.BatteryParameterStatistics['minimum_chargerate'] == 30)
    self.assertTrue(receiver.BatteryParameterStatistics['movingAverage_temperarture'] == [25.33,33.67,43.67])
    self.assertTrue(receiver.BatteryParameterStatistics['movingAverage_chargerate'] == [41.67, 45.0, 55.0])

  def test_getDatafromConsoleOutput(self):
    receiver.getDatafromConsoleOutput()
    
if __name__ == '__main__':
  unittest.main()
