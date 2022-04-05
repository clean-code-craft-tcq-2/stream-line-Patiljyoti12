
import random
 
def get_temperature_readings(min_value,max_value,number):
    if min_value>0 and max_value>0:
        result=random.sample(range(min_value, max_value), number)
        return True
    else:
        return False
    
def get_charge_rate_readings(min_value,max_value,number):
    if min_value>0 and max_value>0:
        result=random.sample(range(min_value, max_value), number)
        return True 
    else:
        return False
