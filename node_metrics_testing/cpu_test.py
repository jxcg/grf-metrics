import math
import multiprocessing

class Stress:
    def __init__(self) -> None:
        pass

    def calculate_square(self, n: int):
        n = int(n)
        return n**2
    
    def calculate_multi_core(self, cores, args):
        for i in range(1, 1000000000):
            with multiprocessing.Pool(cores) as pool:
                result = pool.map(self.calculate_square, [args, args * 99999999999, args * 99999999999])
        return result




if __name__ == "__main__":
    s = Stress()
    print(s.calculate_multi_core(3, 999999999999))
    


    