class TemperatureConverter:

    def convert(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        print("Fahrenheit:", fahrenheit)
        print("Kelvin:", kelvin)


obj = TemperatureConverter()

obj.convert(25)