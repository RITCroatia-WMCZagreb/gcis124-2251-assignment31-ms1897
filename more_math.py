'''
@ASSESSME.USERID: ms1897
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''
import math

def factorial(n):
   if  n > 0:
      factor = 1
      for i in range(1, n + 1):
         factor *= i
      return factor
   else:
      return 0
   
def sqrt(n):
   if n > 0:
      return math.sqrt(float(n))
   else:
      return 0

def trunc(n):
   if n > 0:
      return math.trunc(float(n))      
   else:
      return 0


def fact(n):
   return factorial(n)

def root(n):
   return sqrt(n)

def trunk(n):
   return trunc(n)


def main():
   number_a = int(input("Enter a numeric value: "))
   print(f"{number_a} factorial = {factorial(number_a)}")

   number_b = float(input("Enter a numeric value: "))
   print(f"The square root of {number_b} = {sqrt(number_b)}")

   number_c = float(input("Enter a numeric value: "))
   print(f"{number_c} truncated = {trunc(number_c)}")


if __name__ == "__main__":
    main()