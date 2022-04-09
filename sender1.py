import random 

def generate_samples(min_value,max_value,no_of_samples):
    result=random.sample(range(min_value, max_value),no_of_samples)
    return result
    
    
def get_temperature_readings(min_value,max_value,no_of_samples):
    temperature_samples=generate_samples(min_value,max_value,no_of_samples)
    fah_temperature_samples=celcius_to_Farenheit_convertor(temperature_samples)
    return fah_temperature_samples
    
def celcius_to_Farenheit_convertor(temperature_samples):
    fah_temperature_samples=[]
    for sample in temperature_samples:
        fah_temperature_samples.append(round(((sample * 1.8) + 32),2))
    return fah_temperature_samples

def get_charge_rate_readings(min_value,max_value,no_of_samples):
    charge_rate_samples=generate_samples(min_value,max_value,no_of_samples)
    return charge_rate_samples
    

def display_samples_on_console(min_value,max_value,no_of_samples):
    fah_temperature_samples=get_temperature_readings(min_value,max_value,no_of_samples)
    charge_rate_samples=get_charge_rate_readings(min_value,max_value,no_of_samples)
    message=format_samples(fah_temperature_samples,charge_rate_samples)
    return message

    
def format_samples(fah_temperature_samples,charge_rate_samples):
    return "The temperature readings{}, and charge_rate readings {}".format(fah_temperature_samples,charge_rate_samples)
    
    
    
