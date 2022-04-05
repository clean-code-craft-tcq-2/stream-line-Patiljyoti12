import sender
import unittest 

class sender_test(unittest.TestCase):
  def test_get_temperature_readings(self):
    self.assertTrue((sender.get_temperature_readings(20,100,50))==True)
   
  def test_get_charge_rate_readings(self):
    self.assertTrue((sender.get_charge_rate_readings(10,100,50))==True)

    
    
if __name__ == '__main__':
  unittest.main()
