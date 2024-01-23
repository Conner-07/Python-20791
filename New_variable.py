# Function to calculate change
def calculate_change(tendered, cost):
    # Calculate the change
    change = tendered - cost

    # Denominations
    bills_and_coins = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

    # Calculate and print denominations
    i = 0
    while i < len(bills_and_coins):
        denomination_value = int(change // bills_and_coins[i])
        remaining_change = change % bills_and_coins[i]
        print("You gave:", tendered, "and the cost was:", cost, ", so your change in", bills_and_coins[i], "$ bills/coins is:", denomination_value)
        change = remaining_change
        i = i + 1

# Function to convert temperature between scales
def convert_temperature(value, from_scale, to_scale):
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit + 459.67) * 5/9

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(kelvin):
        return (kelvin * 9/5) - 459.67

    # Perform temperature conversion based on scales
    if from_scale == 'Celsius' and to_scale == 'Fahrenheit':
        return celsius_to_fahrenheit(value)
    elif from_scale == 'Celsius' and to_scale == 'Kelvin':
        return celsius_to_kelvin(value)
    elif from_scale == 'Fahrenheit' and to_scale == 'Celsius':
        return fahrenheit_to_celsius(value)
    elif from_scale == 'Fahrenheit' and to_scale == 'Kelvin':
        return fahrenheit_to_kelvin(value)
    elif from_scale == 'Kelvin' and to_scale == 'Celsius':
        return kelvin_to_celsius(value)
    elif from_scale == 'Kelvin' and to_scale == 'Fahrenheit':
        return kelvin_to_fahrenheit(value)
    else:
        return "Invalid temperature scales"

# Separate conversions
print("Temperature Conversion 1:")
result_1 = convert_temperature(98.6, 'Fahrenheit', 'Celsius')
print("Result:", result_1)

print("\nTemperature Conversion 2:")
result_2 = convert_temperature(329.7, 'Kelvin', 'Fahrenheit')
print("Result:", result_2)

print("\nTemperature Conversion 3:")
result_3 = convert_temperature(-60.9, 'Celsius', 'Kelvin')
print("Result:", result_3)

# Example usage of calculate_change
print("\nTransaction Example:")
calculate_change(100, 36.57)
