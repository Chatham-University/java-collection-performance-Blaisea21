import random

class ArrayDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]
        print("The first few numbers are:")
        print("\n".join(map(str, self.nums[:6])))
        self.mults_of_five()

    def mults_of_five(self):
        multiples = [num for num in self.nums if num % 5 == 0]
        print(f"Found {len(multiples)} multiples of 5.")
