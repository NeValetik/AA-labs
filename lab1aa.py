
import time
import matplotlib.pyplot as plt
def plotFibPerformance(fibFunc, numList):
  times = []
  for n in numList:
    start = time.perf_counter()
    fibFunc(n)
    times.append(time.perf_counter() - start)
  plt.figure(figsize=(10, 6))
  plt.plot(numList, times, "bo-")
  plt.xlabel("n-th Fibonacci Number")
  plt.ylabel("Time (seconds)")
  plt.title(f"Performance of {fibFunc.__name__}")
  plt.grid(True)
  # return plt.gcf()
  plt.show()

def fibonaci_1 (n):
  if n<=1:
    return 1
  return fibonaci_1(n-1) + fibonaci_1(n-2)

def fibonaci_2 (n):
  if n <= 0:
    return None  
  elem = [1, 1]  
  for i in range(2, n): 
    elem.append(elem[i-1] + elem[i-2])
  return elem[-1]

def fibonaci_3(n, a=1, b=1):
  if n == 0:
    return a
  return fibonaci_3(n - 1, b, a + b)

def fibonaci_4 (n):
  a = (1 + (5**0.5))/2
  b = (1 - (5**0.5))/2
  return (a**(n+1) - b**(n+1))//(5**0.5)

def fibonaci_5 (n):
  
  if (n <= 1): 
    return n

  curr = 0
  prev1 = 1
  prev2 = 0

  for _ in range(2,n): 
    curr = prev1 + prev2
    prev2 = prev1
    prev1 = curr

  return curr

def multiply(mat1, mat2):
  
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    mat1[0][0], mat1[0][1] = x, y
    mat1[1][0], mat1[1][1] = z, w

def matrix_power(mat1, n):
  
  if n == 0 or n == 1:
    return

  mat2 = [[1, 1], [1, 0]]

  matrix_power(mat1, n // 2)

  multiply(mat1, mat1)

  if n % 2 != 0:
    multiply(mat1, mat2)

def fibonaci_6(n):
  if n <= 1:
    return n

  mat1 = [[1, 1], [1, 0]]

  matrix_power(mat1, n - 1)

  return mat1[0][0]


fib_func = fibonaci_5
n_values = list(range(5, 1000, 20))

plotFibPerformance(fib_func, n_values)
