import sender1
import unittest

def test_generate_samples(self):
    self.assertEqual(len(sender1.generate_samples(10,60,50)==50))
    
def test_temperature_readings(self):
    self.assertTrue(sender1.get_temperature_readings(20,100,50)!=[])
    
def test_celcius_to_Farenheit_converter(self):
    self.assertTrue(sender1.celcius_to_Farenheit_convertor([10,20,30,40]==[50,68,86,104]))
    
def test_chjarge_rate_readings(self):
    self.assertEqual(len(sender1.get_charge_rate_readings(30,120,50)==50))
   
if __name__ == '__main__':
  unittest.main()
    
