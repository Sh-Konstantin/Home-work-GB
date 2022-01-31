class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order (self, row_len):
        result = ['*' * row_len] * (self.nums // row_len)
        if self.nums % row_len:
            result.append('*'* (self.nums % row_len))
        return '\n' .join(result)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('sum of cell is:')
        return Cell (self.nums + other.nums)

    def __sub__(self, other):
        print('Subtraction =of cell is ')
        if self.nums <other.nums:
            raise  ValueError( 'вычитание не воможно, ячеек в первой клетке меньше чем во второй')
        return Cell (self.nums - other.nums)

    def __mul__(self, other):
        print("Multiplay of cell is")
        return Cell (self.nums - other.nums)

    def __floordiv__(self, other):
        print ("Floordiv of cell is:")
        return  Cell(self.nums // other.nums)


ceLL_1 = Cell (15)
ceLL_2 = Cell (13)

print (ceLL_1 + ceLL_2)
print (ceLL_1 - ceLL_2)
print (ceLL_1 * ceLL_2)
print (ceLL_1 // ceLL_2)
print (ceLL_1. make_order(7))