class MathOperations:

    def multiply(self, *numbers):
        result = 1

        for num in numbers:
            result = result * num

        return result


obj = MathOperations()

print(obj.multiply(2, 3))
print(obj.multiply(2, 3, 4))