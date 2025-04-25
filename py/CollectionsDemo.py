import random
import time
from ArrayDemo import ArrayDemo
from LinkedListDemo import LinkedListDemo
from VectorDemo import VectorDemo

HOW_MANY_NUMS = 10**6
SEED = 5564011392837540628

def measure_time(cls, how_many_nums, rand):
    start = time.time()
    cls(how_many_nums, rand)
    end = time.time()
    print(f"{cls.__name__} Time: {end - start:.3f} seconds")

def main():
    rand = random.Random(SEED)
    measure_time(ArrayDemo, HOW_MANY_NUMS, rand)
    measure_time(VectorDemo, HOW_MANY_NUMS, rand)
    measure_time(LinkedListDemo, HOW_MANY_NUMS, rand)

if __name__ == "__main__":
    main()
