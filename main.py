class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        if celsius < -273.15:
            raise ValueError("Temperature value is below absolute zero.")
        fahrenheit = celsius * 9/5 + 32
        return fahrenheit
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        if fahrenheit < -459.67:
            raise ValueError("Temperature value is below absolute zero.")
        celsius = (fahrenheit - 32) * 5/9
        return celsius
try:
    celsius = 25
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")
    fahrenheit = 77
    celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")
    celsius = -300
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")
except ValueError as e:
    print("ValueError:", str(e))
