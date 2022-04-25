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
    line = ['The temperature readings[163.4', ' 78.8', ' 158.0', ' 93.2', ' 68.0', ' 73.4', ' 89.6', ' 125.6', ' 87.8', ' 159.8', ' 104.0', ' 152.6', ' 168.8', ' 165.2', ' 138.2', ' 143.6', ' 170.6', ' 129.2', ' 105.8', ' 122.0', ' 172.4', ' 69.8', ' 95.0', ' 150.8', ' 116.6', ' 141.8', ' 96.8', ' 82.4', ' 136.4', ' 98.6', ' 174.2', ' 107.6', ' 91.4', ' 114.8', ' 131.0', ' 123.8', ' 75.2', ' 80.6', ' 149.0', ' 147.2', ' 84.2', ' 118.4', ' 156.2', ' 134.6', ' 120.2', ' 113.0', ' 102.2', ' 145.4', ' 77.0', ' 140.0]', ' and charge_rate readings [72', ' 60', ' 33', ' 76', ' 61', ' 79', ' 66', ' 20', ' 29', ' 55', ' 25', ' 43', ' 38', ' 37', ' 69', ' 30', ' 78', ' 36', ' 24', ' 22', ' 50', ' 57', ' 47', ' 32', ' 26', ' 42', ' 54', ' 23', ' 63', ' 74', ' 48', ' 49', ' 52', ' 28', ' 45', ' 77', ' 67', ' 70', ' 31', ' 44', ' 34', ' 59', ' 65', ' 40', ' 53', ' 56', ' 58', ' 21', ' 39', ' 27]\n']
    temperature = []
    charge_rate = []
    temperature,charge_rate = receiver.segregateTemperatureandChargerate(line,temperature,charge_rate)
    self.assertTrue(temperature == ['The temperature readings[163.4', ' 78.8', ' 158.0', ' 93.2', ' 68.0', ' 73.4', ' 89.6', ' 125.6', ' 87.8', ' 159.8', ' 104.0', ' 152.6', ' 168.8', ' 165.2', ' 138.2', ' 143.6', ' 170.6', ' 129.2', ' 105.8', ' 122.0', ' 172.4', ' 69.8', ' 95.0', ' 150.8', ' 116.6', ' 141.8', ' 96.8', ' 82.4', ' 136.4', ' 98.6', ' 174.2', ' 107.6', ' 91.4', ' 114.8', ' 131.0', ' 123.8', ' 75.2', ' 80.6', ' 149.0', ' 147.2', ' 84.2', ' 118.4', ' 156.2', ' 134.6', ' 120.2', ' 113.0', ' 102.2', ' 145.4', ' 77.0', ' 140.0]'])
    self.assertTrue(charge_rate ==  [' and charge_rate readings [72', ' 60', ' 33', ' 76', ' 61', ' 79', ' 66', ' 20', ' 29', ' 55', ' 25', ' 43', ' 38', ' 37', ' 69', ' 30', ' 78', ' 36', ' 24', ' 22', ' 50', ' 57', ' 47', ' 32', ' 26', ' 42', ' 54', ' 23', ' 63', ' 74', ' 48', ' 49', ' 52', ' 28', ' 45', ' 77', ' 67', ' 70', ' 31', ' 44', ' 34', ' 59', ' 65', ' 40', ' 53', ' 56', ' 58', ' 21', ' 39', ' 27]\n'])
    
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
