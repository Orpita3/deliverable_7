import numpy as np
import pandas as pd

#ask user to enter an integer number Greater then 0
n = int(input("Enter an integer number number Greater then 0: "))
#check if the number is number Greater then 0
while  n <= 0:
    print("The number is not number Greater then 0")
    n = int(input("Enter an integer number number Greater then 0: "))

#n is the length of array

#function to create the even sequence
def EVEN_NUMBERS(n):
    EVEN = []
    for i in range(0,n*2):
            if i % 2 == 0:
                EVEN.append(i)
    return EVEN

#function to create the odd sequence
def ODD_NUMBERS(n):
    ODD = []
    for i in range(0,n*2):
        if i % 2 == 1:
            ODD.append(i)
    return ODD

#function to create the fibonacci sequence
def fibonacci_nums(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n-1:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence

#display the output
df = pd.DataFrame({"EVEN":EVEN_NUMBERS(n), "ODD":ODD_NUMBERS(n), "Fibonacci":fibonacci_nums(n)})
print(df)
