
import random
 
def get_temperature_readings(min_value,max_value,number):
    result=random.sample(range(min_value, max_value), number)
    if result!=[]:
       return True
    else:
       return False
    
def get_charge_rate_readings(min_value,max_value,number):
    result=random.sample(range(min_value, max_value), number)
    if result!=[]:
       return True
    else:
       return False

def print_to_console(result):
 print("The samples list containg  the streamed data is {}".format(result))
