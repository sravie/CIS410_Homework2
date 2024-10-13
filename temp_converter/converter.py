def convert_fahrenheit_to_celsius(fahrenheit_value):
    celsius_value = (fahrenheit_value - 32) * 5 / 9
    return round(celsius_value)

def convert_celsius_to_fahrenheit(celsius_value):
    fahrenheit_value = (celsius_value * 9 / 5) + 32
    return round(fahrenheit_value)
