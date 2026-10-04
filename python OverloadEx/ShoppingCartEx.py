class ShoppingCart:

    def total(self, *prices):
        result = 0

        for price in prices:
            result = result + price

        return result


obj = ShoppingCart()

print("Total:", obj.total(100))
print("Total:", obj.total(100, 200))
print("Total:", obj.total(100, 200, 300))