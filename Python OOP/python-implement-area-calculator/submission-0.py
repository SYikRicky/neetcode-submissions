import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length: int, width: int = None) -> int:
        if width == None:
            area = length ** 2 * math.pi
            return round(area, 2)
        return length * width

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
