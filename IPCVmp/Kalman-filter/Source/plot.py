import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('output_kalman.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[1]))
        y.append(int(row[2]))

plt.plot(x,y, label='Kalman filter')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kalman filter')
plt.legend()
plt.show()