"""
Chapter 7

Exercise 5: Cities
"""

# A default value was set to the parameter
def describe_city(city, country='Armenia'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

#if in any instances the parameters were set to a default value and the user wants to change country then the parameter should be mentioned to change it
describe_city('Yerevan')  
describe_city('Nairobi', 'Kenya')    
describe_city('Tsaghkadzor', 'Armenia') 
