import numpy as np
import matplotlib.pyplot as plt

xi = np.array([]) #1,2,3,4,5,6,7
yi = np.array([]) #0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5

n = int(input("Masukkan jumlah data: "))

for i in range(0, n):
    masukX = int(input("Masukkan nilai x ke %d: " % (i+1)))
    xi = np.append(xi, masukX)

for i in range(0, n):
    masukY = float(input("Masukkan nilai y ke %d: " % (i+1)))
    yi = np.append(yi, masukY)

def hitungXiYi(x, y):
    total = 0
    for i in range(0, n):
        total += x[i]*y[i]
    return total

def hitungXi(x):
    total = 0
    for i in range(0, n):
        total += x[i]
    return total

def hitungYi(y):
    total = 0
    for i in range(0, n):
        total += y[i]
    return total

def hitungXi2(x):
    total = 0
    for i in range(0, n):
        total += x[i]**2
    return total

def hitungMeanY(y):
    mean = 0
    total = 0
    for i in range(0, n):
        total += y[i]
    mean = total / n
    return mean

def hitungMeanX(x):
    mean = 0
    total = 0
    for i in range(0, n):
        total += x[i]
    mean = total / n
    return mean

def hitungA1(x, y):
    hasil = (n*hitungXiYi(x, y) - hitungXi(x)*hitungYi(y))/(n*hitungXi2(x) - (hitungXi(x))**2)
    return hasil

def hitungA0(x, y):
    hasil = hitungMeanY(y) - hitungA1(x, y)*hitungMeanX(x)
    return hasil

x = np.arange(0, (xi[-1] + 5), 1)
y = hitungA0(xi, yi) + hitungA1(xi, yi)*x
plt.plot(x, y, label = "Model Regresi", color = "red")
plt.scatter(xi, yi, label = "Titik asli", color = "blue")
plt.grid(True)
plt.legend()
plt.show()