import sender1

def test_celcius_to_Farenheit_convertor(temperature_samples,expected_temperature_samples):
    fah_temperature_samples=sender1.celcius_to_Farenheit_convertor(temperature_samples)
    assert(fah_temperature_samples==expected_temperature_samples)


def test_generate_samples(min_value,max_value,no_of_samples,expected_length_value):
    result=sender1.generate_samples(min_value,max_value,no_of_samples)
    resultantsamples_length=len(result)
    assert(resultantsamples_length==expected_length_value)
    
def test_charge_rate_readings(min_value,max_value,no_of_samples,expected_length_value):
    charge_rate_samples=sender1.get_charge_rate_readings(min_value,max_value,no_of_samples)
    resultantsamples_length=len(charge_rate_samples)
    assert(resultantsamples_length==expected_length_value)
 

    

if __name__ == '__main__':
   test_celcius_to_Farenheit_convertor([10,20,30,40],[50.0,68.0,86.0,104.0])
   test_generate_samples(20,100,50,50)
   test_charge_rate_readings(20,40,10,10)
   print(sender1.display_samples_on_console(20,80,50))#printing to consider as an input for receiver code
  
  
    
