import numpy as np
import scipy as sp
from deci_to_bin import deci_to_bin
import math
from faster_classical_shors import faster_classical_shors_algo
import ast
import time


arr0 = np.array([[1], [0]])
arr1 = np.array([[0], [1]])

def faster_factor(number_to_factor):
    n_bits = len(deci_to_bin(number_to_factor))
    guess = round(math.sqrt(number_to_factor))

    return faster_classical_shors_algo(n_bits, number_to_factor, guess)

def faster_shors_algo(number_to_factor):
    with open("database.txt", "w") as file:
        file.close()

    faster_factor(number_to_factor)
    return_string = ""

    with open("database.txt", "r") as file:
        for line in file:
            return_string = line.strip()
            break
        file.close()


    return_list = ast.literal_eval(return_string)
    return return_list





if __name__=="__main__":
    number_to_factor = int(input("Number to factor: "))
    print()

    start = time.time()
    print("Factors:", faster_shors_algo(number_to_factor))
    end = time.time()

    print()
    print(end - start, "seconds")
    print((end - start)/60, "minutes")

    





# print("Hello, world! This is pi:", sp.constants.pi)
